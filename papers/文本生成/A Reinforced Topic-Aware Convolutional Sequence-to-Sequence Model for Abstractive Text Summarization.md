# 一种用于抽象文本摘要的强化主题感知卷积序列到序列模型
> [daima_不完善](https://github.com/sc-lj/NLP/blob/8d2df8ffd2ce676c3ed0b704111931c745fe50a1/Summarization/ConvS2S/README.md)
[阅读笔记_机器之心](https://www.jiqizhixin.com/articles/IJCAI2018-Tencent-Model-for-Abstractive-Text-Summarization)
**另外，2018年的Facebook类似的：[代码完备](https://github.com/EdinburghNLP/XSum/tree/59f6884f8f81f9e1749db4053b2c26efd4f318a8)**
其他参考：[链接](https://github.com/SunshineBot/paper-notes/blob/4c17445c2fa23bc06011b9fc3990b210586f7b7c/Abstractive%20Text%20Summarization%20-%20Notes.md)
## Abstract
在本文中，我们提出了一种深度学习方法，通过**将主题信息合并到卷积序列到序列（ConvS2S）模型并使用自我关键序列训练（SCST）进行优化来解决自动摘要任务**。
通过**共同关注主题和词级对齐**(jointly attending to topics and word-level alignment)，我们的方法可以通过有偏差的概率生成机制(biased probability generation mechanism)来提高生成的摘要的一致性，多样性和信息性。
另一方面，像SCST一样，强化训练直接优化了关于非可微度度量ROUGE(non-differentiable metric ROUGE)的所提出的模型，这也避免了推理期间的暴露偏差(exposure bias during inference)。
我们使用Gigaword，DUC-2004和LCSTS数据集上的最先进方法进行实验评估。
实证结果证明了我们提出的方法在抽象概括中的优越性.
## 1 Introduction
**文本摘要的难点：**
>1. 自动文本摘要中的关键挑战是正确评估和选择重要信息，有效过滤冗余内容，以及正确聚合相关段并制作人类可读摘要
>2. 与输入和输出序列通常具有相似长度的机器转换任务不同，摘要任务更可能使输入和输出序列极不平衡。
>3. 此外，机器翻译任务通常在输入和输出序列之间具有一些直接的字级对齐，这在摘要中不太明显。 

**有两种类型的自动摘要技术，即提取和抽象。(extraction and abstraction)**
>1. 提取摘要的目标[Neto et al。，2002]是通过**选择源文档的重要部分并逐字连接来产生摘要**，
>2. 而抽象概括[Chopra et al。，2016]**基于核心思想生成摘要**。

>*抽象方法还应该能够正确地重写源文档的核心思想，并确保生成的摘要语法正确，便于人类阅读，这与人类进行摘要的方式非常接近*

**相关研究：**
>最近，深度神经网络模型已被广泛用于NLP任务，例如机器翻译[Bahdanau等，2014]和文本摘要[Nallapati等，2016b]。
特别是，**基于注意的序列 - 序列框架**[Bahdanau等，2014]与递归神经网络（RNNs）[Sutskever等，2014]在NLP任务中占优势。

**RNN的缺陷：**
>1. 然而，与基于CNN的模型([Dauphin等，2016])的分层结构相比，基于RNN的模型由于其非线性链结构而更容易出现梯度消失。
>2. 另外，RNN的**隐藏状态之间的时间依赖性阻止了序列元素的并行化**，这使得训练效率低下。

**本文的主要贡献：**
>在本文中，我们提出了一种**基于卷积序列到序列（ConvS2S）框架**[Gehring等，2017]与**主题感知注意机制相结合**的新方法。
据我们所知，这是自动抽象摘要的第一项工作，它**包含了主题信息，可以为深度学习架构提供主题和上下文对齐信息**。
此外，我们还通过**采用强化训练来优化**我们提出的模型
>1. 我们提出了一种**联合关注和偏向概率生成机制( a joint attention and biased probability generation mechanism)**，将主题信息合并到自动摘要模型中，该模型引入了上下文信息，以帮助模型生成更多连贯的摘要，增加多样性和信息量。
>2. 我们**在ConvS2S中采用自我关键序列训练技术**，针对不可微分的汇总度量ROUGE直接优化模型，这也解决了暴露偏差问题
>3. 三个基准数据集的广泛实验结果表明，通过充分利用:**通过主题嵌入和SCST增强的ConvS2S架构**的强大功能，我们提出的模型为抽象摘要提供了高精度，推进了最先进的方法。 

## 2 Related Work
*****
## 3 Reinforced Topic-Aware Convolutional Sequence-to-Sequence Model
>**在本节中，我们提出了强化的主题感知卷积序列到序列模型，它包括一个包含输入词和主题的卷积结构，一个多步联合注意机制，一个带主题信息偏置的生成结构和一个强化学习训练过程。**

![图1：主题感知卷积体系结构的图形说明](https://i.loli.net/2019/04/03/5ca44483e25dd.jpg)
> 图1：主题感知卷积体系结构的图形说明。
>1. 源序列的单词嵌入和主题嵌入由相关的卷积块（左下和右下）编码。
>2. 然后我们通过计算解码器表示（左上）和单词/主题编码器表示的点积来共同关注单词和主题。
>3. 最后，我们通过偏差概率生成机制生成目标序列。

### 3.1  ConvS2S Architecture
>我们利用ConvS2S架构[Gehring et al。，2017]作为我们模型的基础架构。
在本文中，**使用了两个卷积块，分别与wordlevel和topic-level嵌入相关联**。
我们在本节介绍前者，接下来介绍后者，以及**新的联合注意力机制和有偏文本生成机制**。

#### Position Embeddings(位置嵌入)
`x = (x1, . . . , xm)`表示输入的句子。输入单词的embed分布空间为 `w = (w1,...,wm)`，其中,`wi ∈ R^d`是随机初始化矩阵`Dword ∈ R^{V ×d}`中的一行；词汇表表示为`V`。 为了保留输入元素的位置信息，增加了位置embed，`p = (p1,...,pm)`，其中，`pi ∈ R^d`。最终，输入元素的embed为`e = (w1 + p1 , . . . , wm + pm )`。 用`q = (q1 , . . . , qn )`表示在decoder端输出元素的embedding。
#### Convolutional Layer(卷积层)
在encoder端和decoder端构建几层卷积神经网络，并且假设`卷积核大小为k`，`输入元素的维度为d`。那么卷积神经网络的将**k个输入元素进行串联**，得到`X ∈ R^{kd}`；映射得到的输出元素为`Y ∈ R^{2d}`; 即：
![title](https://i.loli.net/2019/04/03/5ca4526676ab6.png)
其中：核矩阵为`WY ∈ R^{2d×kd}`。偏差`bY ∈ R^{2d}`

重写输出`Y为Y=[A; B]`,其中 `A, B ∈ R^d`。这里引入一个新的概念--gated linear unit(GLU)，这类似于激活函数。
**g([A;B])=A ⊗ σ(B)**
其中，⊗ 表示矩阵的元素相乘，σ是sigmoid函数。GLU的输出空间为R^d。**GLU相当于Relu激活单元：(X * W + b)，加上一个Sigmoid激活单元：O(X * V + c)组成的。**
我们用`h^l =(h^l_1,...,h^l_n)`表示decoder端第l层的输出， `z^l = (z^l_1,...,z^l_m)`表示encoder端的第l层输出。 

下面以decoder端为例，第l个卷积层的第i个单元的计算公式为：
![title](https://i.loli.net/2019/04/03/5ca4542fed566.png)
其中:h^l_i ∈ R^d，◦ 表示复合函数.


#### Multi-step Attention(多步注意力机制)
引入注意力机制是为了使模型获得更多文本的历史信息。 先把当前的decoder状态h^l_i嵌入为:
![title](https://i.loli.net/2019/04/03/5ca4564f3bb26.png)
其中：`q_i ∈ R^d` 是先前decoded元素的embedding。权重 `W_d^l ∈ R^{d×d}`，偏差 `b^l_d ∈ R^d`。
在状态i和输入元素j的注意力权重α^l_{ij}的计算公式为：
![title](https://i.loli.net/2019/04/03/5ca4579699cd7.png)
其中：`z^{u_o}_j`表示上一次encoder端的输出结果.
当前decoder层的条件输入c^l_i ∈ R^d的计算公式:






********
### 3.2  Topic-Aware Attention Mechanism
>主题模型是一种用于发现源文章集合中出现的抽象主题思想或隐藏语义的统计模型。在本论文中，我们**使用了主题模型来获取文档的隐含知识以及将引入主题信息的多步注意力机制集成到 ConvS2S 模型中**，这有望为文本摘要提供**先验知识**。现在我们介绍**如何通过联合注意机制和带偏置概率生成过程将主题模型信息引入到基本 ConvS2S 框架中**

#### Topic Embeddings(主题嵌入)
#### Joint Attention(联合注意力机制？)
#### Biased Probability Generation(有偏概率生成)
************
### 3.3  Reinforcement Learning



