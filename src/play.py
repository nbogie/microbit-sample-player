from microbit import display, sleep, button_a, button_b
import audio

def frames_from_file(sndfile, frame):
    while(sndfile.readinto(frame, 32) > 0):
        yield frame

def play_snd(fname):
    frame = audio.AudioFrame()
    with open(fname, 'rb') as sndfile:
        audio.play(frames_from_file(sndfile, frame),wait=True)
        audio.stop()
    del frame

display.show('r')
while True:
    if button_a.is_pressed():
        play_snd('clip.raw')
    if button_b.is_pressed():
        play_snd('clip.raw')
        play_snd('clip.raw')
        play_snd('clip.raw')
        play_snd('clip.raw')
    sleep(200)
    
