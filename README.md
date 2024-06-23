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
* [ArXiv 2405 | Rethinking Scanning Strategies with Vision Mamba in SemSeg of Remote Sensing Imagery](https://blog.csdn.net/P_LarT/article/details/139011603) - Fri, 17 May 2024: <small>*这项研究对主流扫描方向及其组合对遥感图像语义分割的影响进行了全面的实验研究。通过在 LoveDA，ISPRS Potsdam 和 ISPRS Vaihingen 数据集上进行的广泛实验，我们证明，**无论其复杂性或所涉及的扫描方向数量如何，都没有单一的扫描策略能胜过其他扫描策略。简单的单个扫描方向被认为足以对高分辨率遥感图像进行语义分割。** 还建议了未来研究的相关方向。*</small>
* [ICLR 2024 | FasterViT: Fast Vision Transformers with Hierarchical Attention](https://blog.csdn.net/P_LarT/article/details/139006516) - Fri, 17 May 2024: <small>*本文提出了一种 CNN 和 ViT 的混合架构，即 FasterViT。这样的混合架构可以快速生成高质量 token，然后基于 Transformer 块来进一步处理这些 token。其重点在于结合架构组合和高效的注意力模块的设计，从而优化 ViT 模型的计算效率，提高图像的吞吐率，加强对于高分辨率图像的适应能力。*</small>
* [ICCV 2021 | FcaNet: Frequency Channel Attention Networks 中的频率分析](https://blog.csdn.net/P_LarT/article/details/138244386) - Sat, 27 Apr 2024: <small>*文章是围绕 2D 的 DCT 进行展开的，本文针对具体的计算逻辑进行梳理和解析。*</small>
* [CVPR 2024 - Rethinking the Evaluation Protocol of Domain Generalization](https://blog.csdn.net/P_LarT/article/details/137741841) - Sun, 14 Apr 2024: <small>*这篇文章主要讨论了领域泛化评估协议的重新思考，特别是如何处理可能存在的测试数据信息泄露风险。作者首先指出，当前的领域泛化评估协议可能存在问题，可能导致测试数据信息泄露，进而影响评估的公平性和准确性。作者还根据这些建议重新评估了十个代表性的领域泛化算法，并提供了三个新的测试leaderboard。这些更改和新的测试leaderboard的板将鼓励未来的研究，并促进领域泛化的更准确评估。*</small>
* [CVPR 2024 | Efficient Deformable ConvNets: Rethinking Dynamic and Sparse Operator](https://blog.csdn.net/P_LarT/article/details/137741750) - Sun, 14 Apr 2024: <small>*本文提出了高效的 DCNv4，这是一个专为视觉应用设计的高效有效的运算符。将 DCNv4 集成到其他现代骨干架构中，包括 ConvNeXt 和 ViT，替换深度可分离卷积和密集自注意力层。值得注意的是，在没有进行任何超参数调整的情况下，这些经过精心设计的网络在使用 DCNv4 时表现得相当出色，同时速度快得多，显示了动态、稀疏的 DCNv4 的有效性和效率。这些改进使得 DCNv4 与 DCNv3 相比显示出显著更快的收敛速度，并且处理速度大大提高，DCNv4 的速度提高了三倍以上。*</small>
* [CVPR 2024 | Retrieval-Augmented Open-Vocabulary Object Detection](https://blog.csdn.net/P_LarT/article/details/137677560) - Fri, 12 Apr 2024: <small>*RALF 通过从大型词汇库中检索词汇并增强损失函数和视觉特征来提高检测器对新类别的泛化能力。通过实验，作者证明了 RALF 在 COCO 和 LVIS 基准数据集上的有效性。特别是在 COCO 数据集的新类别上，APN50 提高了 3.4%，在 LVIS 数据集的新类别上，mask APr 提高了 3.6%。*</small>
* [CVPR 2024 | SED: A Simple Encoder-Decoder for Open-Vocabulary Semantic Segmentation](https://blog.csdn.net/P_LarT/article/details/137677438) - Fri, 12 Apr 2024: <small>*这篇文章提出了一种名为 SED 的简单编码器解码器，用于结合 CLIP 的 open-vocabulary 能力实现了开放词汇语义分割。在多个语义分割数据集上的实验证明了 SED 在开放词汇准确性和效率方面的优势。当使用 ConvNeXt-B 时，SED 在 ADE20K 上的 mIoU 得分为 31.6%，并且在单个 A6000 上每张图像只需 82 毫秒。*</small>
* [CVPR 2024 | Rethinking Interactive Image Segmentationwith Low Latency, High Quality, and Diverse Pro](https://blog.csdn.net/P_LarT/article/details/137635048) - Thu, 11 Apr 2024: <small>*现有的专家模型和通用模型在实现低延迟、高质量的交互式分割以及支持多种提示方面存在困难。研究人员提出了一种名为 SegNext 的方法，它重新引入了专家模型中常用的密集视觉提示的表示和融合方式，以促进高质量的分割。是实现高质量分割的关键设计选择。与现有的专家模型相比，该方法能够在保持低延迟的同时实现更好的分割效果。相比之下，本文提出的方法通过引入密集的视觉提示和优化模型结构，实现了低延时和高性能的图像分割效果。这篇文章主要研究了如何在保持低延迟的同时提高交互式图像分割的质量，并实现多种提示的兼容性。*</small>
* [CVPR 2024 | Open-Vocabulary Video Anomaly Detection](https://blog.csdn.net/P_LarT/article/details/137634977) - Thu, 11 Apr 2024: <small>*这篇文章主要研究了开放词汇视频异常检测（openvocabulary video anomaly detection，OVVAD）的问题，这是一个具有挑战性但实际重要的问题。实验结果表明，该模型在三个公开基准 UBnormal，UCF-Crime，XD-Violence 上优于现有方法，特别是在处理新类别时表现出明显的优势。利用语言图像预训练模型，如 CLIP 作为基础，得益于其强大的零样本泛化能力。，以更好地处理开放词汇视频异常检测问题。并引入了几个专用模块来促进对基线和新异常的检测。*</small>
* [CVPR 2024 | OVFoodSeg: Elevating Open-Vocabulary Food Image Segmentation via Image-Informed Textual](https://blog.csdn.net/P_LarT/article/details/137634899) - Thu, 11 Apr 2024: <small>*在整合视觉语言模型 CLIP 的基础上，为了处理食物配料视觉表征中大的类内方差，该方法集成了两个创新模块，即图像到文本学习器 FoodLearner 和图像感知的文本编码器 Image-Informed Text Encoder，丰富了文本嵌入与图像特定的信息，从而有效地将知识从已知的食材转移到新的食材。通过在大规模食品相关图像文本对数据集上预训练 FoodLearner，OVFoodSeg 成功地将视觉信息与文本表示紧密地联系起来，从而有效地解决了食材图像分割中的大类内变化问题。*</small>
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
