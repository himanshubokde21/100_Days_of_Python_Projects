from moviepy import VideoFileClip
import os

cvt_video = VideoFileClip("input.mp4")
ext_audio = cvt_video.audio
save_path = os.path.join(os.path.expanduser('~'), 'Downloads', "output.mp3")
ext_audio.write_audiofile(os.path.join(save_path))

ext_audio.close()
cvt_video.close()

