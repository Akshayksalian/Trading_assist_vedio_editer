from flask import Flask
import os
import cv2
import pyrebase
from moviepy.editor import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    path = 'D:/Picture/Eve/test/'

    pre_imgs = os.listdir(path)

    images = []
    for i in pre_imgs:
        if i.endswith(".png") or i.endswith(".jpeg") or i.endswith(".jpg"):
            images.append(path+i)

    # cv2_forcc = cv2.VideoWriter_fourcc(*'mp4v')
    # frame = cv2.imread(images[0])
    # size = list(frame.shape)
    # del size[2]
    # size.reverse()

    # video = cv2.VideoWriter("D:/Picture/Eve/diwali 2019/image_py.mp4",cv2_forcc,1,size)

    # for i in range(len(images)):
    #     video.write(cv2.imread(images[i]))


    # video.release()

    # return "video created succesfully"

    clips = []

    # for j in images:
    #     clips.append(ImageClip(j).set_duration(1))

    clip1 = ImageClip('https://cdn.igp.com/f_auto,q_auto,t_pnopt12prodlp/products/p-blue-chocolate-pinata-ball-cake-for-birthday-750-grams--146283-m.jpg').set_duration(1)
    clip2 = ImageClip('https://cdn.igp.com/f_auto,q_auto,t_pnopt12prodlp/products/p-blue-chocolate-pinata-ball-cake-for-birthday-750-grams--146283-2.jpg').set_duration(2)
    clips.append(clip1)
    clips.append(clip2)
    audio_clip = AudioFileClip("https://samplelib.com/lib/preview/mp3/sample-12s.mp3")

    
    VideoClip = concatenate_videoclips(clips,method='compose').set_audio(audio_clip)
    VideoClip.write_videofile("video.mp4",fps=24,remove_temp=True,codec="libx264",audio_codec="aac")
    return "moviePy created vedio"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)