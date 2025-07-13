# Hi 👋, I'm lartpang

## 🧑‍🤝‍🧑 Me

$$
\textbf{life} = \int_{birth}^{now} \mathbf{happy}(time) + \mathbf{sad}(time) d(time)
$$

<p align="center">
  A Python and PyTorch developer, deep-learning worker and open-source activist.
  <br /><br />

  <img src="https://github.com/lartpang/lartpang/assets/26847524/47e4b857-c6b7-4237-a637-0ec73485e48e" />
  Created by the awesome <a href="https://erikdemaine.org/fonts/tetris/">tool</a>. 😊
</p>

* 📝 I regulary write articles on [https://www.yuque.com/lart](https://www.yuque.com/lart)
* 💬 Ask me about **Python, PyTorch** in [ISSUES](https://github.com/lartpang/lartpang/issues)
* ⚡ Fun fact **I am a boy.**

## 📝 Recent Writing

<!-- writing starts -->
* [NeurIPS 2024 | Can Transformers Smell Like Humans?](https://blog.csdn.net/P_LarT/article/details/149295789) - Sat, 12 Jul 2025: <small>*本文探讨了Transformer模型在无嗅觉标签条件下，能否通过化学结构预训练对齐人类嗅觉感知。研究发现，MoLFormer模型提取的气味剂表征能够有效预测专家标注的嗅觉描述符、人类连续评分及气味剂相似度，其性能接近监督模型且优于传统物理化学特征方法。分析表明，模型深层表征更偏向高层感知特征而非底层化学属性。研究证实了自监督Transformer在嗅觉感知预测中的潜力，为化学与神经科学研究提供了新工具，但受限于数据质量和个体差异等因素，仍有改进空间。*</small>
* [ArXiv 2506 | WaRA: Wavelet Low Rank Adaptation](https://blog.csdn.net/P_LarT/article/details/149216094) - Wed, 09 Jul 2025: <small>*本文提出WaRA(Wavelet Low Rank Adaptation)，一种新型参数高效微调(PEFT)方法，通过将小波变换引入低秩适应过程，有效解决了现有方法在捕捉多尺度结构数据时的不足。WaRA的核心创新点在于： 在小波域进行低秩分解，保留关键结构信息的同时大幅减少参数量 引入跨子带参数共享策略，进一步提升参数效率 采用Haar正交基实现高效的小波变换。实验证明，WaRA在图像生成、分类等视觉任务中显著优于传统LoRA方法，在语言任务中也展现出良好性能。*</small>
* [ArXiv 2501 | From Molecules to Mixtures: Learning Representations of Olfactory Mixture Similarity](https://blog.csdn.net/P_LarT/article/details/149208677) - Tue, 08 Jul 2025: <small>*本文提出POMMIX模型，首次将数字化嗅觉研究从单一分子扩展到复杂混合物。该模型采用层次化架构：基于图神经网络学习分子嵌入，通过自注意力机制聚合混合物表示，并设计对称性评分函数预测相似性。实验表明，POMMIX在低数据量场景下显著优于传统方法，并验证了&quot;嗅觉白噪声&quot;现象。研究为蚊虫驱避剂开发、食品香料设计等应用提供了新思路，并展示了领域知识与深度学习结合在化学感知建模中的潜力。*</small>
* [ArXiv 2507 | SWinMamba: Serpentine Window State Space Model for Vascular Segmentation](https://blog.csdn.net/P_LarT/article/details/149172348) - Mon, 07 Jul 2025: <small>*本文提出了一种新型血管分割模型SWinMamba，通过将蛇形窗口序列融入双向状态空间模型，有效解决了血管几何连续性（VGC）的建模难题。该方法包含三个核心组件：SWToken采用蛇形窗口自适应分割图像，提供灵活感受野；BAM通过双向聚合整合局部特征；SFFU融合空间和频率域特征以构建全面表示。在CHASE-DB1等三个数据集上的实验表明，该方法显著提升了血管分割的完整性和连通性，β0指标平均提升18.17%，同时保持较低计算成本。消融实验验证了各模块的有效性，为临床诊断和手术导航提供了更可靠的血管分割方案。*</small>
* [CVPR 2025 | DefMamba: Deformable Visual State Space Model](https://blog.csdn.net/P_LarT/article/details/149170100) - Mon, 07 Jul 2025: <small>*提出了一种创新的视觉基础模型DefMamba，通过可变形扫描策略动态调整扫描路径，优先捕捉重要信息。该方法将可变形机制首次引入状态空间模型(SSM)，结合深度卷积和可变形分支，设计了包含偏移网络的可变形状态空间模型(DSSM)。实验表明，DefMamba在ImageNet分类、COCO检测/分割和ADE20K语义分割等任务中性能显著优于现有SSM方法，且计算复杂度较低。该研究为SSM在视觉任务中的应用提供了新思路，但处理不完整物体结构时仍存在局限。*</small>
* [Arxiv 2502 | DAMamba: Vision State Space Model with Dynamic Adaptive Scan](https://blog.csdn.net/P_LarT/article/details/149167284) - Mon, 07 Jul 2025: <small>*摘要： 本文提出DAMamba，一种基于动态自适应扫描（DAS）的视觉状态空间模型，解决了传统扫描策略在图像语义邻接性破坏和灵活性不足的问题。DAS通过数据驱动方式动态调整扫描顺序和区域，结合可学习的偏移预测网络优化特征提取。DAMamba整合多尺度层次化结构和卷积增强模块，在ImageNet-1K分类任务中达到83.8%准确率，显著超越现有SSM和ViT模型。在COCO目标检测/分割及ADE20K语义分割任务中，DAMamba分别取得最高50.6 mAP和51.9 mIoU，验证了其作为通用视觉骨干网络的*</small>
* [ICCV 2025 | Achieving More with Less: Additive Prompt Tuning for Rehearsal-Free CIL](https://blog.csdn.net/P_LarT/article/details/149156683) - Sun, 06 Jul 2025: <small>*本文提出了一种新型的类增量学习方法APT（Additive Prompt Tuning），通过创新的提示调优方式解决了现有基于提示的方法计算开销大的问题。APT采用直接修改CLS token注意力计算的方式，而非传统的提示拼接方法，显著降低了计算复杂度。该方法还提出渐进式提示融合（PPF）策略，通过加权平均新旧提示有效减轻灾难性遗忘。实验表明，APT在多个基准测试中性能最优，如ImageNet-R上平均准确率提升5.2%，同时计算量减少41.5%，可训练参数减少78.2%。该方法不仅适用于类增量学习，还展现*</small>
* [生成 | 朗之万动力学与郎之万采样](https://blog.csdn.net/P_LarT/article/details/149140845) - Sat, 05 Jul 2025: <small>*朗之万动力学是描述微观粒子在势能场中受趋势力、摩擦力和随机力共同作用的随机微分方程。该方程揭示了热平衡系统中微观状态的概率分布由能量决定（玻尔兹曼分布）。在过阻尼极限下，方程简化为只含趋势力和随机力的一阶形式，成为郎之万采样的理论基础。郎之万采样利用梯度信息和随机噪声，通过离散化处理（欧拉-丸山方法）实现高效概率采样，特别适用于高维非标准化分布。该方法将物理系统的热平衡原理转化为机器学习中的采样引擎，在生成建模等领域有重要应用。*</small>
* [ArXiv 2101 | Rethinking Interactive Image Segmentation Feature Space Annotation](https://blog.csdn.net/P_LarT/article/details/148924990) - Thu, 26 Jun 2025: <small>*摘要 本文提出了一种创新的交互式图像分割方法，通过在特征空间进行批注操作来同时处理多幅图像。与传统在像素空间进行单幅图像标注的模式不同，该方法将用户交互转移到特征空间，显著减少了标注工作量。实验证明，该方法在前景分割数据集上达到state-of-the-art水平，在Cityscapes语义分割数据集上实现91.5%的准确率，标注效率提升74.75倍。该研究为图像分割标注提供了新思路，可与其他方法结合进一步提升标注效率。*</small>
* [CVPR 2024 | Rethinking Inductive Biases for Surface Normal Estimation](https://blog.csdn.net/P_LarT/article/details/148924871) - Thu, 26 Jun 2025: <small>*这篇论文重新思考了表面法线估计的归纳偏置问题，提出了创新性方法。作者指出现有基于通用密集预测模型的方法存在局限，进而提出三点改进：利用射向每个像素的射线方向作为输入，设计基于射线方向的激活函数，将法线估计重构为相对旋转估计。实验表明，该方法能生成更清晰平滑的预测结果，且在数据量较少时展现更强的泛化能力。该研究为从单RGB图像估计表面法线的任务提供了新思路，对三维重建等计算机视觉应用具有重要意义。*</small>
<!-- writing ends -->

View the archives @ [csdn@p_lart](https://blog.csdn.net/p_lart).

## 📽️ Some Projects

| Name                                                                                         | Stars                                                                               | Description                                                                                                                                                      |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Hands-on-Docker (中文)**](https://github.com/lartpang/Hands-on-Docker)                    | ![stars](https://img.shields.io/github/stars/lartpang/Hands-on-Docker)              | 一份详尽的 Docker 使用指南。                                                                                                                                     |
| [**Awesome-Class-Activation-Map**](https://github.com/lartpang/awesome-class-activation-map) | ![stars](https://img.shields.io/github/stars/lartpang/awesome-class-activation-map) | An awesome list of papers and tools about the class activation map (CAM) technology.                                                                             |
| [**PyTorchTricks**](https://github.com/lartpang/PyTorchTricks)                               | ![stars](https://img.shields.io/github/stars/lartpang/PyTorchTricks)                | Some tricks of pytorch…                                                                                                                                          |
| [**MethodsCmp**](https://github.com/lartpang/MethodsCmp)                                     | ![stars](https://img.shields.io/github/stars/lartpang/MethodsCmp)                   | A Simple Toolkit for Counting the FLOPs/MACs, Parameters and FPS of Pytorch-based Methods.                                                                       |
| [**PySODEvalToolkit**](https://github.com/lartpang/PySODEvalToolkit)                         | ![stars](https://img.shields.io/github/stars/lartpang/PySODEvalToolkit)             | A Python-based salient object detection and video object segmentation evaluation toolbox.                                                                        |
| [**PySODMetrics**](https://github.com/lartpang/PySODMetrics)                                 | ![stars](https://img.shields.io/github/stars/lartpang/PySODMetrics)                 | A simple and efficient implementation of SOD metrcis.                                                                                                            |
| [**PyLoss**](https://github.com/lartpang/PyLoss)                                             | ![stars](https://img.shields.io/github/stars/lartpang/PyLoss)                       | Some loss functions for deeplearning.                                                                                                                            |
| [**OpticalFlowBasedVOS**](https://github.com/lartpang/OpticalFlowBasedVOS)                   | ![stars](https://img.shields.io/github/stars/lartpang/OpticalFlowBasedVOS)          | A simple and efficient codebase for the optical flow based video object segmentation.                                                                            |
| [**CoSaliencyProj**](https://github.com/lartpang/CoSaliencyProj)                             | ![stars](https://img.shields.io/github/stars/lartpang/CoSaliencyProj)               | A project for co-saliency detection. Some codes are borrowed from ICNet. Thanks to ICNet Intra-saliency Correlation Network for Co-Saliency Detection (NIPS2020) |
| [**RunIt**](https://github.com/lartpang/RunIt)                                               | ![stars](https://img.shields.io/github/stars/lartpang/RunIt)                        | A simple program scheduler for your code on different devices.                                                                                                   |
| [**RegisterIt**](https://github.com/lartpang/RegisterIt)                                     | ![stars](https://img.shields.io/github/stars/lartpang/RegisterIt)                   | Register it: A more flexible register for the DeepLearning project.                                                                                              |
| [**mssim.pytorch**](https://github.com/lartpang/mssim.pytorch)                               | ![stars](https://img.shields.io/github/stars/lartpang/mssim.pytorch)                | A better pytorch-based implementation for the mean structural similarity. Differentiable simpler SSIM and MS-SSIM.                                               |
| [**tta.pytorch**](https://github.com/lartpang/tta.pytorch)                                   | ![stars](https://img.shields.io/github/stars/lartpang/tta.pytorch)                  | Test-Time Augmentation library for Pytorch.                                                                                                                      |
| [**YuQueTools**](https://github.com/lartpang/YuQueTools)                                     | ![stars](https://img.shields.io/github/stars/lartpang/YuQueTools)                   | A simple tool to download your own articles from yuque.                                                                                                          |
| [**ManageMyAttachments**](https://github.com/lartpang/ManageMyAttachments)                   | ![stars](https://img.shields.io/github/stars/lartpang/ManageMyAttachments)          | Manage the attachments of your own obsidian vault.                                                                                                               |
