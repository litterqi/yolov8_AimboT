# yolov8_AimboT

## 第一步
根据[requirements.txt](https://github.com/litterqi/yolov8_AimboT/blob/main/requirements.txt)安装需要的依赖包。

## 第二步
根据自身电脑所最高支持的cuda版本安装cuda。[cuda官网](https://developer.nvidia.com/cuda-toolkit)

安装pytorch，根据需求选择安装CPU版（大小为100MB）还是GPU版（大小为2G以上）。[pytorch官网](https://pytorch.org/)

## 第三步
下载[best.pt](https://github.com/litterqi/yolov8_AimboT/blob/main/best.pt)

之后AimboT须在best.pt下载的路径下运行

## 第四步
启动csgo。若安装的是GPU版的pytorch请运行[gpu_run.py](https://github.com/litterqi/yolov8_AimboT/blob/main/runs/gpu_run.py)文件，若是CPU版的pytorch请运行cpu_run.py文件。

（如果是国服csgo，请运行gpu_run_china.py或cpu_run_china.py）。
