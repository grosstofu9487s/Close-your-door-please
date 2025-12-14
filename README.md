# Close-your-door-please
A YOLOv11 model that can tell you to close the door if you forgot to do it by plays a music.
</br>
一個我花大概三天訓練的Yolo模型，如果你忘記關門他會播一段音樂叫你去關。

<h1>How to use 如何使用</h1>
Just download all the file in source code, I'm just too lazy to create the release.
</br>
把所有檔案下載下來就可以用了，我懶得新增release。

<h1>Time Setting 時間設定</h1>
In default, the time from you forgot close the door to the music play is <b>5 second</b>, you can change it by change the value <b>debounce_Time</b> in the code in line 17
</br>
預設情況下，從你忘記關門到音樂播放的時間是 <b>5秒</b> ，你可以透過更改程式的第17行的 <b>debounce_Time</b> 變數值來變更這一段時間的時長。

<h1>Music Customize 音樂設定</h1>
In default, if you forget to close the door in the time you set, a music will play. the music is Blusrose from Hoshimachi suisei (my wife), so if you want to change that music just copy and replace the <b>Audio.mp3</b> file.
</br>
預設情況下，當你被程式判斷為開啟並經過了指定時間，一段音樂就會播放。預設的音樂會是星街彗星 (我老婆) 的Bluerose，如果你想改掉這個音樂的話把你要的音樂檔案直接覆寫 <b>Audio.mp3</b> 就可以了。
