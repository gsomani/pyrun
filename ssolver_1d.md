---
layout: default
title: 1D Semiconductor solver
repo: gsomani/semiconductor_solver
branch: main
permalink: /ssolver_1d
---

Semiconductor solver solves Poisson's eqaution in 1D to calculate equilibrium potential inside semiconductor. Steady state solution calculation for 1D semiconductor is also implemented.

For more information, visit the [project website](www.gsomani.github.io/semiconductor_solver).

<pre data-executable data-language="python">
{%- include py/params.py -%}
</pre>

<pre data-executable data-language="python">
{%- include py/solver_1d.py -%}
</pre>

<pre data-executable data-language="python">
{%- include py/solver_bias.py -%}
</pre>
