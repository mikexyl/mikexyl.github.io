---
layout: about
title: about
permalink: /
description: Robotics, collaborative SLAM, and multi-robot systems.
subtitle: Robotics Engineer / Student / Researcher
profile:
  align: right
  image: profile.png
  image_circular: true
social: false
selected_papers: false
redirect_from:
  - /about/
  - /about.html
---

<div class="intro-links">
  <a class="action-link" href="{{ site.cv_url }}">CV <span aria-hidden="true">↗</span></a>
  <a class="action-link" href="https://github.com/{{ site.github_username }}">GitHub <span aria-hidden="true">↗</span></a>
  <a class="action-link" href="mailto:{{ site.email }}">Email <span aria-hidden="true">↗</span></a>
</div>

<section class="research-section" aria-labelledby="projects-heading">
  <div class="section-heading">
    <div>
      <h2 id="projects-heading">Projects</h2>
    </div>
    <a class="text-link" href="{{ '/publications/' | relative_url }}">Publications <span aria-hidden="true">↗</span></a>
  </div>
  {% include research_cards.liquid %}
</section>
