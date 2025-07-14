import numpy as np
import sounddevice as sd
import time

def play_tone(frequency=550, duration=5, sample_rate=44100, volume=0.5):
    """Play a sine wave tone of a given frequency (Hz) and duration (sec)."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * frequency * t)
    wave *= volume  # scale volume (0.0 to 1.0)
    sd.play(wave, samplerate=sample_rate)
    sd.wait()

def pulse_tone(frequency=550, on_time=1, off_time=1, cycles=5):
    """Play a tone in pulses: ON for on_time, OFF for off_time, repeated."""
    for i in range(cycles):
        play_tone(frequency, on_time)
        time.sleep(off_time)

def sweep_tone(start_freq=500, end_freq=650, duration=10):
    """Play a tone that linearly increases frequency from start to end."""
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    freqs = np.linspace(start_freq, end_freq, t.shape[0])
    wave = np.sin(2 * np.pi * freqs * t)
    wave *= 0.5
    sd.play(wave, samplerate=sample_rate)
    sd.wait()

def alternate_tones(freq1=550, freq2=600, tone_duration=2, cycles=5):
    """Alternate between two frequencies for a given number of cycles."""
    for i in range(cycles):
        print(f"Cycle {i+1}: Playing {freq1} Hz")
        play_tone(freq1, tone_duration)
        time.sleep(0.2)  # slight pause for realism
        print(f"Cycle {i+1}: Playing {freq2} Hz")
        play_tone(freq2, tone_duration)
        time.sleep(0.2)



#play_tone(550, 10)             # Test T1
#play_tone(600,10)              # Test T2
pulse_tone(550, 1, 1, 10)      # Test T3
# sweep_tone(500, 650, 10)       # Test T4
#alternate_tones(550, 600, tone_duration=2, cycles=5)

