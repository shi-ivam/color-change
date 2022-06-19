import os



def generate_frames(file_location):
    # delete all files in output folder
    files = os.listdir('output')
    for file in files:
        os.remove('output/'+file)
    # generate frames
    os.system("ffmpeg -i "+  file_location +" -vf fps=1 output/out%4d.png")
    os.system('python resize.py')

def generate_video(file_name):
    # generate video
    os.system("ffmpeg -framerate 10 -i output/out%4d.png catalog/" + file_name + ".mp4")