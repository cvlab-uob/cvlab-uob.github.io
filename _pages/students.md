---
layout: page
permalink: /team/
title: Team
description: 
nav: true
navigation_weight: 20
---

<style>
    .team-cards .row {
        margin-bottom: 0.8rem;
    }

    .team-cards p {
        margin: 0 0 0.2rem;
    }

    .team-cards .col-sm-6.clearfix {
        padding-right: 1.4rem;
        min-height: 228px;
    }

    .team-cards img.img-responsive {
        width: 170px;
        height: 170px;
        object-fit: cover;
        border-radius: 50%;
        float: left;
        margin-right: 1rem;
        margin-top: 0.1rem;
        border: 2px solid rgba(255, 255, 255, 0.96);
        box-shadow:
            0 14px 24px rgba(0, 0, 0, 0.18),
            0 6px 10px rgba(0, 0, 0, 0.12),
            inset 0 1px 0 rgba(255, 255, 255, 0.45);
        transform: perspective(900px) translateZ(0);
        transition: transform 0.22s ease, box-shadow 0.22s ease;
    }

    .team-cards img.img-responsive:hover {
        transform: perspective(900px) translateY(-3px) scale(1.02);
        box-shadow:
            0 20px 30px rgba(0, 0, 0, 0.22),
            0 9px 14px rgba(0, 0, 0, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.5);
    }

    .team-cards h4 {
        margin: 0 0 0.3rem;
        font-size: 1.25rem;
        font-weight: 700;
        line-height: 1.2;
        letter-spacing: 0.01em;
    }

    .team-cards i {
        display: block;
        font-style: normal;
        line-height: 1.5;
        margin-bottom: 0.35rem;
        color: #4a4a4a;
    }

    .team-cards .research-topics {
        margin: 0.35rem 0 0;
        padding-left: 1.1rem;
        line-height: 1.5;
    }

    .team-cards .research-topics li {
        margin-bottom: 0.18rem;
    }

    @media (max-width: 767px) {
        .team-cards .col-sm-6.clearfix {
            min-height: 0;
            margin-bottom: 1.3rem;
            padding-right: 0;
        }

        .team-cards .row {
            margin-bottom: 0.2rem;
        }

        .team-cards img.img-responsive {
            width: 136px;
            height: 136px;
            margin-right: 0.9rem;
        }

        .team-cards h4 {
            font-size: 1.14rem;
        }
    }

    .table td, .table th {
        padding: 0.25rem 0.5rem;
        line-height: 0.1;
    }
</style>

<section class="team-cards">
    <div class="row">
        <div class="col-sm-6 clearfix">
            <img src="/assets/img/team/Hyung%20Jin%20Chang.png" class="img-responsive" width="40%" style="float: left;">
            <h4><a href="/">
                <b>Hyung Jin Chang</b>
            </a></h4>
            <i>
            <b>Associate Professor</b><br>
            <a href="mailto:h.j.chang@bham.ac.uk" class="email" data-addr="KKaaqpMwICWe8TAlMLI=">Email</a><br>
            </i>
            <ul class="research-topics" style="overflow: hidden">
            <li>Director of HCVL</li>
            </ul>
        </div>
        <div class="col-sm-6 clearfix">
            <img src="https://www.yihua.zone/images/yihua.png" class="img-responsive" width="40%" style="float: left">
            <h4><a href="https://www.yihua.zone/">
                <b>Yihua Cheng</b>
            </a></h4>
            <i>
            <b>Postdoctoral Fellow</b><br>
            <a href="https://www.yihua.zone/">Homepage</a> | <a href="mailto:y.cheng.2@bham.ac.uk" class="email" data-addr="KKaaqpMwICWe8TAlMLI=">Email</a><br>
            </i>
            <ul class="research-topics" style="overflow: hidden">
            <li>Computer Vision and Human-Computer Interaction</li>
            <li>Gaze Research</li>
            </ul>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-6 clearfix">
            <img src="/assets/img/team/Esha.jpg" class="img-responsive" width="40%" style="float: left">
            <h4><a href="https://eshadasgupta.github.io/portfolio/">
                <b>Esha Dasgupta</b>
            </a></h4>
            <i>
            <b>PhD Student</b><br>
            <a href="https://eshadasgupta.github.io/portfolio/">Homepage</a> | <a href="mailto:exd949@student.bham.ac.uk" class="email" data-addr="KKaaqpMwICWe8TAlMLI=">Email</a><br>
            </i>
            <ul class="research-topics" style="overflow: hidden">
            <li>3D Human Posture Estimation</li>
            <li>Musculoskeletal Regression</li>
            </ul>
        </div>
        <div class="col-sm-6 clearfix">
            <img src="/assets/img/team/Jonathan.jpg" class="img-responsive" width="40%" style="float: left">
            <h4><a href="/team/jonathan">
                <b>Jonathan Freer</b>
            </a></h4>
            <i>
            <b>PhD Student</b><br>
            <a href="mailto:jxf782@student.bham.ac.uk" class="email" data-addr="KKaaqpMwICWe8TAlMLI=">Email</a><br>
            </i>
            <ul class="research-topics" style="overflow: hidden">
            <li>Novel View Synthesis</li>
            <li>NeRF</li>
            </ul>
        </div>
    </div>
    <p></p>
    <div class="row">
        <div class="col-sm-6 clearfix">
            <img src="/assets/img/team/Yuqi.jpg" class="img-responsive" width="40%" style="float: left">
            <h4><a href="/team/yuqi">
                <b>Yuqi Hou</b>
            </a></h4>
            <i>
            <b>PhD Student</b><br>
            <a href="mailto:JXF782@student.bham.ac.uk" class="email" data-addr="KKaaqpMwICWe8TAlMLI=">Email</a><br>
            </i>
            <ul class="research-topics" style="overflow: hidden">
            <li>Eye Gaze Tracking</li>
            <li>Deep Learning</li>
            </ul>
        </div>
        <div class="col-sm-6 clearfix">
            <img src="/assets/img/team/Zhuo.jpg" class="img-responsive" width="40%" style="float: left">
            <h4><a href="https://chzh9311.github.io">
                <b>Zhuo Chen</b>
            </a></h4>
            <i>
            <b>PhD Student</b><br>
            <a href="https://chzh9311.github.io">Homepage</a> | <a href="mailto:zxc417@student.bham.ac.uk" class="email" data-addr="KKaaqpMwICWe8TAlMLI=">Email</a><br>
            </i>
            <ul class="research-topics" style="overflow: hidden">
            <li>Hand-Object Interaction</li>
            <li>3D Contact Modeling for Grasp Generation</li>
            </ul>
        </div>
    </div>
    <p></p>
    <div class="row">
        <div class="col-sm-6 clearfix">
            <img src="/assets/img/team/Shijing.jpg" class="img-responsive" width="40%" style="float: left">
            <h4><a href="/publications/">
                <b>Shijing Wang</b>
            </a></h4>
            <i>
            <b>PhD Student</b><br>
            <a href="mailto:sxw1350@student.bham.ac.uk" class="email" data-addr="KKaaqpMwICWe8TAlMLI=">Email</a><br>
            </i>
            <ul class="research-topics" style="overflow: hidden">
            <li>Gaze Following</li>
            <li>Vision-Language Models</li>
            </ul>
        </div>
    </div>
