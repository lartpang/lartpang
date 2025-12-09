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
* [神经网络 | 从线性结构到可学习非线性](https://blog.csdn.net/P_LarT/article/details/155709559) - Mon, 08 Dec 2025: <small>*CNN、Transformer、ONN（Operational Neural Network）和KAN*</small>
* [储层计算 (Reservoir Computing) 概述](https://blog.csdn.net/P_LarT/article/details/155644579) - Sat, 06 Dec 2025: <small>*储层计算（RC）通过固定非线性储层与可训练线性读出的解耦设计，克服了传统递归神经网络训练中的梯度问题。其核心在于利用高维动力系统将输入信号映射到线性可分空间，仅需训练输出层权重。数学证明表明，当储层权重矩阵的谱半径满足特定条件时，系统具备回声状态属性和衰退记忆特性，确保状态收敛并遗忘久远历史。RC架构从随机连接演进到结构化拓扑（如简单环、带跳跃环），并发展出深度堆叠等变体，显著提升了计算效率与性能。这一范式为时间序列建模提供了高效解决方案。*</small>
* [告别乱码：OpenCV 中文路径（Unicode）读写的解决方案](https://blog.csdn.net/P_LarT/article/details/154360161) - Mon, 03 Nov 2025: <small>*本文针对OpenCV中文路径读取失败问题，提出了一种基于C++17标准库的跨平台解决方案。核心思路是：使用std::filesystem处理中文路径，利用std::fstream进行二进制文件读写，最后通过OpenCV的imdecode和imencode函数实现图像编解码。*</small>
* [生成模型 | DDPM -＞ Imrpoved DDPM -＞ DDIM](https://blog.csdn.net/P_LarT/article/details/150712115) - Sun, 24 Aug 2025: <small>*本文介绍了三种扩散模型变体：DDPM、Improved DDPM和DDIM。DDPM通过迭代去噪过程生成样本，但采样速度较慢。Improved DDPM改进了噪声调度策略，采用余弦形式的调整，并引入混合损失函数以优化训练。DDIM则通过非马尔可夫链设计，在保持相同训练目标的同时，显著加快采样速度。这三种方法在扩散模型的噪声处理、损失函数设计和采样效率上各有创新，推动了扩散模型在生成任务中的性能提升。*</small>
* [生成模型 | 扩散模型损失函数公式推导](https://blog.csdn.net/P_LarT/article/details/150646412) - Sat, 23 Aug 2025: <small>*本文推导了扩散模型的损失函数，通过引入前向分布简化计算，最终将损失分解为三部分：$L_T$（可忽略的常量）、$L_{t-1}$（KL散度项）和$L_0$（重构误差）。*</small>
* [生成模型 | 扩散模型公式推导](https://blog.csdn.net/P_LarT/article/details/150637291) - Sat, 23 Aug 2025: <small>*本文介绍了扩散模型的前向加噪和反向去噪过程。前向过程通过马尔科夫链逐步将数据$x_0$转化为高斯噪声$x_T$，其中噪声强度由预设参数$eta_t$控制。反向过程则利用神经网络从噪声$x_T$逐步恢复原始数据$x_0$。*</small>
* [ICCV 2025 | Reverse Convolution and Its Applications to Image Restoration](https://blog.csdn.net/P_LarT/article/details/150469410) - Sun, 17 Aug 2025: <small>*本文提出了一种新颖的深度可分离反向卷积算子（reverse convolution），通过建立并求解正则化最小二乘优化问题，实现了对depthwise卷积的有效反转。该算子采用FFT推导闭式解，并详细研究了核初始化、padding策略等实现细节。基于此构建的reverse卷积块结合了层归一化、1×1卷积和GELU激活，形成类Transformer结构，可直接替换现有网络中的常规卷积层，构建ConverseNet。*</small>
* [TCSVT 2023 | StructToken - Rethinking Semantic Segmentation with Structural Prior](https://blog.csdn.net/P_LarT/article/details/150464275) - Sun, 17 Aug 2025: <small>*一种新的语义分割范式，通过结构化token直接构建语义掩码并逐步细化，而非传统逐像素分类方法。作者设计了三种交互结构（CSE、SSE和静态卷积）来捕获特征图中的结构信息，并通过堆叠处理单元实现mask细化。*</small>
* [torchvision 中 deform_conv2d 操作的经验性解析](https://blog.csdn.net/P_LarT/article/details/150463945) - Sun, 17 Aug 2025: <small>*详细解析了torchvision中可变形卷积(deform_conv2d)的实现原理和使用方法。*</small>
* [一次由默认参数引起的思考](https://blog.csdn.net/P_LarT/article/details/150463724) - Sun, 17 Aug 2025: <small>*本文探讨了依赖版本更新导致代码输出不一致的问题。作者在迁移代码时发现，由于Pillow图像处理库从6.2.1升级到7.2.0，其默认插值策略改变导致resize()函数输出结果不同。文章分析了默认参数的利弊，指出其虽提升开发效率但存在潜在风险。作者建议采取两种应对策略：一是固定依赖版本确保稳定性；二是对关键参数进行显式配置。最后强调开发应以程序稳定运行为首要目标，盲目追求新版本可能得不偿失，并提醒开发者需谨慎对待工具依赖的版本管理。*</small>
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

## 💾 Some Datasets

| Name                                                                                                   | Description                                     |
| ------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| [**lartpang/OVCamo**](https://github.com/lartpang/OVCamo)                                              | Open-Vocabulary Camouflaged Object Segmentation |
| [**yooweey/AugmentedIRSTD1kTestset**](https://huggingface.co/datasets/yooweey/AugmentedIRSTD1kTestset) | Augmented Testset of the IRSTD-1k dataset       |
