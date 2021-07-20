# import moviepy.editor as mpe
import threading
import time
import cv2
import pyautogui
import numpy as np
import pyaudio
import wave

def screen():
    codec = cv2.VideoWriter_fourcc(*"MP4V")
    out = cv2.VideoWriter("Recordedf.mp4", codec , 25, (1366, 768))
    cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Recording", 480, 270)
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img) 
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        if cv2.waitKey(1) == ord('q'):
            break

    out.release() 
    cv2.destroyAllWindows()

def voicee():
        
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "voice.mp3"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# def merger():
#     clip = mpe.VideoFileClip("Recordedf.mp4")
#     audio_bg = mpe.AudioFileClip("voice.mp3")
#     final_clip = clip.set_audio(audio_bg)
#     final_clip.write_videofile("output.mp4")


if __name__ =="__main__":
    t1 = threading.Thread(target=screen)
    t2 = threading.Thread(target=voicee)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    time.sleep(1)
    # merger()