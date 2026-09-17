from PIL.ImageDraw import ImageDraw



def triangle_from_vertical_lines(draw:ImageDraw, color:tuple=(255, 255, 255), flip_h:bool = False, flip_v:bool = False):
    """
    Draws a triangle with vertical lines. Original orientation is left to right increassing:
    :param flip_h: Makes the triangle turn arround horizontally
    :param flip_v: Makes the triangle turn arround vertically
    :param color: Color of the triangle
    :param draw: ImageDraw object of the image
    """
    # Usage examples:
    # triangle_from_vertical_lines(draw=draw)
    # triangle_from_vertical_lines(draw=draw, color=color)
    # triangle_from_vertical_lines(draw=draw, color=color, flip_h=True)
    # triangle_from_vertical_lines(draw=draw, color=color, flip_v=True)
    # triangle_from_vertical_lines(draw=draw, color=color, flip_h=True, flip_v=True)

    original_width, original_height = draw.im.size

    relation = (original_height / original_width)    # Relation between variables we're gonna iterate
    relation *= 4                                    # is 4* because of pixels with movement


    # Fliping the image H and V makes them having some common variables
    if (not flip_v):
        min_triangle_height = original_height
        vertical_steps = -2
    else:
        min_triangle_height = 0
        vertical_steps = 2


    if (not flip_h != flip_v):
        max_triangle_height = original_height
    else:
        max_triangle_height = 0
        relation *= -1


    for w in range(0, original_width, 4):
        for h in range(min_triangle_height, int(max_triangle_height), vertical_steps):

            # "pixel" of 2x2 pixels
            draw.rectangle(xy=((w, h), (w + 1, h + 1)), outline=color)
            # Differece between methods :
            # img.putpixel((w+1, h), (55, 255, 255))   : Time take 0:00:00.517718
            # draw.rectangle(xy=((w, h), (w+1, h+1)))  : Time take 0:00:00.106540

        max_triangle_height = max_triangle_height - relation












