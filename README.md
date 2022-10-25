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
* [各种 IoU 损失变体](https://blog.csdn.net/P_LarT/article/details/127502104) - Mon, 24 Oct 2022: <small>*IoU损失及其各种变体已经在密集预测任务中展现出了优异的效果。这里做一个简单的罗列与梳理。*</small>
* [向日葵远控无法启动——[rpcclient]rpcclient_default::connect is error](https://blog.csdn.net/P_LarT/article/details/127423101) - Thu, 20 Oct 2022: <small>*解决linux桌面上向日葵启动失败的问题。即`[rpcclient]rpcclient_default::connect is error (sunloginclient:4212): Gtk-CRITICAL **:10:31:18.209: gtk_nain_quit: assertion 'nain_loops != NULL' failed`*</small>
* [PyTorch之F.pad的使用与报错记录](https://blog.csdn.net/P_LarT/article/details/127390628) - Tue, 18 Oct 2022: <small>*这一函数用于实现对高维tensor的形状补齐操作。模式中，padding的数量不得超出原始tensor对应维度的大小。常见的错误主要是因为padding的数量超过了对应模式的要求。模式中，padding的数量必须小于对应维度的大小。对于padding并没有限制。*</small>
* [ECCV 2022 | RGB图像引导下的基于轻量ToF传感器的深度估计](https://blog.csdn.net/P_LarT/article/details/127146695) - Sun, 02 Oct 2022: <small>*文章提出了一种深度估计任务。其主要针对轻量级ToF传感器采集的深度分布数据，在RGB图像的引导下，获得准确的高分辨率深度图，并为此提供了一个数据集。提出的模型获得了更加准确的深度补全和深度超分辨的效果。并实现了与商用级别的RGB-D传感器相当的性能。*</small>
* [CVPR 2022 | NeW CRFs: Neural Window Fully-connected CRFs for Monocular Depth Estimation](https://blog.csdn.net/P_LarT/article/details/127124910) - Fri, 30 Sep 2022: <small>*这篇文章将全局全连接CRF使用Attention进行了改造，并使用了基于窗偏移的计算过程实现了更低的计算量。提出的结构被用于单目深度估计任务模型的构建中。*</small>
* [ICCV 2021 Oral | CoaT: Co-Scale Conv-Attentional Image Transformers](https://blog.csdn.net/P_LarT/article/details/127023702) - Sat, 24 Sep 2022: <small>*设计了一种简化的线性注意力机制，并引入了卷积相对位置编码。基于这些构建了一个包含多尺度特征交互的架构。*</small>
* [CVPR2022 | MPViT: Multi-Path Vision Transformer for Dense Prediction](https://blog.csdn.net/P_LarT/article/details/126989548) - Thu, 22 Sep 2022: <small>*本文重点探究Transformer中的multi-scale patch embedding和multi-path structure scheme的设计。*</small>
* [OpenCV DNN模块常用操作](https://blog.csdn.net/P_LarT/article/details/126961138) - Tue, 20 Sep 2022: <small>*在实际利用opencv提供的dnn模块部署onnx格式的模型的时候，一些python端利用numpy可以简单轻易实现的操作，在C++端就得仔细考虑下实现的策略了。因为大多数并没有非常简单方便地使用形式，甚至可能需要自己去实现。这里做一个记录。*</small>
* [CVPR 2022 Oral | MAXIM: Multi-Axis MLP for Image Processing](https://blog.csdn.net/P_LarT/article/details/126931492) - Mon, 19 Sep 2022: <small>*这是一篇在底层视觉任务上构建更有效的局部+全局交互策略的文章，再多个任务上实现了良好的效果。*</small>
* [ECCV 2022 | MaxViT: Multi-Axis Vision Transformer](https://blog.csdn.net/P_LarT/article/details/126903713) - Sat, 17 Sep 2022: <small>*本文是针对Attention操作的一种改进。思路上来说之前的卷积方法中已经使用过类似的策略，但是作者们将这种思路用在Attention中，也展现出了良好的效果。提出的结构Multi-Axis Attention有效改善了原始Attention在实际应用中所欠缺的可放缩性，能够更有效的处理高分辨率特征。具体而言，就是通过完全借助局部注意力实现了局部交互和全局交互的形式（全局交互的实现思想其实值得借鉴），在有效降低计算复杂度的情况下，仍然获得了良好的表现。*</small>
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
