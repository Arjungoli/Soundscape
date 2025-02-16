# https://learnpython.com/blog/plot-waveform-in-python/
import wave
import numpy as np
import matplotlib.pyplot as plt
import sys
import librosa

wav_obj = wave.open('/Users/pavithragopisetty/Documents/Arjun/mynewproject/output.wav', 'r')

sample_freq = wav_obj.getframerate()
print(sample_freq)

n_samples = wav_obj.getnframes()
print(n_samples)

t_audio = n_samples/sample_freq
print(t_audio, "seconds")

signal_wave = wav_obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
print(signal_array.shape)

# for stereo:
#l_channel = signal_array[0::2]
#r_channel = signal_array[1::2]

times = np.linspace(0, n_samples/sample_freq, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title('Audio')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()

plt.figure(figsize=(15, 5))
plt.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()

def analyze_audio(audio_path):
    # Load the audio file
    y, sr = librosa.load(audio_path)
    
    # Perform your analysis here
    # For example, plotting the waveform
    plt.figure(figsize=(14, 5))
    plt.plot(y)
    plt.title('Waveform')
    
    # Save the plot
    output_path = audio_path.replace('.m4a', '_analysis.png')
    plt.savefig(output_path)
    plt.close()
    
    return f"Analysis saved to {output_path}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python plot_audio.py <audio_file_path>")
        sys.exit(1)
        
    audio_path = sys.argv[1]
    result = analyze_audio(audio_path)
    print(result)