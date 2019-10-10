from PIL import Image
import os
run = True

i = 0



while run == True:
    Img = Image.open(os.path.expanduser("~/Beans/beanman.jpg"))
    Img.show()
    i += 1
    if i > 500:
        break
    print(i)