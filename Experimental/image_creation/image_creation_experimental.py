from PIL import Image, ImageDraw
from datetime import datetime

from PIL.ImageFont import ImageFont, FreeTypeFont

#  vvvv --- Ratios --- vvvv #
# https://unisystem.com/uni-abc/lcd-screen-resolutions-and-aspect-ratios-key-parameters-and-applications
# 480p  (SD)     – 720  x 480  (345.600 pixels)
# width, height = 720, 480

# 720p  (HD)     – 1280 x 720  pixels
# width, height = 1280, 720

# 1080p (FHD)    – 1920 x 1080 pixels
width, height = 1920, 1080

# 1440p (2K QHD) – 2560 x 1440 pixels
# width, height = 2560, 1440

# 2160p (4K UHD) – 3840 x 2160 pixels
# width, height = 3840, 2160

# 4320p (8K UHD) – 7680 x 4320 (33.177.600 pixels)
# width, height = 7680, 4320
#  ^^^^ --- Ratios --- ^^^^ #


# img = Image.new('RGBA', (width, height), (88,  33, 222, 40))
img = Image.new('RGB', (width, height), (0, 0, 0))

draw = ImageDraw.Draw(img)


######################### Rectangulo
# draw.rectangle(xy=((width/2 -33, height/2 -33), (width/2 +33, height/2 +33)))
#########################


######################### Text
# draw.text(  # https://pillow.readthedocs.io/en/stable/handbook/text-anchors.html
#     xy=(width/2 , height/2),
#     text="ey!",
#     align="center",
#     font=FreeTypeFont("consolas.ttf", size=26),
#     font_size=46,
#     anchor="mm"
# )
#########################


# draw.line(xy=((width/2, 0), (width/2, height)), width=1 , fill="grey")
# draw.line(xy=((0, height/2), (width, height/2)), width=1 , fill="grey")




# Make a balck-withe pattern 1 by 2

custom_height = height
rel = - (width/ height)


for w in range(0, width, 4):
    for h in range(0, custom_height, 4):

            # print((w, h))
            img.putpixel((w, h), (50, 255, 255))
            img.putpixel((w+1, h), (50, 255, 255))
            img.putpixel((w, h+1), (50, 255, 255))
            img.putpixel((w+1, h+1),(50, 255, 255))

    custom_height = int(custom_height + (rel))
    print(f"{custom_height}, ", end="")








# custom_height = height
# for w in range(0, width, 2):
#     for h in range(0, custom_height, 2):
#
#             print((w, h))
#             img.putpixel((w, h), (50, 255, 255))
#     custom_height = int(custom_height - 6*(1/custom_height))
#     print()
# img.putdata((500,)*365)


# Con "marco"
# for w in range(20, width -20, 2):
#     for h in range(20, height -20, 2):

img.save('exp_image.png')
img.show()


print(f"\n\nDone {datetime.now()}")




