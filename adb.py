#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import subprocess
import random

def init_op():
    subprocess.Popen('adb shell input tap 540 1900', shell=True)
    time.sleep(2)
    subprocess.Popen('adb shell input tap 185 188', shell=True)
    time.sleep(2)

def read_news():
    # 看7-9篇文章
    news_count = random.randint(7, 9)
    for i in range(news_count):
        subprocess.Popen('adb shell input tap 500 ' + str(300 + 150 * i), shell=True)
        time.sleep(5)
        
        # 滑动阅读
        vec_swipe_count = random.randint(5, 10)
        for j in range(vec_swipe_count):
            second1 = random.randint(2, 5)
            time.sleep(second1)
            left1 = random.randint(300, 500)
            left2 = random.randint(300, 500)
            height1 = random.randint(1300, 1600)
            height2 = random.randint(600, 1000)
            subprocess.Popen('adb shell input swipe {} {} {} {}'.format(left1, height1, left2, height2), shell=True)
        
        # 收藏分享
        if i ==4 or i== 6:
            # 收藏
            subprocess.Popen('adb shell input tap 927 1874', shell=True)
            time.sleep(2)
            # 分享
            subprocess.Popen('adb shell input tap 1019 1869', shell=True)
            time.sleep(2)
            subprocess.Popen('adb shell input tap 137 1348', shell=True)
            time.sleep(2)
            subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
            time.sleep(2)

        # 评论
        if i == 1 or i==3:
            subprocess.Popen('adb shell input tap 490 1880', shell=True)
            time.sleep(5)
            commentKey = random.randint(1, 5)
            if commentKey == 1:
                subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "祖国万岁！人民万岁！"', shell=True)
            elif commentKey == 2:
                subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "富强、民主、文明、和谐"', shell=True)
            elif commentKey == 3:
                subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "中华民族崛起！"', shell=True)
            elif commentKey == 4:
                subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "坚持党的领导，人民当家作主"', shell=True)
            elif commentKey == 5:
                subprocess.Popen('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "跟着党走，好日子还在后头"', shell=True)
            time.sleep(2)
            subprocess.Popen('adb shell input tap 1009 1730', shell=True)
            time.sleep(5)
        
        # 返回
        subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
        time.sleep(5)

def watch_videos(): 
    subprocess.Popen('adb shell input tap 757 1863', shell=True)
    time.sleep(10)

    # 看6个视频
    for i in range(7):
        subprocess.Popen('adb shell input tap 500 ' + str(370 + 160 * (i)), shell=True)
        second = random.randint(300, 400)
        time.sleep(second)
        subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
        time.sleep(5)
        left1 = random.randint(300, 500)
        left2 = random.randint(300, 500)
        height1 = random.randint(1300, 1600)
        height2 = random.randint(600, 1000)
        subprocess.Popen('adb shell input swipe {} {} {} {}'.format(left1, height1, left2, height2), shell=True)
        time.sleep(5)

if __name__ == "__main__":
    init_op()
    read_news()
    watch_videos()
