# Human-Centred Visual Learning Group Website

This is the website of our academic research group at the University of Birmingham.

A simple, clean, and responsive [Jekyll](https://jekyllrb.com/) theme for academics.
If you like the theme, give it a star!
## Getting started

For more about how to use Jekyll, check out [this tutorial](https://www.taniarascia.com/make-a-static-website-with-jekyll/).

### Step 1. Open with GitHub Desktop
If you want to change the content, please following:
1. Fork our github Repo.
2. Open code with GitHub Desktop. Please use the master branch.
3. Make any changes to your webpage, commit, and push.
4. Wait for a few minutes and let the action complete. You can see the progress in the Actions tab. If completed successfully, in addition to the `master` branch, your repository should also autonomously deploy the `gh-pages` branch.
5. Finally, make a pull requests. The webpage will become available at https://cvlab-uob.github.io/.

### Step 2. Local setup
If you want to pre-view the website when you edit it on your local computer, please following:

#### 1. Install Jekyll
Assuming you have [Ruby](https://www.ruby-lang.org/en/downloads/) and [Bundler](https://bundler.io/) installed on your system (*hint: for ease of managing ruby gems, consider using [rbenv](https://github.com/rbenv/rbenv)*). For Ubuntu/MacOS,

```bash
$ sudo apt install ruby-full ruby-bundler
$ sudo gem install bundler jekyll
$ jekyll -v
```
#### 2. View your website on your local computer

```bash
$ cd <your-repo-name>
$ bundle install
$ bundle exec jekyll serve
# => Now browse to http://localhost:4000
```
Now, feel free to edit the content.
After you are done, **commit** your final changes.

### Step 3. Features (for HJ)

1. To change the About page in _config.yml and _pages/about.md
2. To add the news in _news/xxx.md. ***Please note that each added News should be created in a new Markdown file.***
3. To change the Research page in _pages/research.md. Images are in assets/img/research.
4. To change the Team page in the _pages/student.md. Same as Openings, Teaching and Contact pages.
5. Your publications page is generated automatically from your BibTex bibliography.
Simply edit `_bibliography/papers.bib`. Following:
```bash
@inproceedings{tse2022collaborative,
  title={Collaborative Learning for Hand and Object Reconstruction with Attention-guided Graph Convolution},
  author={Tze Ho Elden Tse and Kwang In Kim and Ales Leonardis and Hyung Jin Chang},
  year={2022},
  booktitle={IEEE Computer Vision and Pattern Recognition (CVPR)},
  arxiv={2204.13062},
  video = {},
  code = {},
  website = {},
  abbr = {CVPR'22},
  img= {/assets/img/paper/EldenCVPR22.jpg},
  selected = {true}
}
```
### Step 4. Personal Page (for Group Members)
If you want to have your own personal academic page, we also provide a template for you.

1. Repeat Step 1 and Setp 2.
2. We prepare a template in _pages/personal_page/template.md
3. Copy template.md and rename it as <your_name>.md and following:
```bash
---
layout: default
permalink: /team/<your_name>
title: <your_name>
---
```
4. Commit, push, and pull request. Your personal page will become available at https://cvlab-uob.github.io/team/your_name.