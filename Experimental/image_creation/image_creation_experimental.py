from PIL import Image, ImageDraw
from datetime import datetime
from verified_methods_exp import triangle_from_vertical_lines


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

######################### Image & Draw
### Image and Draw creation
# img = Image.new('RGBA', (width, height), (88,  33, 222, 40))
img = Image.new('RGB', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(img)
#########################


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

######################### Lines
### Lines that split the image on four equals quarters
# draw.line(xy=((width/2, 0), (width/2, height)), width=1 , fill="grey")
# draw.line(xy=((0, height/2), (width, height/2)), width=1 , fill="grey")
#########################




### Tests
# t_i = datetime.now()
#
# triangle_from_vertical_lines(draw=draw, color=(55, 255, 255), reverse=True)
#
# t_f = datetime.now()
#
# print()
# print(f"Time take {t_f - t_i}")
#
# img.show()

# del img, draw
# img = Image.new('RGB', (width, height), (0, 0, 0))
# draw = ImageDraw.Draw(img)
# triangle_from_vertical_lines(draw=draw, color=(55, 255, 255))
# img.show(title="normal")
del img, draw
img = Image.new('RGB', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(img)
color = (55, 255, 255)
color1 = (55, 255, 255)
color2 = (55, 255, 255)
color3 = (55, 255, 255)
triangle_from_vertical_lines(draw=draw, color=color)
img.show(title="reversed")
# input()
img1 = Image.new('RGB', (width, height), (0, 0, 0))
draw1 = ImageDraw.Draw(img1)
triangle_from_vertical_lines(draw=draw1, color=color1, flip_h=True)
# img1.show(title="reversed")
# input()
img2 = Image.new('RGB', (width, height), (0, 0, 0))
draw2 = ImageDraw.Draw(img2)
triangle_from_vertical_lines(draw=draw2, color=color2, flip_v=True)
# img2.show(title="reversed")
# input()
img3 = Image.new('RGB', (width, height), (0, 0, 0))
draw3 = ImageDraw.Draw(img3)
triangle_from_vertical_lines(draw=draw3, color=color3, flip_h=True, flip_v=True)
# img3.show(title="reversed")


imas = (img, img1, img2, img3)
# imas = imas[::-1]º
def image_grid(imgs, rows, cols):
    """method from https://stackoverflow.com/a/65583584/31001735"""
    assert len(imgs) == rows * cols
    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols * w, rows * h))
    grid_w, grid_h = grid.size
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i % cols * w, i // cols * h))
    return grid
gri = image_grid(imgs=imas, rows=2, cols=2)
gri.show()

######################################
# img.save('exp_image.png')
# img.show()
######################################

print(f"\n\nDone {datetime.now()}")




