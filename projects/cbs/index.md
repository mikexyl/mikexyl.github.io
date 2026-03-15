---
layout: single
title: "Distributed Pose Graph Optimization via Contractive Belief Sharing"
permalink: /projects/cbs/
---

**Xiangyu Liu, Margarita Chli**  
**IEEE Robotics and Automation Letters (RA-L), accepted 2025**

## Overview

Contractive Belief Sharing (CBS) is a distributed pose graph optimization method for multi-robot SLAM. It is built for the setting where each robot should optimize its trajectory collaboratively without handing control to a central coordinator and without paying the heavy communication cost of globally synchronized optimization.

CBS combines two ideas that are usually in tension:

1. MAP-style optimization, which is typically more stable.
2. Belief propagation, which is typically more scalable and communication-efficient.

The result is a hybrid pipeline that keeps computation and communication local to neighboring robots, while improving convergence behavior on loopy and noisy graphs.

<div class="embed-container">
  <iframe
      src="https://www.youtube.com/embed/6oYA7FmQ_0E"
      width="700"
      height="480"
      frameborder="0"
      allowfullscreen="true">
  </iframe>
</div>

<p>
  <img src="/projects/cbs/teaser.png" alt="CBS teaser figure" width="800"/>
</p>

## Problem Setting

Distributed Pose Graph Optimization (DPGO) is a core subproblem in collaborative SLAM. In practice, a useful DPGO solver should:

- remain stable on noisy and loopy real-world graphs,
- use as few communication rounds as possible,
- avoid centralized synchronization bottlenecks,
- and scale as the number of robots grows.

Existing methods usually trade off one side for another. Optimization-based approaches can converge reliably, but they often need many communication rounds. Belief-propagation approaches communicate more efficiently, but can oscillate or diverge when graph structure becomes challenging.

CBS is designed to bridge that gap.

## Core Idea

CBS operates in two stages:

1. **Pose-belief sharing**: robots estimate and exchange Gaussian beliefs over poses that are relevant to neighboring robots.
2. **Anchor-belief sharing**: once pose updates stabilize, robots exchange beliefs over anchor variables to align frames consistently across the full team.

Each robot receives beliefs from neighbors, converts them into local factors in its own graph, runs a local MAP optimization, computes updated marginals, and then applies a damping rule before publishing new beliefs again.

This keeps the protocol fully distributed and neighbor-to-neighbor, while still correcting drift and improving global consistency.

## Why CBS Converges Better

The key mechanism in CBS is a **Hellinger-distance-based damping rule**.

Instead of publishing each new belief update directly, CBS measures how far the update moves relative to the previous belief. It then scales that update so that the Hellinger distance decays in a controlled way between iterations. If an update diverges too aggressively, it is not broadcast immediately.

This produces two practical effects:

- it suppresses oscillatory or divergent belief updates on hard graphs,
- and it preserves the communication pattern and scalability advantages of belief sharing.

The method is also accompanied by a formal convergence analysis in the paper, modeling each robot update as the composition of:

- local optimization,
- local marginalization,
- and belief damping.

Under the stated local conditions, the resulting update map is contractive.

## Algorithm Structure

At a high level, each robot repeats the following loop:

1. Receive pose or anchor beliefs from neighbors.
2. Convert those beliefs into local belief factors tied to the sender's anchor frame.
3. Run local MAP optimization over the robot's own graph.
4. Compute local marginal covariances through Schur-complement-based marginalization.
5. Apply Hellinger damping to the updated beliefs.
6. Publish only the regulated beliefs to neighbors.

During the first stage, the exchanged information focuses on pose beliefs. During the second stage, anchor beliefs propagate across the team so that robots eventually maintain anchor estimates for every other robot, improving consistent global alignment.

## Experimental Results

The paper evaluates CBS against **ASAPP**, **DGS**, and **MESA** on standard DPGO benchmark datasets and additional synthetic multi-robot setups.

Main takeaways:

- CBS reaches high trajectory accuracy while using substantially fewer communication rounds than stronger optimization-heavy baselines.
- Compared with lighter belief-sharing baselines, CBS remains more stable and accurate on noisy datasets.
- A single parameter setting was reported to work across all tested benchmark datasets in the main comparison.
- As the number of robots increases, CBS shows lower normalized communication, optimization, and runtime costs than the compared methods.

### Parameter Sensitivity

The damping parameters `q` and `D_max` control the tradeoff between speed and conservativeness:

- larger `D_max` can reduce communication rounds but may increase final error,
- smaller `q` makes updates more conservative,
- and the best behavior comes from balancing both to preserve contraction without slowing progress too much.

<p>
  <img src="/projects/cbs/cbs_params.png" alt="CBS parameter sensitivity results" width="800"/>
</p>

### Scalability

On synthetic 3D grid-world experiments with increasing robot counts, CBS maintains modest growth in per-robot communication and computation while matching strong final accuracy. This is the main argument for using CBS in larger collaborative SLAM systems where fully centralized optimization becomes harder to justify.

<p>
  <img src="/projects/cbs/cbs_comparison_metrics.png" alt="CBS scalability comparison" width="800"/>
</p>
