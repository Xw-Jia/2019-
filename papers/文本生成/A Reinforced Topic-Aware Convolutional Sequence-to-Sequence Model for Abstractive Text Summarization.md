# 一种用于抽象文本摘要的强化主题感知卷积序列到序列模型
## Abstract
在本文中，我们提出了一种深度学习方法，通过**将主题信息合并到卷积序列到序列（ConvS2S）模型并使用自我关键序列训练（SCST）进行优化来解决自动摘要任务**。
通过**共同关注主题和词级对齐**(jointly attending to topics and word-level alignment)，我们的方法可以通过有偏差的概率生成机制(biased probability generation mechanism)来提高生成的摘要的一致性，多样性和信息性。
另一方面，像SCST一样，强化训练直接优化了关于非可微度度量ROUGE(non-differentiable metric ROUGE)的所提出的模型，这也避免了推理期间的暴露偏差(exposure bias during inference)。
我们使用Gigaword，DUC-2004和LCSTS数据集上的最先进方法进行实验评估。
实证结果证明了我们提出的方法在抽象概括中的优越性.
## Introduction
**文本摘要的难点：**
>1. 自动文本摘要中的关键挑战是正确评估和选择重要信息，有效过滤冗余内容，以及正确聚合相关段并制作人类可读摘要
>2. 与输入和输出序列通常具有相似长度的机器转换任务不同，摘要任务更可能使输入和输出序列极不平衡。
>3. 此外，机器翻译任务通常在输入和输出序列之间具有一些直接的字级对齐，这在摘要中不太明显。 

**有两种类型的自动摘要技术，即提取和抽象。(extraction and abstraction)**
>1. 提取摘要的目标[Neto et al。，2002]是通过选择源文档的重要部分并逐字连接来产生摘要，
> 2. 而抽象概括[Chopra et al。，2016]基于核心思想生成摘要。
