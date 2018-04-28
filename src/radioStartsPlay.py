from microbit import display, sleep, button_a, button_b
import audio, radio

def frames_from_file(sndfile, frame):
    while(sndfile.readinto(frame, 32) > 0):
        yield frame

def play_snd(fname):
    frame = audio.AudioFrame()
    with open(fname, 'rb') as sndfile:
        audio.play(frames_from_file(sndfile, frame),wait=True)
        audio.stop()
    del frame

def roar():
    play_snd('clip.raw')

radio.config(group=138)
radio.on()
display.show(')')

while True:
    incoming = radio.receive()
    if incoming is not None:
        display.show("!")
        roar()
        roar()
    if button_a.is_pressed():
        display.show('p')
        roar()
    if button_b.is_pressed():
        radio.send("roar")
        display.show(">")
        sleep(500)
    sleep(200)
    
