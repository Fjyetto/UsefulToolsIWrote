import sys
import subprocess

# This converts from any supported video to wmv

print('cmd entry:', sys.argv)
T='ffmpeg -y -i '+sys.argv[1]+' -s 640x640 '+sys.argv[1]+'CON.wmv'
print(T)
subprocess.call(T)