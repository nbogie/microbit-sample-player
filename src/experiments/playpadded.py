from microbit import display, sleep, button_a
import audio

def frames_from_file(sndfile, frame):
    buff = audio.AudioFrame()
    while(sndfile.readinto(buff, 32) > 0):
        for i in range(16):
            frame[i*2] = buff[i]
            frame[i*2+1] = (buff[i+1] + buff[i])//2
        yield frame

def play_snd(fname):
    frame = audio.AudioFrame()
    with open(fname, 'rb') as sndfile:
        audio.play(frames_from_file(sndfile, frame),wait=False)
        sleep(1000)
        audio.stop()
    del frame

display.show('r')
while True:
    if button_a.is_pressed():
        play_snd('clip.raw')
    sleep(200)
    