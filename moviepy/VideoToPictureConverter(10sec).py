from moviepy.editor import VideoFileClip
import os


def FramesExtractor(imgdir, movie):
    if not os.path.exists(imgdir):
        os.makedirs(imgdir)

    clip = VideoFileClip(movie)
    print(clip.duration)
    clip_duration = int(clip.duration)
    print(clip_duration)

    image_numb = 0
    i = 0
    while i < clip_duration:
        imgpath = os.path.join(imgdir, '{}.png'.format(int(image_numb)))
        print(imgpath)
        image_numb += 1
        i += 1
        clip.save_frame(imgpath, image_numb)


movie = "second.mkv"
clip = VideoFileClip(movie)
imgdir = "./images"

FramesExtractor(imgdir, movie)
