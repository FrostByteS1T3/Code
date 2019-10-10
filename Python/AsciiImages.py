import Pillow
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`\". "
gscale2 = "@%#*+=-:. "
image = Image.open('Flower.jpg').convert('L')
w, h = image.size[0], image.size[1]
w = w / cols