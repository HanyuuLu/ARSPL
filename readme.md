# 停车位信息自动上报系统(Automatic reporting system of parking lot)(ARSPL)

![](https://img.shields.io/badge/LICENSE-MIT-green) ![](https://img.shields.io/badge/Python-3.x-blue) ![](https://img.shields.io/badge/OpenCV--python-3.4.2.16-blue)

# 运行方法
* 在采集设备中运行`client.py`
* 配置信息采集服务器并运行`server.py`

# 依赖
* websocket 8.1
* HyperLPR(项目中已自带，仅client需要)
* opencv-python 3.4.2.16(仅client需要)

# 可运行平台
* windows 7 sp1 above (Windows 10测试通过)
* Linux arm, x86, x86_64 (Raspberry pi测试通过)

- 本系统车牌识别功能由[HyperLPR](https://github.com/zeusees/HyperLPR)提供，我们在此处修正了两个 bug 以便于我们后续开发
  1. [#253](https://github.com/zeusees/HyperLPR/issues/253)
  2. [#252](https://github.com/zeusees/HyperLPR/issues/252)

# LICENSE

- [ARSPS](./LICENSE)
- [HyperLPR](./LICENSE_HyperLPR)
