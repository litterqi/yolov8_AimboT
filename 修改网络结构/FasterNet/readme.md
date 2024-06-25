[论文]([https://arxiv.org/abs/2303.03667](https://github.com/litterqi/yolov8_AimboT/blob/main/%E4%BF%AE%E6%94%B9%E7%BD%91%E7%BB%9C%E7%BB%93%E6%9E%84/FasterNet/fasterNet.pdf))

![image](https://github.com/litterqi/yolov8_AimboT/assets/123362884/6ece2d8f-5f3c-4e3b-80c7-4d908b441873)

提出了一种新的PConv，在输入通道的一部分上应用常规Conv（卷积层）进行空间特征提取，并保持其余通道不变。在输入特征图上的有效感受野看起来像一个T形Conv，与常规Conv相比，它更专注于中心。

使用新型PConv和现成的PWConv作为主要的算子，进一步提出FasterNet：

![image](https://github.com/litterqi/yolov8_AimboT/assets/123362884/709016f1-201b-46e3-933b-9fe9d627302f)

整体架构有4个层级，层次级前面都有一个嵌入层或一个合并层。每个阶段都使用FasterNet Block进行计算。每个FasterNet Block有一个PConv层，后跟2个1*1的Conv层。
