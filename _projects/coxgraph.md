---
layout: research
title: "Coxgraph: Multi-robot Collaborative, Globally Consistent, Online Dense Reconstruction System"
short_title: Coxgraph
permalink: /projects/coxgraph/
description: Globally consistent dense mapping across multiple robots, with compact communication of 3D submaps.
img: /images/coxgraph.png
venue: IROS · 2021
authors: Xiangyu Liu, Weicai Ye, Chaoran Tian, Hujun Bao, and Guofeng Zhang
award: Best Paper Award Finalist · Safety, Security, and Rescue Robotics
importance: 3
resources:
  - label: Paper
    url: /projects/coxgraph/Coxgraph.pdf
  - label: Video
    url: https://www.youtube.com/watch?v=Anl3F4vFiME
---

<figure class="project-figure">
  <img src="{{ '/images/coxgraph.png' | relative_url }}" alt="Coxgraph multi-robot dense reconstruction system overview" width="1000" height="600">
</figure>

## Overview

Coxgraph is a system for **real-time, centralized multi-robot collaborative dense reconstruction**. It addresses two challenges: keeping each robot’s map globally consistent and reducing the bandwidth needed to exchange dense 3D data.

The system combines a multi-robot visual SLAM frontend with submap-based optimization, extending Voxgraph to support collaborative mapping. Loop closures and online map fusion correct accumulated drift and align the robots’ reconstructions.

## Compact communication

Instead of transmitting full truncated signed distance function (TSDF) submaps, Coxgraph uses meshes as an intermediate representation. The receiving robot reconstructs the TSDF from the transmitted mesh.

This representation reduces the bandwidth required for dense maps to approximately **10% of the original**, with negligible loss of reconstruction accuracy in the reported experiments.

## Contributions

1. A real-time system for centralized multi-robot collaborative dense reconstruction.
2. A compact representation for transmitting local 3D submaps.
3. Globally consistent mapping through online map fusion optimization and loop closure correction.

## Demonstration

<div class="video-frame">
  <iframe src="https://www.youtube-nocookie.com/embed/Anl3F4vFiME" title="Coxgraph multi-robot dense reconstruction demonstration" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

This work was an **IROS 2021 Best Paper Award Finalist on Safety, Security, and Rescue Robotics in memory of Motohiro Kisoi**.
