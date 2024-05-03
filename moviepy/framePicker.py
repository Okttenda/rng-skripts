from moviepy.editor import VideoFileClip


def framePicker(second, imgpath):
    clip.save_frame(imgpath, second)


movie = "./video.mkv"
imgpath = "./"
clip = VideoFileClip(movie)

input_frame = input("Gebe die Sekunde des Frames an: ")
framePicker(input, imgpath)
