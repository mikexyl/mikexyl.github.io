---
permalink: /coxgraph/
title: "No Nonsense an Easy Lifer"
excerpt: "Coxgraph"
author_profile: true
redirect_from: 
  - /coxgraph/
  - /coxgraph.html
---
# Coxgraph: Multi-robot Collaborative, Globally Consistent, Online Dense Reconstruction System

Motivation:
There exist two major challenges for online multi robot dense reconstruction:

1. to maintain global consistency across all robots
2. high bandwidth requirement for dense map data distribution limited its application in real world.

For the first challenge, to achieve global consistency, we can leverage multi robot visual SLAM frontend to detect loop closure and maintain consistency by extending Voxgraph, a submap-based optimization method for multi robot scenario.
For the communication problem, we propose a concise method to transmit TSDF submaps using meshes as a intermediary data format, and recover it to TSDF in the receiver end.
This method is able to decrease dense map bandwidth to only 10\% of original, with neglectable lost of reconstruction accuracy.

Contribution:

1. We propose an efficient system named *Coxgraph* for centralized multi-robot collaborative dense reconstruction in real-time.
2. We present a compact transmission representation  
which enables transmitting local 3D submaps %which transfer SDF maps with minimal bandwidth requirement.
3. Our system achieves global consistency across robots, by extending online map fusion optimization and loop closure correction methods.

PDF is available [here](./Coxgraph.pdf).

<iframe width="420" height="315"
src="https://www.youtube.com/embed/Anl3F4vFiME">
</iframe>
