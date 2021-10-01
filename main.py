from extend_func import *
from pydub import AudioSegment
from pygame import mixer as Mi
from os import remove
import pafy, glob as G


Mi.init(48000)

def to_mp3(search):
    Y = YouTube(search)["url"]
    try: result = pafy.new(Y)
    except: runmain()
    print(result.title + " | " + Y,"\nDownload...")
    m4a = result.m4astreams[0]
    m4a.download()
    print("Completed!")
    name = G.glob("*.m4a")[0]
    Mp3 = AudioSegment.from_file(name, format="m4a")
    print("Converting...")
    Mp3.export("$music_temp.mp3", format="mp3" , bitrate='256')
    remove(name)
    print("Playing Music...")
    Mi.music.load("$music_temp.mp3")
    Mi.music.play()

def runmain():
    print('| \t\tOptions\t\t\t |')
    print('| \tT - To Search YouTube\t\t |')
    print('| \tS - To stop\t\t\t |')
    print('| \tV - To Change volume 1 - 10\t |')
    print('| \tX - To exit\t\t\t |')
    Select = input("input: ")
    if Select in "Tt":  # Enter 'Tube' to Search.
        try:
            Mi.music.unload()
            remove("$music_temp.mp3")
        except: pass
        finally:
            to_mp3(input("Input Music: ")) # Enter Title of song.
            runmain()
    elif Select in "Ss": # Enter 'Stop' to Stop Music and Delete File
        Mi.music.stop()
        Mi.music.unload()
        remove("$music_temp.mp3")
        runmain()
    elif Select in "Vv": # Change Volume of Music
        Mi.music.set_volume(eval(input("Volume: ")/10))
        print("Volume now is",Mi.music.get_volume())
        runmain()
    elif Select in "Xx":
        exit(0)
    else: runmain()
   
if __name__ == '__main__':
    runmain()
