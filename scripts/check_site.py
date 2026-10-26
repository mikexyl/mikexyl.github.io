"""Check production output, preserved project URLs, and local link targets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag in {"a", "link", "img", "script", "iframe", "source"}:
            target = attrs.get("href") if tag in {"a", "link"} else attrs.get("src")
            if target:
                self.links.append(target)
        if tag == "img" and "alt" not in attrs:
            errors.append(f"Image has no alternative text in {current_file}")


root = Path("_site").resolve()
required = ["index.html", "projects/index.html", "publications/index.html", "cv/index.html",
            "projects/code-slam/index.html", "projects/cbs/index.html", "projects/coxgraph/index.html",
            "projects/coxgraph/Coxgraph.pdf", "projects/coxgraph/IROS21_0958_VI_fi.mp4",
            "assets/css/main.css", "assets/css/tailwind.css"]
errors = [f"Missing output: {name}" for name in required if not (root / name).is_file()]
pages = {}
for current_file in root.rglob("*.html"):
    page = Page()
    content = current_file.read_text()
    page.feed(content)
    pages[current_file] = page
    for placeholder in ["Albert Einstein", "GitHub University", "Your Name", "def meet(me):"]:
        if placeholder in content:
            errors.append(f"Legacy placeholder {placeholder!r} in {current_file.relative_to(root)}")

for path, page in pages.items():
    origin = "/" + str(path.relative_to(root))
    for target in page.links:
        parsed = urlsplit(target)
        if parsed.scheme in {"mailto", "tel", "data", "javascript"}:
            continue
        if parsed.netloc and parsed.netloc != "mikexyl.github.io":
            continue
        resolved = urlsplit(urljoin(origin, target))
        local = root / unquote(resolved.path).lstrip("/")
        if local.is_dir():
            local = local / "index.html"
        if not local.is_file():
            errors.append(f"Broken local target in {path.relative_to(root)}: {target}")
        elif resolved.fragment and local in pages:
            if unquote(resolved.fragment) not in pages[local].ids:
                errors.append(f"Missing anchor in {path.relative_to(root)}: {target}")

if errors:
    raise SystemExit("\n".join(sorted(set(errors))))
print(f"Checked {len(pages)} HTML pages: required routes, local links, assets, anchors, and image alt attributes pass.")
