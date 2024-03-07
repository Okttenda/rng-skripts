from moviepy.editor import VideoFileClip
import os


def extract_frames(movie, times, imgdir):
    if not os.path.exists(imgdir):
        os.makedirs(imgdir)

    clip = VideoFileClip(movie)
    for t in times:
        imgpath = os.path.join(imgdir, '{}.png'.format(int(t * clip.fps)))
        clip.save_frame(imgpath, t)


movie = 'first.mkv'
imgdir = './pngs'
clip = VideoFileClip(movie)
times = [i/clip.fps for i in range(int(clip.duration))]
extract_frames(movie, times, imgdir)
