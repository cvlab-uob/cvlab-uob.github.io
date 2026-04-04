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
</style>

<section class="team-cards">
    <div class="row">
        <div class="col-sm-6 clearfix">
            <img src="/assets/img/team/HJ.png" class="img-responsive" width="40%" style="float: left;">
            <h4><a href="/">
                <b>Hyung Jin Chang</b>
            </a></h4>
            <i>
            <b>Associate Professor</b><br>
            <a href="mailto:H.J.Chang@bham.ac.uk" class="email" data-addr="KKaaqpMwICWe8TAlMLI=">Email</a><br>
            </i>
            <ul class="research-topics" style="overflow: hidden">
            <li>Computer Vision</li>
            <li>Robotics</li>
            </ul>
        </div>
        <div class="col-sm-6 clearfix">
            <img src="https://www.yihua.zone/images/yihua.png" class="img-responsive" width="40%" style="float: left">
            <h4><a href="https://www.yihua.zone/">
                <b>Yihua Cheng</b>
            </a></h4>
            <i>
            <b>Postdoctoral Fellow</b><br>
            <a href="https://www.yihua.zone/">Homepage</a><br>
            </i>
            <ul class="research-topics" style="overflow: hidden">
            <li>Computer Vision and Human-Computer Interaction</li>
            <li>Autonomous Driving</li>
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
            <a href="mailto:EXD949@student.bham.ac.uk" class="email" data-addr="KKaaqpMwICWe8TAlMLI=">Email</a><br>
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
            <a href="mailto:JXF782@student.bham.ac.uk" class="email" data-addr="KKaaqpMwICWe8TAlMLI=">Email</a><br>
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
            <img src="/assets/img/team/Zhuo.png" class="img-responsive" width="40%" style="float: left">
            <h4><a href="/publications/">
                <b>Zhuo Chen</b>
            </a></h4>
            <i>
            <b>PhD Student</b><br>
            <span>Email</span><br>
            </i>
            <ul class="research-topics" style="overflow: hidden">
            <li>RGB-Infrared Image Fusion and Segmentation</li>
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
            <span>Email</span><br>
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
            <a href="https://scholar.google.com/citations?hl=en&user=Wv68qZwAAAAJ"  target="_blank"><strong>Wei Chen</strong></a>. (Co-supervising with Prof. Ales Leonardis)
        </li>
        <li>
            <a href=""  target="_blank"><strong>Haiyang Chen</strong></a>. (Co-supervising with Prof. Andrew Howes)
        </li>
        <li>
            <a href=""  target="_blank"><strong>Dalal Khalid F Aljasem </strong></a>. (Co-supervising with Prof. Andrew Howes)
        </li>
        <li>
            <a href=""  target="_blank"><strong>Emma Maria Rengers</strong></a>. (Co-supervising with Prof. Karen Yeung)
        </li>
        <li>
            <a href="https://scholar.google.com/citations?hl=en&user=iq5N7JgAAAAJ"  target="_blank"><strong>Jinyu Yang</strong></a>. (Co-supervising with Prof. Ales Leonardis)
        </li>
  </ul>
</section>

---

<section>
  <h4> <strong>Visiting Academics</strong></h4>
  <ul>
        <li>
            <a href="https://scholar.google.com/citations?hl=en&user=SXxvdboAAAAJ"  target="_blank"><strong>Jaemin Na</strong></a>, (from Ajou University, South Korea).
        </li>
  </ul>
</section>

---

