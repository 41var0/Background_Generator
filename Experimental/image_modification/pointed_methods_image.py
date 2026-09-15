from PIL import Image, ImageDraw
from random import randrange

FILENAME = "example_1920.png"


def main():
    # img = Image.open(FILENAME)
    width, height = 1920, 1080
    img = Image.new('RGB', (width, height), "#006600")

    draw = ImageDraw.Draw(img)

    HALF_WIDTH = img.width // 2
    HALF_HEIGHT = img.height // 2

    print(f"W{HALF_WIDTH}, H{HALF_HEIGHT}")

    colors = ("#88A156", "#040C06")

    constant_pointer(
        width=img.width,
        height=img.height,
        colors=colors,
        drawable=draw
    )

    img.show()


def constant_pointer(width:int, height:int, colors:tuple[str, str], drawable:ImageDraw):
    """Modify directly the image given pointing it with points 2x2 px all along its grid"""
    x, y = 0, 0
    color_switch = 0

    while x != width:

        while y != height:
            drawable.rectangle(
                xy=((x, y), (x + 2, y + 2)),
                fill=colors[int(color_switch)]
            )

            color_switch = not color_switch
            y += 2

        x += 2
        y = 0
        color_switch = not color_switch


def gradient_pointer(width:int, height:int, gradient_intensivity:int, gradient_rotation:int, colors:tuple[str, str], drawable:ImageDraw):
    """

    :param width:
    :param height:
    :param gradient_intensivity: 0-1 ?
    :param gradient_rotation: 0-360º ?
    :param colors: tuple of 2
    :param drawable:
    :return:
    """

    hw, hh = width/2, height/2

    x, y = 0, 0
    color_switch = 0



    color = colors[]


    while x != width:

        while y != height:
            drawable.rectangle(
                xy=((x, y), (x + 2, y + 2)),
                fill=colors[int(color_switch)]
            )

            color_switch = not color_switch
            y += 2

        x += 2
        y = 0
        color_switch = not color_switch




def bool_by_percentage(p:int=50):
    return randrange(100) < p



if __name__ == '__main__':
    main()

