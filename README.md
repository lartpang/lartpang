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
* [ICCV 2025 | WaveMamba: Wavelet-Driven Mamba Fusion for RGB-Infrared Object Detection](https://blog.csdn.net/P_LarT/article/details/149816528) - Fri, 01 Aug 2025: <small>*本文提出WaveMamba，一种基于小波变换和Mamba的RGB-红外跨模态目标检测方法。研究发现RGB和红外图像在频域具有互补特性：红外图像低频信息丰富，RGB图像高频细节突出。WaveMamba通过离散小波变换分解特征，采用低频Mamba融合块（结合通道交换和门控注意力）和高频绝对最大值增强策略，实现高效特征融合。在六个基准数据集上的实验表明，该方法平均mAP提升4.5%，同时保持较低计算开销，为跨模态目标检测提供了新思路。*</small>
* [ICCV 2025 | CWNet: Causal Wavelet Network for Low-Light Image Enhancement](https://blog.csdn.net/P_LarT/article/details/149617840) - Thu, 24 Jul 2025: <small>*本文提出一种基于因果推理与小波变换的低光照图像增强方法。CWNet通过因果干预分析揭示潜在因果关系，采用全局度量学习分离因果/非因果因子，并引入实例级CLIP语义损失确保局部一致性。同时设计基于小波变换的主干网络优化频域信息恢复。实验表明，CWNet在多个数据集上优于现有方法，有效解决了光照不均与语义保持的挑战。该方法为低光增强提供了新的因果推理视角，显著提升了视觉质量与语义准确性。*</small>
* [CVPR 2025 | Incomplete Multi-modal Brain Tumor Segmentation via Learnable Sorting State Space Model](https://blog.csdn.net/P_LarT/article/details/149468057) - Sat, 19 Jul 2025: <small>*针对多模态脑肿瘤分割中MRI模态缺失问题，提出了一种基于可学习排序状态空间模型(LS3M)的新方法。该框架通过可微分的动态重排机制(SortP)保留3D MRI的空间结构和语义关联，结合串联状态空间模型(S3M)高效建模长程依赖关系，并采用全局输入策略增强上下文感知。实验表明，在BraTS2018和BraTS2020数据集上，LS3M在模态缺失情况下显著优于现有方法。*</small>
* [ICML 2025 | FourierMamba: Fourier Learning Integration with State Space Models for Image Deraining](https://blog.csdn.net/P_LarT/article/details/149464229) - Sat, 19 Jul 2025: <small>*提出FourierMamba模型，将State Space Models与Fourier学习相结合用于图像去雨。针对现有频域方法忽视频率间依赖关系的问题，模型采用多尺度U-Net架构，核心包含Fourier Spatial Interaction SSM和Fourier Channel Evolution SSM两个模块。前者在空间维度通过改进的zigzag扫描策略（bilateral和progressive两种变体）有序处理频谱信息；后者在通道维度建模频率相关性。*</small>
* [TMI 2025 | Serp-Mamba: Advancing High-Resolution Retinal Vessel Segmentation with Selective SSM](https://blog.csdn.net/P_LarT/article/details/149455039) - Fri, 18 Jul 2025: <small>*提出Serp-Mamba模型，用于高分辨率视网膜血管分割。针对UWF-SLO图像中血管形态特殊、类别失衡等挑战，提出两项创新：1) 蛇形交织自适应扫描机制（SIA），通过可变形路径动态贴合血管曲率，解决传统Mamba固定扫描导致的血管断裂问题；2) 模糊驱动双重校准模块（ADDR），利用双阈值划分和交叉注意力重校准模糊像素，缓解高分辨率下的类别失衡问题。*</small>
* [ArXiv 2507 | RegCL: Continual Adaptation of Segment Anything Model via Model Merging](https://blog.csdn.net/P_LarT/article/details/149428890) - Thu, 17 Jul 2025: <small>*本文提出RegCL方法，通过模型合并实现Segment Anything Model (SAM)在动态多域环境中的持续适配。针对SAM在医学、伪装等特殊领域表现不佳且传统微调导致灾难性遗忘的问题，RegCL创新性地将RegMean模型合并算法引入持续学习场景，仅需保存历史任务的权重内积矩阵，即可在不增加推理参数量的前提下合并新旧知识。实验表明，在五个跨域分割任务上，RegCL的平均准确率达0.751 mIoU，显著优于传统方法，且支持与回放方法结合进一步提升性能。*</small>
* [TGRS 2025 | HTD-Mamba: Efficient Hyperspectral Target Detection with Pyramid State Space Model](https://blog.csdn.net/P_LarT/article/details/149427412) - Thu, 17 Jul 2025: <small>*本文提出HTD-Mamba，一种基于金字塔状态空间模型的高光谱目标检测方法，解决了先验知识有限和光谱变化两大挑战。该方法通过空间编码光谱增强（SESA）生成对比样本对，结合多分辨率特征提取（MSFE）和对比学习机制，有效区分目标与背景。引入Mamba模型捕获长程光谱依赖，以线性复杂度实现高效检测。实验表明，HTD-Mamba在四个数据集上显著优于现有方法（如San Diego I数据集AUC达0.9998），在计算效率和检测精度上均具优势。*</small>
* [CVPR 2025 Oral | DiffFNO: Diffusion Fourier Neural Operator](https://blog.csdn.net/P_LarT/article/details/149415784) - Thu, 17 Jul 2025: <small>*该研究提出DiffFNO框架，通过融合扩散模型与改进的傅里叶神经算子（FNO）解决图像超分辨率问题。实验表明，DiffFNO在多个基准测试中PSNR指标提升2-4dB，且对训练未见尺度具有强泛化能力。*</small>
* [小波变换 | Haar 小波变换](https://blog.csdn.net/P_LarT/article/details/149338853) - Mon, 14 Jul 2025: <small>*本文介绍了Haar小波变换的基本原理及其离散实现方法。*</small>
* [小波变换 | 离散小波变换](https://blog.csdn.net/P_LarT/article/details/149337573) - Mon, 14 Jul 2025: <small>*介绍了离散小波变换（DWT）的核心原理与实现方法。重点阐述了从连续小波变换到DWT的离散化过程，包括尺度参数和平移参数的二进网格采样（a_j=2^j, b_jk=k·2^j），以及时间参数的离散化处理。通过多分辨率分析（MRA）理论，系统性地构建了正交或双正交的小波基函数，引入尺度函数和小波函数两套基函数体系。*</small>
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
