# Converting Mp4 to Mp3
import os
import subprocess

files = os.listdir("Videos")
for file in files:
    tutorial_no = file.split(" #")[1].split(" -")[0]
    file_name = file.split("Sigma Web Development Course")[0]
    print(tutorial_no,file_name)
    subprocess.run(["ffmpeg", "-i", f"Videos/{file}", f"Audios/{tutorial_no}_{file_name}.mp3"])