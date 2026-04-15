from PIL import Image

# Getting the PNG iamge
img_logo = Image.open("pngegg.png")

new_width = 64
new_height = int(new_width  * (img_logo.height/img_logo.width))
print(f"NW:{new_width}\nNH:{new_height}")


# Resizing better dimentions
resized_logo = img_logo.resize((new_width, new_height), resample=0)
resized_logo.show()

# Convertining it to ICO
resized_logo.save("icoegg5.ico", format="ICO", quality=100)
resized_logo.save("icoegg11.ico", format="ICO", quality=100)

print("new icon its done")