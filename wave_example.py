
import wave

obj = wave.open("/Users/pavithragopisetty/Documents/Arjun/mynewproject/Soundscape_Arjun/output.wav", "rb")

print("number of channels", obj.getnchannels())

t_audio = obj.getnframes() / obj.getframerate()

print(t_audio)

