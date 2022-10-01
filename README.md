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
* [CVPR 2022 |NeW CRFs: Neural Window Fully-connected CRFs for Monocular Depth Estimation](https://blog.csdn.net/P_LarT/article/details/127124910) - Fri, 30 Sep 2022: <small>*这篇文章将全局全连接CRF使用Attention进行了改造，并使用了基于窗偏移的计算过程实现了更低的计算量。提出的结构被用于单目深度估计任务模型的构建中。*</small>
* [ICCV 2021 Oral | CoaT: Co-Scale Conv-Attentional Image Transformers](https://blog.csdn.net/P_LarT/article/details/127023702) - Sat, 24 Sep 2022: <small>*设计了一种简化的线性注意力机制，并引入了卷积相对位置编码。基于这些构建了一个包含多尺度特征交互的架构。*</small>
* [CVPR2022 | MPViT: Multi-Path Vision Transformer for Dense Prediction](https://blog.csdn.net/P_LarT/article/details/126989548) - Thu, 22 Sep 2022: <small>*本文重点探究Transformer中的multi-scale patch embedding和multi-path structure scheme的设计。*</small>
* [OpenCV DNN模块常用操作](https://blog.csdn.net/P_LarT/article/details/126961138) - Tue, 20 Sep 2022: <small>*在实际利用opencv提供的dnn模块部署onnx格式的模型的时候，一些python端利用numpy可以简单轻易实现的操作，在C++端就得仔细考虑下实现的策略了。因为大多数并没有非常简单方便地使用形式，甚至可能需要自己去实现。这里做一个记录。*</small>
* [CVPR 2022 Oral | MAXIM: Multi-Axis MLP for Image Processing](https://blog.csdn.net/P_LarT/article/details/126931492) - Mon, 19 Sep 2022: <small>*这是一篇在底层视觉任务上构建更有效的局部+全局交互策略的文章，再多个任务上实现了良好的效果。*</small>
* [ECCV 2022 | MaxViT: Multi-Axis Vision Transformer](https://blog.csdn.net/P_LarT/article/details/126903713) - Sat, 17 Sep 2022: <small>*本文是针对Attention操作的一种改进。思路上来说之前的卷积方法中已经使用过类似的策略，但是作者们将这种思路用在Attention中，也展现出了良好的效果。提出的结构Multi-Axis Attention有效改善了原始Attention在实际应用中所欠缺的可放缩性，能够更有效的处理高分辨率特征。具体而言，就是通过完全借助局部注意力实现了局部交互和全局交互的形式（全局交互的实现思想其实值得借鉴），在有效降低计算复杂度的情况下，仍然获得了良好的表现。*</small>
* [Arxiv 2209 | Switchable Self-attention Module](https://blog.csdn.net/P_LarT/article/details/126896049) - Fri, 16 Sep 2022: <small>*这篇文章设计了一种可切换式的注意力模块（题目中是self-attention，但是实际模块设计用的还是原始的通道注意力）。在本文中，实验性的发现对于不同的网络层和不同的场景中，对于注意力模块而言，选择使用合适的激励操作是更有必要的。*</small>
* [ECCV 2022 | Lightweight Attentional Feature Fusion: A New Baseline for Text-to-Video Retrieval](https://blog.csdn.net/P_LarT/article/details/126878555) - Thu, 15 Sep 2022: <small>*本文主要讨论了文本检索视频任务中的特征融合问题。提出了一种基于轻量但是有效的特征融合模块LAFF构建的跨模态双端融合架构。*</small>
* [使用深度图像实现照片虚化效果](https://blog.csdn.net/P_LarT/article/details/126606557) - Tue, 30 Aug 2022: <small>*本文讨论了如何通过RGB-D图像对实现照片虚化。*</small>
* [从二值 Mask 获取外接矩形坐标](https://blog.csdn.net/P_LarT/article/details/126604438) - Tue, 30 Aug 2022: <small>*在数字图像处理中，我们有时候会需要计算二值mask对应的外接矩形。本文针对这一问题给出了几种方便的策略。*</small>
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
