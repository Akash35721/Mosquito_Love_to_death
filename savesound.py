#this is to save these sounds in .wav file so they can be played on the phone USE VLC MEDIA PLAYER

import numpy as np
from scipy.io.wavfile import write
import os


output_dir = r"C:\Users\2004a\OneDrive - UPES\SEMESTER 7\non sharable\Mosquito_Love_to_death\sounds_to_test"
os.makedirs(output_dir, exist_ok=True)


sample_rate = 44100  # Hz
volume = 0.5

def generate_tone(filename, freq=550, duration=10):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * freq * t)
    wave = (wave * volume * 32767).astype(np.int16)
    write(os.path.join(output_dir, filename), sample_rate, wave)

def generate_alternating_tone(filename, freq1=550, freq2=600, duration_each=2, cycles=5):
    full_wave = []
    for _ in range(cycles):
        for freq in [freq1, freq2]:
            t = np.linspace(0, duration_each, int(sample_rate * duration_each), False)
            wave = np.sin(2 * np.pi * freq * t)
            full_wave.extend(wave)
    wave = (np.array(full_wave) * volume * 32767).astype(np.int16)
    write(os.path.join(output_dir, filename), sample_rate, wave)

def generate_sweep(filename, start_freq=500, end_freq=650, duration=10):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    freqs = np.linspace(start_freq, end_freq, t.size)
    wave = np.sin(2 * np.pi * freqs * t)
    wave = (wave * volume * 32767).astype(np.int16)
    write(os.path.join(output_dir, filename), sample_rate, wave)


generate_tone("tone_500Hz.wav", freq=500)
generate_tone("tone_550Hz.wav", freq=550)
generate_tone("tone_600Hz.wav", freq=600)
generate_alternating_tone("tone_550_600_alternating.wav")
generate_sweep("tone_500_to_650_sweep.wav")

