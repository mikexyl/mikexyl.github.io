---
layout: page
title: sitemap
permalink: /sitemap/
nav: false
---

- [About]({{ '/' | relative_url }})
- [Projects]({{ '/projects/' | relative_url }})
- [Publications]({{ '/publications/' | relative_url }})
- [CV]({{ '/cv/' | relative_url }})

{% assign research_projects = site.projects | sort: 'importance' %}
{% for project in research_projects %}
- [{{ project.title }}]({{ project.url | relative_url }})
{% endfor %}