<section>
  <h4><strong>Alumni</strong></h4>
    <div class="table-responsive">
        <table class="table" style="white-space: nowrap;">
            <colgroup>
                <col style="width: 18%;">
                <col style="width: 22%;">
                <col style="width: 16%;">
                <col style="width: 44%;">
            </colgroup>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Role</th>
                    <th>Period</th>
                    <th>Current Position</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Hengfei Wang</strong></td>
                    <td>PhD Student & PostDoc</td>
                    <td>09/2020 - 05/2025</td>
                    <td>PostDoc researcher, EPFL, Switzerland</td>
                </tr>
                <tr>
                    <td><strong>Jeongho Lee</strong></td>
                    <td>PhD Student (Visiting)</td>
                    <td>02/2025 - 08/2025</td>
                    <td>DanKook University, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Sungho Chun</strong></td>
                    <td>PhD Student (Visiting)</td>
                    <td>12/2024 - 03/2025</td>
                    <td>KwangWoon University, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Hopyeong Hwang</strong></td>
                    <td>Visiting Researcher (Visiting)</td>
                    <td>12/2024 - 11/2025</td>
                    <td>Korea Disease Control and Prevention Agency, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Jongsu Youn</strong></td>
                    <td>PhD Student (Visiting)</td>
                    <td>10/2024 - 11/2024</td>
                    <td>PhD Student, Chung-Ang University, South Korea</td>
                </tr>
                <tr>
                    <td><strong>SeungMo Seo</strong></td>
                    <td>PhD Student (Visiting)</td>
                    <td>10/2024 - 11/2024</td>
                    <td>PhD Student, Chung-Ang University, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Uyoung Jeong</strong></td>
                    <td>PhD Student (Visiting)</td>
                    <td>09/2024 - 12/2024</td>
                    <td>PhD Student, UNIST, South Korea</td>
                </tr>
                <tr>
                    <td><strong>YoungChan Choi</strong></td>
                    <td>PhD Student (Visiting)</td>
                    <td>09/2024 - 02/2025</td>
                    <td>DanKook University, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Jung Hoon Sung</strong></td>
                    <td>PhD Student (Visiting)</td>
                    <td>09/2024 - 02/2025</td>
                    <td>DanKook University, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Seungryul Baek</strong></td>
                    <td>Research visit</td>
                    <td>07/2024 - 08/2024</td>
                    <td>Associate Professor, UNIST, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Jeonghan Lee</strong></td>
                    <td>PhD Student (Visiting)</td>
                    <td>07/2024 - 08/2024</td>
                    <td></td>
                </tr>
                <tr>
                    <td><strong>Bo Eun Kim</strong></td>
                    <td>Postdoc (Visiting Researcher funded by KETI)</td>
                    <td>04/2024 - 02/2025</td>
                    <td>Assistant Professor, Dankook University, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Ju Yong Chang</strong></td>
                    <td>Sabbatical visit</td>
                    <td>03/2024 - 02/2025</td>
                    <td>Professor, Kwangwoon University, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Jungchan Cho</strong></td>
                    <td>Sabbatical visit</td>
                    <td>01/2024 - 01/2025</td>
                    <td></td>
                </tr>
                <tr>
                    <td><strong>Jiyoung Yoon</strong></td>
                    <td>Visiting Researcher</td>
                    <td>01/2024 - 12/2024</td>
                    <td>Senior Research Fellow, Busan Development Institute, South Korea</td>
                </tr>
                <tr>
                    <td><strong>SeungJu You</strong></td>
                    <td>Visiting Researcher</td>
                    <td>09/2023 - 09/2024</td>
                    <td>Director, Human Resource Development Division, Ministry of Personnel Management, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Woochul Kim</strong></td>
                    <td>Visiting Researcher (Visiting)</td>
                    <td>08/2023 - 08/2025</td>
                    <td>Ministry of Science and ICT, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Jiho Park</strong></td>
                    <td>MSc Student (Visiting)</td>
                    <td>09/2022 - 12/2022</td>
                    <td>PhD Student, Dongguk University, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Bongkeun Choi</strong></td>
                    <td>Visiting Researcher</td>
                    <td>09/2022 - 08/2023</td>
                    <td>Director, Ministry of Health and Welfare (MOHW), South Korea</td>
                </tr>
                <tr>
                    <td><strong>Sanghun Kim</strong></td>
                    <td>MSc Student (Visiting)</td>
                    <td>09/2022 - 12/2022</td>
                    <td></td>
                </tr>
                <tr>
                    <td><strong>Yongsoo Baek</strong></td>
                    <td>Sabbatical visit</td>
                    <td>02/2022 - 02/2023</td>
                    <td>Professor, Inha University Hospital, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Daeun Sung</strong></td>
                    <td>Visiting Researcher</td>
                    <td>12/2021 - 06/2022</td>
                    <td>Assistant Director, General Services and Personnel Division, Ministry of Trade, Industry and Energy, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Jaemin Na</strong></td>
                    <td>PhD Student (Visiting)</td>
                    <td>10/2021 - 03/2022</td>
                    <td>Senior Research Engineer, Vision AI Research Department, KT AI2X Lab</td>
                </tr>
                <tr>
                    <td><strong>Taehoon Kim</strong></td>
                    <td>PhD Student (Visiting)</td>
                    <td>10/2021 - 03/2022</td>
                    <td>Ajou University, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Xuecheng Qi</strong></td>
                    <td>Research Assistant</td>
                    <td>09/2021 - 02/2022</td>
                    <td>HUAWEI</td>
                </tr>
                <tr>
                    <td><strong>Zhongqun Zhang</strong></td>
                    <td>PhD Student</td>
                    <td>04/2021 - 06/2025</td>
                    <td>Assistant Professor, Nankai University, China</td>
                </tr>
                <tr>
                    <td><strong>Jinwook Kim</strong></td>
                    <td>Sabbatical visit</td>
                    <td>02/2021 - 02/2022</td>
                    <td>Professor, Chung-Ang University, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Tze Ho Elden Tse</strong></td>
                    <td>PhD Student</td>
                    <td>02/2020 - 06/2024</td>
                    <td>PostDoc researcher, NUS, Singapore</td>
                </tr>
                <tr>
                    <td><strong>Linfang Zheng</strong></td>
                    <td>PhD Student</td>
                    <td>01/2020 - 10/2024</td>
                    <td>PostDoc researcher, University of Hong Kong, China</td>
                </tr>
                <tr>
                    <td><strong>John Yang</strong></td>
                    <td>PhD Student (Visiting)</td>
                    <td>09/2019 - 12/2019</td>
                    <td>Software Engineer, NVIDIA, USA</td>
                </tr>
                <tr>
                    <td><strong>HyunChul Sim</strong></td>
                    <td>Visiting Researcher</td>
                    <td>07/2019 - 06/2020</td>
                    <td>Director, Hyundai Motors, South Korea</td>
                </tr>
                <tr>
                    <td><strong>Daniel Varnai</strong></td>
                    <td>Research Assistant</td>
                    <td>01/2019 - 12/2020</td>
                    <td></td>
                </tr>
                <tr>
                    <td><strong>Nora Horanyi</strong></td>
                    <td>PhD Student</td>
                    <td>10/2018 - 05/2023</td>
                    <td>Senior Machine Learning Specialist, JBA Risk Management, UK</td>
                </tr>
                <tr>
                    <td><strong>Yixing Gao</strong></td>
                    <td>Teaching Fellow</td>
                    <td></td>
                    <td>Associate Professor, Jilin University, China</td>
                </tr>
                <tr>
                    <td><strong>Yuming Chen</strong></td>
                    <td>Research Assistant</td>
                    <td></td>
                    <td></td>
                </tr>
            </tbody>
        </table>
    </div>
</section>
