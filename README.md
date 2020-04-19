# xxqg
解放双手，每天自动刷一会攒29分。

dependence:    
- osx
- python3
- adb 
- 网易mumu模拟器 > 夜神模拟器 (分辨率调整为1920*1080)
- 安装ADBKey.apk,然后调整当前输入法为adbkeyboard,用于中文评论
 
how to use:
- 模拟器中打开xxqgAPP，登录
- 本地执行``python3 adb.py``

tips:
#### 当出现 ``` error: no devices/emulators found ```时
``` 
adb kill-server   
adb start-server
``` 
