import numpy as np
from tkinter import *
from tkinter import messagebox
from scipy.fft import fft, fftfreq
import librosa
import soundfile as sf

DICT_FREQ = {0: (0, 60), 60: (0, 170), 170: (60, 310),
             310: (170, 600), 600: (310, 1000), 1000: (600, 3000),
             3000: (1000, 6000), 6000: (3000, 10000)}

def indexer(freq, frequency):
    temp = frequency[:size//2]
    total = len(temp)
    differ = total // temp[-1]
    index = round(differ * freq)
    return index

def db_changer(freq, db, fourier, frequency):
    start, end = DICT_FREQ[freq]
    start, end = indexer(start, frequency), indexer(end, frequency)
    mid = indexer(freq, frequency)
    fourier = np.log10(fourier) * 20
    for i in range(start, mid):
        value = fourier[i] * (0.7 * (i - start) / (mid - start)) * db / 100
        value = value if value <= fourier[i] else fourier[i]
        fourier[i] += value
    for i in range(mid, end):
        value = fourier[i] * (0.7 * (end - i) / (end - mid)) * db / 100
        value = value if value <= fourier[i] else fourier[i]
        fourier[i] += value
    fourier /= 20
    fourier = np.power(10, fourier)
    return fourier

def update_db_changer():
    global fourier
    modified_fourier = np.copy(fourier)
    for i, slider in enumerate(sliders):
        freq = list(DICT_FREQ.keys())[i]
        db = slider.get()
        if db != 0:
            modified_fourier = db_changer(freq, db, modified_fourier, frequency)
    return modified_fourier

def save_modified_audio():
    modified_fourier = update_db_changer()
    reconstructed_audio = np.array(np.fft.ifft(modified_fourier), dtype="float64")
    sf.write("modified_audio.wav", reconstructed_audio, sample_rate)
    messagebox.showinfo("Success", "Modified audio saved successfully.")

audio_sample, sample_rate = librosa.load('stalker.wav', sr = 44100)
size = audio_sample.size
dt_audio = 1 / sample_rate
frequency = fftfreq(size, dt_audio)
fourier = fft(audio_sample)

root = Tk()
root.title("Audio Modifier")
root.geometry("800x220")

sliders_frame = Frame(root)
sliders_frame.pack(pady=10)

sliders = []
for i, freq in enumerate(sorted(DICT_FREQ.keys())):
    start, end = DICT_FREQ[freq]
    slider = Scale(sliders_frame, from_=100, to=-100, orient="vertical", resolution=1)
    slider.set(0)
    slider.grid(row=0, column=i, padx=10, pady=5)
    sliders.append(slider)

    freq_label = Label(sliders_frame, text=f"Freq: {freq}")
    freq_label.grid(row=1, column=i, padx=10)

ok_button = Button(root, text="OK", command=save_modified_audio)
ok_button.pack(pady=10)

root.mainloop()
