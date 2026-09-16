from PIL.ImageDraw import ImageDraw



def triangle_from_vertical_lines(color:tuple, draw:ImageDraw, reverse:bool = False, upsidedown:bool = False):
    """
    Draws a triangle with vertical lines. Original orientation is left to right on decrease:
    :param reverse: Makes the triangle increase throughout width
    :param upsidedown: Makes the triangle turn upside-down
    :param color: Color of teh triangle
    :param draw: ImageDraw object of the image
    """
    # Usage examples:
    # triangle_from_vertical_lines(draw=draw, color=(55, 255, 255))
    # triangle_from_vertical_lines(draw=draw, color=(55, 255, 255), reverse=True)
    # triangle_from_vertical_lines(draw=draw, color=(55, 255, 255), upsidedown=True)
    # triangle_from_vertical_lines(draw=draw, color=(55, 255, 255), reverse=True, upsidedown=True)

    original_width, original_height = draw.im.size

    relation = (original_height / original_width)    # Relation between variables we're gonna iterate
    relation *= 4                  # is 4* because of pixels with movement
    orden = 1


    if (not reverse):
        max_triangle_height = original_height
    else:
        max_triangle_height = 0
        relation *= -1


    if (not upsidedown):
        min_triangle_height = 0
        vertical_steps = 2
    else:
        min_triangle_height = original_height
        max_triangle_height = original_height
        vertical_steps = -2  # vertical steps its 2 because of "pixels width"
        relation *= -1

    # at the end the relation needs to be negative or positive in order to
    #  increase or decrease the max_triangle_height: -*-=+ or -*+=-
    # relation *= orden







    print(f"Condiciones iniciales de max_triangle_height {max_triangle_height}")
    print(f"Condiciones iniciales de min_triangle_height {min_triangle_height}")
    print(f"Condiciones iniciales de vertical_steps {vertical_steps}")
    print(f"Condiciones iniciales de relation {relation}")


    for w in range(0, original_width, 4):
        for h in range(min_triangle_height, int(max_triangle_height), vertical_steps):

            draw.rectangle(xy=((w, h), (w + 1, h + 1)), outline=color)
            # Differece between methods :
            # img.putpixel((w+1, h), (55, 255, 255))   : Time take 0:00:00.517718
            # draw.rectangle(xy=((w, h), (w+1, h+1)))  : Time take 0:00:00.106540


        max_triangle_height = max_triangle_height - relation












