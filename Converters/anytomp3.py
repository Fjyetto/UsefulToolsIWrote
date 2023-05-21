import sys
from pydub import AudioSegment

# This converts from any supported audio to mp3

print('cmd entry:', sys.argv)
AudioSegment.from_file(sys.argv[1]).export(sys.argv[1]+"CONVERT.mp3", format="mp3")