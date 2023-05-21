import PIL
from PIL import Image
direc = input("Image file directory:")
im = Image.open(direc)
print("Select method:\n 1.Pixels per frame \n2.Frames count \n ")
sx,sy = im.size
method = input()
IndividualF = 1
FrameLength = 1
if method=="1":
	FrameLength = int(input("Pixels per Frame : "))
	IndividualF = sx/int(FrameLength)
elif method=="2":
	IndividualF = int(input("Frames : "))
	FrameLength = sx/int(IndividualF)

FrameLength = int(FrameLength)
IndividualF = int(IndividualF)

Frames = []
for x in range(IndividualF):
	box = (x*FrameLength, 0, (x*FrameLength)+FrameLength, sy)
	frm = im.crop(box)
	Frames.append(frm)

fps = int(input("Input FPS : "))
dur = 1/fps
Frames[0].save("SpSheet.gif",save_all=True,append_images=Frames[1:],optimize=False, duration=dur, loop=0)
