---
layout: page
permalink: /publications/
title: Publications
description: 
years: []
nav: true
navigation_weight: 20
---

Only recent publications are listed here. The full list can be found in my [Google Scholar Link](https://scholar.google.com/citations?user=3TggrEkAAAAJ&hl=en).

<div class="publications">

<!-- <h2 class="year">Journel</h2>
{% bibliography -f papers -q @*[Journel=true]* %} -->

{% assign years = (2002..2026) | reverse %}
{% for y in years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}} && preprint!=true && supplementary!=true]* %}
{% endfor %}

</div>