---
layout: default
title: DEVSIM TCAD Semiconductor Device Simulator 
repo: gsomani/devsim
branch: binder
permalink: /devsim
---

DEVSIM is an open source semiconductor device simulation software using the finite volume method to solve partial differential equations on a mesh. The solver is accessed using the python API. For more information, visit the [official website](https://devsim.org/).

Below is the example showing 2D capacitor simulation. The source of the example is examples folder in [devsim github repository](https://github.com/devsim/devsim). 

<pre data-executable data-language="python">
{%- include py/cap2d.py -%}
</pre>
