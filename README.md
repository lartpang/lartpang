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
* [ICCV 2025 | Reverse Convolution and Its Applications to Image Restoration](https://blog.csdn.net/P_LarT/article/details/150469410) - Sun, 17 Aug 2025: <small>*本文提出了一种新颖的深度可分离反向卷积算子（reverse convolution），通过建立并求解正则化最小二乘优化问题，实现了对depthwise卷积的有效反转。该算子采用FFT推导闭式解，并详细研究了核初始化、padding策略等实现细节。基于此构建的reverse卷积块结合了层归一化、1×1卷积和GELU激活，形成类Transformer结构，可直接替换现有网络中的常规卷积层，构建ConverseNet。*</small>
* [TCSVT 2023 | StructToken - Rethinking Semantic Segmentation with Structural Prior](https://blog.csdn.net/P_LarT/article/details/150464275) - Sun, 17 Aug 2025: <small>*一种新的语义分割范式，通过结构化token直接构建语义掩码并逐步细化，而非传统逐像素分类方法。作者设计了三种交互结构（CSE、SSE和静态卷积）来捕获特征图中的结构信息，并通过堆叠处理单元实现mask细化。*</small>
* [torchvision 中 deform_conv2d 操作的经验性解析](https://blog.csdn.net/P_LarT/article/details/150463945) - Sun, 17 Aug 2025: <small>*详细解析了torchvision中可变形卷积(deform_conv2d)的实现原理和使用方法。*</small>
* [一次由默认参数引起的思考](https://blog.csdn.net/P_LarT/article/details/150463724) - Sun, 17 Aug 2025: <small>*本文探讨了依赖版本更新导致代码输出不一致的问题。作者在迁移代码时发现，由于Pillow图像处理库从6.2.1升级到7.2.0，其默认插值策略改变导致resize()函数输出结果不同。文章分析了默认参数的利弊，指出其虽提升开发效率但存在潜在风险。作者建议采取两种应对策略：一是固定依赖版本确保稳定性；二是对关键参数进行显式配置。最后强调开发应以程序稳定运行为首要目标，盲目追求新版本可能得不偿失，并提醒开发者需谨慎对待工具依赖的版本管理。*</small>
* [TIP 2004 | Image quality assessment: From error visibility to structural similarity](https://blog.csdn.net/P_LarT/article/details/150463462) - Sun, 17 Aug 2025: <small>*本文介绍了全参考图像质量评估方法SSIM（结构相似性指数）的设计背景与实现。传统评估方法如MSE和PSNR虽计算简单，但与人类感知质量匹配度低。SSIM基于结构信息退化假设，通过亮度、对比度和结构三个分量评估图像质量。论文详细阐述了SSIM的算法框架，并对比了不同实现的高斯滤波处理方式差异。作者基于PyTorch实现了可微分的MSSIM代码，支持用户自定义padding和核形式参数，确保与现有实现兼容。该指标在图像处理系统优化、算法评估等领域具有重要应用价值。*</small>
* [ACMMM 2024 | Wave-Mamba: Wavelet State Space Model for Ultra-High-Definition Low-Light Image Enhance](https://blog.csdn.net/P_LarT/article/details/149830920) - Fri, 01 Aug 2025: <small>*针对超高清低照度图像增强中的计算复杂度和信息丢失问题，提出Wave-Mamba模型。该模型创新性地结合离散小波变换（DWT）与状态空间模型（SSM），通过小波域分析发现：1）93.7%图像能量集中于低频分量；2）高频对增强结果影响微弱。基于此，设计低频状态空间模块（LFSSBlock）进行全局增强，并通过改进的高频增强模块（HFEBlock）校正细节。*</small>
* [ICCV 2025 | WaveMamba: Wavelet-Driven Mamba Fusion for RGB-Infrared Object Detection](https://blog.csdn.net/P_LarT/article/details/149816528) - Fri, 01 Aug 2025: <small>*本文提出WaveMamba，一种基于小波变换和Mamba的RGB-红外跨模态目标检测方法。研究发现RGB和红外图像在频域具有互补特性：红外图像低频信息丰富，RGB图像高频细节突出。WaveMamba通过离散小波变换分解特征，采用低频Mamba融合块（结合通道交换和门控注意力）和高频绝对最大值增强策略，实现高效特征融合。在六个基准数据集上的实验表明，该方法平均mAP提升4.5%，同时保持较低计算开销，为跨模态目标检测提供了新思路。*</small>
* [ICCV 2025 | CWNet: Causal Wavelet Network for Low-Light Image Enhancement](https://blog.csdn.net/P_LarT/article/details/149617840) - Thu, 24 Jul 2025: <small>*本文提出一种基于因果推理与小波变换的低光照图像增强方法。CWNet通过因果干预分析揭示潜在因果关系，采用全局度量学习分离因果/非因果因子，并引入实例级CLIP语义损失确保局部一致性。同时设计基于小波变换的主干网络优化频域信息恢复。实验表明，CWNet在多个数据集上优于现有方法，有效解决了光照不均与语义保持的挑战。该方法为低光增强提供了新的因果推理视角，显著提升了视觉质量与语义准确性。*</small>
* [CVPR 2025 | Incomplete Multi-modal Brain Tumor Segmentation via Learnable Sorting State Space Model](https://blog.csdn.net/P_LarT/article/details/149468057) - Sat, 19 Jul 2025: <small>*针对多模态脑肿瘤分割中MRI模态缺失问题，提出了一种基于可学习排序状态空间模型(LS3M)的新方法。该框架通过可微分的动态重排机制(SortP)保留3D MRI的空间结构和语义关联，结合串联状态空间模型(S3M)高效建模长程依赖关系，并采用全局输入策略增强上下文感知。实验表明，在BraTS2018和BraTS2020数据集上，LS3M在模态缺失情况下显著优于现有方法。*</small>
* [ICML 2025 | FourierMamba: Fourier Learning Integration with State Space Models for Image Deraining](https://blog.csdn.net/P_LarT/article/details/149464229) - Sat, 19 Jul 2025: <small>*提出FourierMamba模型，将State Space Models与Fourier学习相结合用于图像去雨。针对现有频域方法忽视频率间依赖关系的问题，模型采用多尺度U-Net架构，核心包含Fourier Spatial Interaction SSM和Fourier Channel Evolution SSM两个模块。前者在空间维度通过改进的zigzag扫描策略（bilateral和progressive两种变体）有序处理频谱信息；后者在通道维度建模频率相关性。*</small>
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
