from PIL import Image, ImageDraw, GifImagePlugin

# this takes a background gif and overlays a foreground gifs on top of it

foregroundFrames = []
backgroundFrames = []
result = []

fg = Image.open("fg.gif")
bg = Image.open("bg.gif")

for frame in range(0,fg.n_frames):
    fg.seek(frame)
    foregroundFrames.append(fg.copy())
for frame in range(0,bg.n_frames):
    bg.seek(frame)
    backgroundFrames.append(bg.copy())
    
if len(foregroundFrames)!=len(backgroundFrames):
    raise Exception("Different gif length fg:"+str(len(foregroundFrames))+" bg:"+str(len(backgroundFrames)))

for frame in range(len(backgroundFrames)):
    result.append(Image.alpha_composite(backgroundFrames[frame].convert("RGBA"),foregroundFrames[frame].convert("RGBA")))
    
result[0].save('result.gif',save_all=True,append_images=result[1:],optimize=False,duration=40,loop=0)