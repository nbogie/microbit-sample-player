from microbit import display, sleep, button_a, button_b
import audio

def frames_from_file(sndfile, frame):
    while(sndfile.readinto(frame, 32) > 0):
        yield frame
        for i in range(32):
            frame[i] = 0

def play_snd(fname, num_times):    
    frame = audio.AudioFrame()
    
    for i in range(num_times):
        with open(fname, 'rb') as sndfile:
            audio.play(frames_from_file(sndfile, frame),wait=True)            
    del frame
    audio.stop()

display.show('r')
while True:
    if button_a.is_pressed():
        play_snd('clip.raw', 1)
    if button_b.is_pressed():
        play_snd('clip.raw', 4)
    sleep(200)
    