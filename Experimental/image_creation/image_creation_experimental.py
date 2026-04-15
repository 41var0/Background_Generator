from PIL import Image, ImageDraw
from datetime import datetime

from PIL.ImageFont import ImageFont, FreeTypeFont

#  vvvv --- Ratios --- vvvv #
# https://unisystem.com/uni-abc/lcd-screen-resolutions-and-aspect-ratios-key-parameters-and-applications
# 480p  (SD)     – 720  x 480  (345.600 pixels)
width, height = 720, 480

# 720p  (HD)     – 1280 x 720  pixels
# width, height = 1280, 720

# 1080p (FHD)    – 1920 x 1080 pixels
# width, height = 1920, 1080

# 1440p (2K QHD) – 2560 x 1440 pixels
# width, height = 2560, 1440

# 2160p (4K UHD) – 3840 x 2160 pixels
# width, height = 3840, 2160

# 4320p (8K UHD) – 7680 x 4320 (33.177.600 pixels)
# width, height = 7680, 4320
#  ^^^^ --- Ratios --- ^^^^ #


img = Image.new('RGBA', (width, height), (88,  33, 222, 40))

draw = ImageDraw.Draw(img)



draw.rectangle(xy=((width/2 -33, height/2 -33), (width/2 +33, height/2 +33)))
draw.text(  # https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html
    xy=(width/2 , height/2),
    text="ey!",
    align="center",
    font=FreeTypeFont("consolas.ttf", size=26),
    font_size=46,
    anchor="mm"
)
# draw.line(xy=((width/2, 0), (width/2, height)), width=1 , fill="grey")
# draw.line(xy=((0, height/2), (width, height/2)), width=1 , fill="grey")




# uv init numpy_101
# uv add ipykernel numpy



# Make a balck-withe pattern 1 by 2
# for w in range(width):
#     for h in range(height):
#         if (((w + h) % 6) != 0):
#             img.putpixel((w, h), (0,0,0))
#         if (((w - h) % 6) != 0):
#             img.putpixel((w, h), (0,0,0))

# img.putdata((500,)*365)

img.save('exp_image.png')
img.show()


print(f"Done {datetime.now().microsecond}")




