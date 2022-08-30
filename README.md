# Hi 👋, I'm lartpang

## 🧑‍🤝‍🧑 Me

$$
\textbf{life} = \int_{birth}^{now} \mathbf{happy}(time) + \mathbf{sad}(time) d(time)
$$

<p align="center">A Python and PyTorch developer, deep-learning worker and open-source activist. I like python. Python can do anything.</p>

- 📝 I regulary write articles on [https://www.yuque.com/lart](https://www.yuque.com/lart)
- 💬 Ask me about **Python, PyTorch** in [ISSUES](https://github.com/lartpang/lartpang/issues)
- ⚡ Fun fact **I am a boy.**

## 📝 Recent Writing

<!-- writing starts -->
* [使用深度图像实现照片虚化效果](https://blog.csdn.net/P_LarT/article/details/126606557) - Tue, 30 Aug 2022: <small>*本文讨论了如何通过RGB-D图像对实现照片虚化。*</small>
* [从二值 Mask 获取外接矩形坐标](https://blog.csdn.net/P_LarT/article/details/126604438) - Tue, 30 Aug 2022: <small>*在数字图像处理中，我们有时候会需要计算二值mask对应的外接矩形。本文针对这一问题给出了几种方便的策略。*</small>
* [如何计算质心](https://blog.csdn.net/P_LarT/article/details/126474206) - Mon, 22 Aug 2022: <small>*本文介绍了质心的概念，以及基于Numpy、Scipy、OpenCV等工具的多种实现方式。*</small>
* [Arxiv 2207 | HorNet: Efficient High-Order Spatial Interactions with Recursive Gated Convolutions](https://blog.csdn.net/P_LarT/article/details/126416277) - Fri, 19 Aug 2022: <small>*这篇文章旨在使用卷积结构设计一种更加有效的空间交互模块。作者们通过递归门控策略设计了递归门控卷积操作，从而在特征内部构建了更高阶的空间交互过程。这种结构可以作者为一种即插即用的模块来提升视觉Transformer或者卷积模型。除了构建backbone，也可以用于解码器来提升密集预测任务的性能。...*</small>
* [Arxiv 2206 | Global Context Vision Transformers](https://blog.csdn.net/P_LarT/article/details/126409460) - Thu, 18 Aug 2022: <small>*本文的目的主要在于改进自注意力计算的高昂计算成本。所以基于局部自注意力的形式进行了扩展，实现了一种更加高效的全局注意力形式，而免去了Swin那样的划窗操作（划窗操作需要进行padding和mask，以及划窗仅仅会覆盖不同局部区域的部分内容）或者其他更为复杂的例如token unfolding和rolling操作，甚至是对于key和value的额外计算。......*</small>
* [Arxiv 2207 | LightViT: Towards Light-Weight Convolution-Free Vision Transformers](https://blog.csdn.net/P_LarT/article/details/126301936) - Fri, 12 Aug 2022: <small>*本文旨在改进轻量视觉Transformer模型的设计。*</small>
* [小心你的字典和样板代码](https://blog.csdn.net/P_LarT/article/details/126070605) - Sat, 30 Jul 2022: <small>*编码错误反思*</small>
* [Arxiv 2106 | Vision Transformers with Hierarchical Attention](https://blog.csdn.net/P_LarT/article/details/125702867) - Sun, 10 Jul 2022: <small>*本文重新设计了视觉Transformer中的多头自注意力（MHSA），以实现更高效的全局关系建模过程，同时又不牺牲细粒度信息。*</small>
* [CVPR 2022 | Cross-Image Relational Knowledge Distillation for Semantic Segmentation](https://blog.csdn.net/P_LarT/article/details/125671757) - Fri, 08 Jul 2022: <small>*当前用于视觉分割的知识蒸馏 (KD) 方法通常指导学生模仿教师网络从独立数据样本生成的结构化信息。然而，他们忽略了对 KD 有价值的跨图像的像素间全局语义关系。本文提出了一种新的跨图像的关系知识蒸馏 (CIRKD)，其重点是在整个图像之间迁移 pixel-to-pixel 和 pixel-to-region 的关系。其中的动机是一个好的教师网络可以根据全局像素依赖性构建一个结构良好的特征空间。CIRKD 使学生更好地模仿教师的结构化语义关系，从而提高分割性能。...*</small>
* [Vision MLP | ActiveMLP: An MLP-like Architecture with Active Token Mixer](https://blog.csdn.net/P_LarT/article/details/125318217) - Thu, 16 Jun 2022: <small>*与CycleMLP的思路和实现都非常类似的一篇工作。直观上来看，本文将偏移量的约束放宽，使用了可学习的形式，这一点正如我之前的文章《Pytorch中Spatial-Shift-Operation的5种实现策略》（Pytorch中Spatial-Shift-Operation的5种实现策略）中提到的那样，都可以看做是NIPS 2018的Constructing Fast Network through Deconstruction of Convolution一种特化版本。...*</small>
<!-- writing ends -->

View the archives @ [csdn@p_lart](https://blog.csdn.net/p_lart).

## 📽️ Some Projects

**PyTorch.**
* [**PyTorchTricks**](https://github.com/lartpang/PyTorchTricks), Some tricks of pytorch… :star:

**SOD.**
* **New:rocket::rocket::rocket:** [**MethodsCmp**](https://github.com/lartpang/MethodsCmp), A simple toolkit for counting the FLOPs/MACs, Parameters and FPS of the model.
* **Practical:wrench:** [**PySODEvalToolkit**](https://github.com/lartpang/PySODEvalToolkit), A Python-based salient object detection and video object segmentation evaluation toolbox.
* **Practical:wrench:** [**PySODMetrics**](https://github.com/lartpang/PySODMetrics), A simple and efficient implementation of SOD metrcis.
* [**PyLoss**](https://github.com/lartpang/PyLoss), Some loss functions for deeplearning.
* [**OpticalFlowBasedVOS**](https://github.com/lartpang/OpticalFlowBasedVOS), A simple and efficient codebase for the optical flow based video object segmentation.
* [**CoSaliencyProj**](https://github.com/lartpang/CoSaliencyProj), A project for co-saliency detection. Some codes are borrowed from ICNet. Thanks to ICNet Intra-saliency Correlation Network for Co-Saliency Detection (NIPS2020)~

**Usefull tools for your deeplearning project.**
* [**RunIt**](https://github.com/lartpang/RunIt), A simple program scheduler for your code on different devices.
* [**RegisterIt**](https://github.com/lartpang/RegisterIt), Register it: A more flexible register for the DeepLearning project.
* [**MSSIM.pytorch**](https://github.com/lartpang/MSSIM.pytorch), A better pytorch-based implementation for the mean structural similarity. Differentiable simpler SSIM and MS-SSIM.

<p align="center"><img src="https://komarev.com/ghpvc/?username=lartpang" alt="lartpang" /></p>
<p align="center">Generated by <a href="https://rahuldkjain.github.io/gh-profile-readme-generator/" alt="generator">Readme Generator</a></p>
