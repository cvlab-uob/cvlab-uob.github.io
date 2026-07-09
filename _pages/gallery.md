---
layout: page
permalink: /gallery/
title: Gallery
description: Photos from our group activities, conference trips, and everyday lab life.
nav: true
navigation_weight: 45
---

<div class="gallery-page">
  {% assign albums = site.gallery | sort: "date" | reverse %}
  {% assign grouped = albums | group_by_exp: "a", "a.date | date: '%Y'" %}
  {% for group in grouped %}
    <h2 class="year">{{ group.name }}</h2>
    <div class="gallery-grid">
      {% for album in group.items %}
        {% include album_card.html album=album %}
      {% endfor %}
    </div>
  {% endfor %}
</div>
