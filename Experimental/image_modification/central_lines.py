from PIL import Image, ImageDraw


FILENAME = "example_1920.png"

img = Image.open(FILENAME)
draw = ImageDraw.Draw(img)

HALF_WIDTH = img.width // 2
HALF_HEIGHT = img.height // 2

print(f"W{HALF_WIDTH}, H{HALF_HEIGHT}")



# Horizontal line
draw.line(
    xy=((0, HALF_HEIGHT), (img.width, HALF_HEIGHT)),
    fill="white",
    width=1
)

# Vertical line
draw.line(
    xy=((HALF_WIDTH, 0), (HALF_WIDTH, img.height)),
    fill="white",
    width=1
)

img.show()