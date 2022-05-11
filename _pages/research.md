---
layout: page
permalink: /research/
title: Research
description:
nav: true
navigation_weight: 15
---
            
---
## **Eye Gaze Tracking**


<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/research/gaze.gif" title="Example Submodular Settings" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


**Eye gaze** is an important functional component in various applications, as it
indicates human attentiveness and can thus be used to study their intentions
and understand social interactions. For these reasons, accurately estimating
gaze is an active research topic in computer vision, with applications in affect
analysis, saliency detection and action recognition, to name
a few. Gaze estimation has also been applied in domains other than computer
vision, such as navigation for eye gaze controlled wheelchairs, detection
of non-verbal behaviors of drivers, and inferring the object of interest in
human-robot interactions.

Research Output: [<a href="https://openaccess.thecvf.com/content_ECCV_2018/papers/Tobias_Fischer_RT-GENE_Real-Time_Eye_ECCV_2018_paper.pdf">RT-GENE(ECCV2018)</a>], [<a href="">CVPRW'22</a>]

Researchers: Hengfei and Nora

---
## **Hand and Object Interaction Modeling**

<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/research/HO.jpg" title="Example Submodular Settings" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<!-- <div class="caption">
    Example Submodular Settings
</div> -->

**Estimating the pose and shape of hands and objects** under interaction finds numerous applications including augmented and virtual reality. **Existing approaches for hand and object reconstruction** require explicitly defined physical
constraints and known objects, which limits its application
domains. Our algorithm is agnostic to object models, and it
learns the physical rules governing hand-object interaction.
This requires automatically inferring the shapes and physical interaction of hands and (potentially unknown) objects.
We seek to approach this challenging problem by proposing a collaborative learning strategy where two-branches
of deep networks are learning from each other. Specifically,
we transfer hand mesh information to the object branch
and vice versa for the hand branch. The resulting optimisation (training) problem can be unstable, and we address
this via two strategies: (i) attention-guided graph convolution which helps identify and focus on mutual occlusion
and (ii) unsupervised associative loss which facilitates the
transfer of information between the branches. Experiments
using four widely-used benchmarks show that our framework achieves beyond state-of-the-art accuracy in 3D pose
estimation, as well as recovers dense 3D hand and object
shapes. Each technical component above contributes meaningfully in the ablation study.

Research Output: [<a href="https://arxiv.org/pdf/2204.13062.pdf">CVPR'22</a>], [<a href="https://arxiv.org/abs/2007.05168">SeqHAND(ECCV'22)</a>], [<a href="http://www.iis.ee.ic.ac.uk/~dtang/cvpr_14.pdf">CVPR'14</a>], [<a href="https://hyungjinchang.files.wordpress.com/2015/03/latentregressionforest_tpami.pdf">TPAMI'16</a>]

Researchers: Elden and Zhongqun

---
## **6D Object Pose Estimation**

<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/research/6D.jpg" title="Example Submodular Settings" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

**Fast and accurate tracking of an object’s motion**
is one of the key functionalities of a robotic system for achieving
reliable interaction with the environment. This paper focuses on
the instance-level six-dimensional (6D) pose tracking problem
with a symmetric and textureless object under occlusion. We
propose a Temporally Primed 6D pose tracking framework with
Auto-Encoders (TP-AE) to tackle the pose tracking problem.
The framework consists of a prediction step and a temporally
primed pose estimation step. The prediction step aims to quickly
and efficiently generate a guess on the object’s real-time pose
based on historical information about the target object’s motion.
Once the prior prediction is obtained, the temporally primed
pose estimation step embeds the prior pose into the RGB-D
input, and leverages auto-encoders to reconstruct the target
object with higher quality under occlusion, thus improving the
framework’s performance. Extensive experiments show that the
proposed 6D pose tracking method can accurately estimate the
6D pose of a symmetric and textureless object under occlusion,
and significantly outperforms the state-of-the-art on T-LESS
dataset while running in real-time at 26 FPS.

Research Output: [<a href="http://pure-oai.bham.ac.uk/ws/portalfiles/portal/164770788/_ICRA_TP_AE_6D_Object_Tracking.pdf">TP-AE(ICRA'22)</a>], [<a href="http://openaccess.thecvf.com/content/CVPR2021/papers/Chen_FS-Net_Fast_Shape-Based_Network_for_Category-Level_6D_Object_Pose_Estimation_CVPR_2021_paper.pdf">FS-Net(CVPR'21 Oral)</a>], [<a href="http://openaccess.thecvf.com/content_CVPR_2020/papers/Chen_G2L-Net_Global_to_Local_Network_for_Real-Time_6D_Pose_Estimation_CVPR_2020_paper.pdf">G2L-Net(CVPR'20)</a>], [<a href="http://openaccess.thecvf.com/content_WACV_2020/papers/Chen_PonitPoseNet_Point_Pose_Network_for_Robust_6D_Object_Pose_Estimation_WACV_2020_paper.pdf">PPNet(WACV'20)</a>]

Researchers: Linfang and Wei

---
## **Neural Radiance Field (NeRF)**

<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/research/NeRF.jpg" title="Example Submodular Settings" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Imagine you have a photo of yourself where everything
is perfect except the camera angle. Perhaps the photographer cut off the top of the attraction you were standing in
front of, or you wished the photo had a wider field-of-view.
The best course of action to correct this would be to retake the photo immediately after looking at the outcomes,
but this is not always possible, especially for touristic locations, which are often the photos that you care about a lot.
Moreover, in situations where there is no “second try”, for
example when your baby walks for the first time, a re-take
is not an option.

Research Output: [<a href="https://openaccess.thecvf.com/content/WACV2022/papers/Freer_Novel-View_Synthesis_of_Human_Tourist_Photos_WACV_2022_paper.pdf">WACV'22</a>]

Researchers: Jonathan and Hengfei


## **Visual Object Tracking**

<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/research/tracking.jpg" title="Example Submodular Settings" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Key to realizing the vision of human-centred computing is the ability for machines to recognize people, so that spaces and devices can become truly personalized. However, the unpredictability of real-world environments impacts robust recognition, limiting usability. In real conditions, human identification systems have to handle issues such as out-of-set subjects and domain deviations, where conventional supervised learning approaches for training and inference are poorly suited. With the rapid development of Internet of Things (IoT), we advocate a new labelling method that exploits signals of opportunity hidden in heterogeneous IoT data. The key insight is that **one sensor modality can leverage the signals measured by other co-located sensor modalities to improve its own labelling performance**. If identity associations between heterogeneous sensor data can be discovered, it is possible to automatically label data, leading to more robust human recognition, without manual labelling or enrolment. On the other side of the coin, we also study the privacy implication for such cross-modal identity association.

Research Output: [<a href="https://hyungjinchang.files.wordpress.com/2018/03/cvpr2018-traca-preprint.pdf">CVPR'18</a>], [<a href="https://hyungjinchang.files.wordpress.com/2015/03/attentional-correlation-filter-network-for-adaptive-visual-tracking.pdf">CVPR'17</a>], [<a href="https://hyungjinchang.files.wordpress.com/2015/03/cvpr2016-visualtracking.pdf">CVPR'16</a>], [<a href="">CVPR'13</a>]

Researches: Jinyu and Zhongqun