</section>

---

<section>
  <h4> <strong>Co-supervising PhD Students</strong></h4>
  <ul>
        <li>
            <a href=""  target="_blank"><strong>Oluwatofunmi Akintaro</strong></a>. (Co-supervision with Dr. Jianbo Jiao)
        </li>
        <li>
            <a href=""  target="_blank"><strong>Han Hu</strong></a>. (Co-supervision with Dr. Jianbo Jiao)
        </li>
        <li>
            <a href=""  target="_blank"><strong>Alexandru Popa</strong></a>. (Co-supervision with Dr. Shan He)
        </li>
        <li>
            <a href=""  target="_blank"><strong>Anselmo Parnada</strong></a>. (Co-supervision with Dr. Yongjing Wang)
        </li>
  </ul>
</section>

---

<section>
  <h4> <strong>Current Visiting Researchers</strong></h4>
  <ul>
        <li>
            <a href=""  target="_blank"><strong>Prof. Wonpyo Lee</strong></a>, (sabbatical visit from Joseon University, South Korea).
        </li>
        <li>
            <a href=""  target="_blank"><strong>Ms. Hana Lee</strong></a>, (from the Korean Government).
        </li>
        <li>
            <a href=""  target="_blank"><strong>Mr. ByeongMin Tae</strong></a>, (from the Korean Government).
        </li>
        <li>
            <a href=""  target="_blank"><strong>Mr. Jihoon Lim</strong></a>, (from Seoul Economics).
        </li>
  </ul>
</section>

---

<style>
    .alumni-list h5 {
        margin-top: 1.4rem;
        margin-bottom: 0.6rem;
    }
    .alumni-list ul {
        list-style: none;
        padding-left: 0;
        margin-bottom: 0.6rem;
    }
    .alumni-list ul li {
        padding: 0.15rem 0;
        line-height: 1.55;
    }
    .alumni-list ul li::before {
        content: "• ";
        margin-right: 0.35rem;
        color: #888;
    }
</style>

