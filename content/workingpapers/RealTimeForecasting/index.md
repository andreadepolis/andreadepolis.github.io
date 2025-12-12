---
title: "Tracking weekly activity using new data sources"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Galvao
- Petrella
weight: 4
# Author notes (optional)
#author_notes:
#- "Equal contribution"
#- "Equal contribution"

date: "2023-01-01"
publishDate: "2023-01-01T00:00:00Z"
doi: ""
# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]
# Publication name and optional abbreviated publication name.
#publication: In *Wowchemy Conference*
#publication_short: In *ICW*

abstract:
# Summary. An optional shortened abstract. Add for example "in the media"
summary: with <a href="https://sites.google.com/site/anabgalvao/" target="_blank" rel="noopener noreferrer">Ana Galvāo</a> (Bloomber LP) and <a href="https://sites.google.com/a/ivanpetrella.com/www/" target="_blank" rel="noopener noreferrer">Ivan Petrella</a> (Collegio Carlo Alberto).

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
links:
- icon_pack: fas
  icon: file
  name: Working Paper
  url: ""

url_pdf: ""
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ""
  placement: 1
  focal_point: "Smart"
  preview_only: true

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
#projects:
#- example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
#slides: example

share: false  # Show social sharing links?
profile: false
---
Policymakers increasingly rely on real-time measures of economic activity to inform decisions, yet official statistics are typically available only with substantial delay. This paper develops a methodology to extract information from high-frequency indicators in order to produce weekly estimates of official monthly statistics in real time.

Building on real-time tracking and nowcasting models, our approach addresses two challenges inherent in alternative indicators: the absence of seasonal adjustment and the prevalence of outliers. We incorporate seasonal components directly into the model, allowing the seasonal structure of low-frequency data to inform high frequency proxies, and employ fat-tailed distributions to mitigate the influence of large, infrequent shocks. Applying our methodology to UK data, we track retail sales, monthly GDP, and vacancies using proxies such as debit card spending (Revolut) and online job advertisements.

Our results show that weekly estimates improve real-time prediction of official releases and highlight the usefulness of high-frequency alternative data.
