import sys
import requests
#from api_02 import *

#def process_audio(filename):
#    audio_url = upload(filename)
#    return save_transcript(audio_url, 'file_title')

#if __name__ == "__main__":
#    if len(sys.argv) > 1:
#        filename = sys.argv[1]
#    else:
#        filename = "/Users/Documents/Arjun/mynewproject/Soundscape_Arjun/recording.m4a"
#   
#    result = process_audio(filename)
#    print(result)  # This will be captured by the Swift code*/


import requests
from api_02 import *

filename = "/Users/Documents/Arjun/mynewproject/Soundscape_Arjun/recording.m4a"
audio_url = upload(filename)

save_transcript(audio_url, 'file_title')
