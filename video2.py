# -*- coding: utf-8 -*-
import cv2
#動画ファイルを読み込む
file_name = u"test2.mov"
video = cv2.VideoCapture(file_name)
#フレーム数を取得
frame_count = int(video.get(7))
#フレームレート(1フレームの時間単位はミリ秒)の取得
frame_rate = int(video.get(5))
#ウィンドウの名前を設定
cv2.namedWindow('player',  cv2.WINDOW_AUTOSIZE)
for i in range(frame_count):
    is_read, frame = video.read()
    #フレームレートのミリ秒数待つ
    k = cv2.waitKey(frame_rate)
    if k == 27 or not is_read:
        break
    cv2.imshow("player", frame)