<section class="alumni-list">
  <h4><strong>Alumni</strong></h4>

  <h5><strong>Post-doctoral Fellows</strong></h5>
  <ul>
    <li>Bo Eun Kim (04/2024 - 02/2025, now Assistant Professor, Dankook University, South Korea)</li>
    <li><a href="https://gaoyixing.wordpress.com/" target="_blank">Yixing Gao</a> (09/2020 - 09/2021, now Associate Professor, Jilin University, China)</li>    
  </ul>

  <h5><strong>PhD Students</strong></h5>
  <ul>
    <li><a href="https://hengfei-wang.github.io/" target="_blank">Hengfei Wang</a> (09/2020 - 05/2025, now PostDoc researcher, EPFL, Switzerland)</li>
    <li><a href="https://zhongqunzhang.github.io/" target="_blank">Zhongqun Zhang</a> (04/2021 - 06/2025, now Assistant Professor, Nankai University, China)</li>
    <li><a href="https://lynne-zheng-linfang.github.io/" target="_blank">Linfang Zheng</a> (01/2020 - 10/2024, now PostDoc researcher, University of Hong Kong, China)</li>
    <li><a href="https://eldentse.github.io" target="_blank">Tze Ho Elden Tse</a> (02/2020 - 06/2024, now PostDoc researcher, NUS, Singapore)</li>
    <li>Nora Horanyi (10/2018 - 05/2023, now Senior Machine Learning Specialist, JBA Risk Management, UK)</li>
  </ul>

  <h5><strong>Visiting PhD Students</strong></h5>
  <ul>
    <li>Jeongho Lee (02/2025 - 08/2025, now Dankook University, South Korea)</li>
    <li><a href="https://sites.google.com/view/sunghochun/home" target="_blank">Sungho Chun</a> (12/2024 - 03/2025, now Kwangwoon University, South Korea)</li>
    <li>YoungChan Choi (09/2024 - 02/2025, now Dankook University, South Korea)</li>
    <li>Jung Hoon Sung (09/2024 - 02/2025, now Dankook University, South Korea)</li>
    <li><a href="https://uyoung-jeong.github.io/" target="_blank">Uyoung Jeong</a> (09/2024 - 12/2024, now PhD Student, UNIST, South Korea)</li>
    <li>Jongsu Youn (10/2024 - 11/2024, now PhD Student, Chung-Ang University, South Korea)</li>
    <li>SeungMo Seo (10/2024 - 11/2024, now PhD Student, Chung-Ang University, South Korea)</li>
    <li>Jeonghan Lee (07/2024 - 08/2024)</li>
    <li>Jaemin Na (10/2021 - 03/2022, now Senior Research Engineer, Vision AI Research Department, KT AI2X Lab)</li>
    <li>Taehoon Kim (10/2021 - 03/2022, now Ajou University, South Korea)</li>
    <li>John Yang (09/2019 - 12/2019, now Software Engineer, NVIDIA, USA)</li>
  </ul>

  <h5><strong>Visiting Researchers & Sabbatical Visitors</strong></h5>
  <ul>
    <li>Hopyeong Hwang (12/2024 - 11/2025, now Korea Disease Control and Prevention Agency, South Korea)</li>
    <li>Woochul Kim (08/2023 - 08/2025, now Ministry of Science and ICT, South Korea)</li>
    <li><a href="https://sites.google.com/site/juyongchang/" target="_blank">Ju Yong Chang</a> (03/2024 - 02/2025, now Professor, Kwangwoon University, South Korea)</li>
    <li><a href="https://sites.google.com/view/visual-ai/professor" target="_blank">Jungchan Cho</a> (01/2024 - 01/2025, now Professor, Gachon University, South Korea)</li>
    <li>Jiyoung Yoon (01/2024 - 12/2024, now Senior Research Fellow, Busan Development Institute, South Korea)</li>
    <li>SeungJu You (09/2023 - 09/2024, now Director, Human Resource Development Division, Ministry of Personnel Management, South Korea)</li>
    <li><a href="https://sites.google.com/site/bsrvision00/" target="_blank">Seungryul Baek</a> (07/2024 - 08/2024, now Associate Professor, UNIST, South Korea)</li>
    <li>Bongkeun Choi (09/2022 - 08/2023, now Director, Ministry of Health and Welfare (MOHW), South Korea)</li>
    <li>Yongsoo Baek (02/2022 - 02/2023, now Professor, Inha University Hospital, South Korea)</li>
    <li>Daeun Sung (12/2021 - 06/2022, now Assistant Director, General Services and Personnel Division, Ministry of Trade, Industry and Energy, South Korea)</li>
    <li>Jinwook Kim (02/2021 - 02/2022, now Professor, Chung-Ang University, South Korea)</li>
    <li>HyunChul Sim (07/2019 - 06/2020, now Director, Hyundai Motors, South Korea)</li>
  </ul>

  <h5><strong>Visiting MSc Students</strong></h5>
  <ul>
    <li><a href="https://zihos.github.io/" target="_blank">Jiho Park</a> (09/2022 - 12/2022, now PhD Student, Dongguk University, South Korea)</li>
    <li>Sanghun Kim (09/2022 - 12/2022)</li>
  </ul>  

  <h5><strong>Research Assistants & Teaching Fellows</strong></h5>
  <ul>
    <li>Xuecheng Qi (09/2021 - 02/2022)</li>
    <li>Daniel Varnai (01/2019 - 12/2020)</li>
    <li>Yuming Chen (Research Assistant)</li>
  </ul>
</section>
