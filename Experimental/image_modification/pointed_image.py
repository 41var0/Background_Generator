from PIL import Image, ImageDraw


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

    pointer(
        width=img.width,
        height=img.height,
        colors=colors,
        drawable=draw
    )

    img.show()


def pointer(width:int, height:int, colors:tuple, drawable:ImageDraw):
    """Modify directly the image given pointing it with points 2x2 px all along its grid"""
    x, y = 0, 0
    color_switch = 0


    # revisar
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


if __name__ == '__main__':
    main()

