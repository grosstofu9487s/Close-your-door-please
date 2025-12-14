# 匯入一些必要的函式庫，如果裝置沒有下載的話到terminal打:
# pip install pygame opencv-python ultralytics
from ultralytics import YOLO # 讓程式可以用YOLO模型
from cv2 import VideoCapture # 讓程式可以開鏡頭
import pygame #讓程式可以播音樂
from time import sleep #讓程式可以等待

# 播音樂的功能初始化 & 把音檔載入到程式裡
pygame.init()
pygame.mixer.music.load('Audio.mp3')

# 匯入YOLO模型 & 定義要開啟的鏡頭
model = YOLO("close-your-door-please_v1.pt")
capture = VideoCapture(0)

# 必要變數
debounce_Time = 5 # 門沒關要等多少秒以後才會播音樂
FPS = 0 # 你懂
index = 0 # 主函式需要的變數，定義為: 門沒關以後經過了幾幀畫面，預設為 0

# 檢查門有沒有關的函式，回傳 100 / 運行的時間 & 門有沒有關 (有關會回傳 0 ，沒關會回傳 1)
def check_Door(frame): # 傳入一份參數，參數內容為一幀畫面的內容
    results = model(frame) # 用YOLO模型判斷那一幀畫面裡面門有沒有關

    for result in results: # 回傳結果，因為模型判斷後的結果有很多個，我們透過迴圈取得所有結果，再選擇我們想要讓函式回傳的結果
        return 100 / result.speed['inference'], result.probs.top1

# 播音樂，如果音樂已經在播了就不要播，如果門關了就把音樂關掉，如果門又沒關就再播
def play_Music(result, index): # 門有沒有關, 經過了幾幀畫面
    match result:
        case 1: # 如果門沒關
            if index >= FPS*debounce_Time: # 如果經過了指定時間後門還是沒關
                if pygame.mixer.music.get_busy(): # 如果音樂已經播了
                    return # 回去，然後就三仙歸洞了
                pygame.mixer.music.set_volume(1) # 調整音樂的音量
                pygame.mixer.music.play() # 播音樂
                
        case 0: # 如果門關了
            if pygame.mixer.music.get_busy(): # 如果音樂有在播
                for volume in range(int(pygame.mixer.music.get_volume())*10): # 這邊有點複雜，講簡單點就是把音樂的音量做淡出效果
                    sleep(0.1)
                    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)
                    # 其實不用淡出效果也可以，甚至還比較好寫，但我管他的，淡出效果很重要
                pygame.mixer.music.stop() # 停止播放音樂

# 主要函式 (因為透過鏡頭偵測所回傳的圖像是偵測到的每一幀影像，所以要用無限迴圈)
while True:
    try: # 嘗試開啟鏡頭
        ret, frame = capture.read()
    except ConnectionAbortedError: # 如果失敗了 (這邊定義的情況是沒偵測到鏡頭)
        print("Unable to use current camera.") # 跟你講你沒開鏡頭
        break

    FPS, result = check_Door(frame=frame) # 用上面定義的函式做這一幀畫面的判斷
    
    play_Music(result, index) # 用上面定義的函式播音樂

    match result: # 看你門有沒有關
        case 1: # 沒關
            index += 1 # 把這個變數加一，也就是門沒關過後過了幾幀
        case 0: # 關了
            index = 0 # 我懶得解釋了，氣貫長虹

# 2025/12/13 Sat
# Grosstofu