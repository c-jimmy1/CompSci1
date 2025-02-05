from PIL import Image ## must import Image first to be able to use it

image1, image2, image3, image4 = r'Labs\Lab4\ca.jpg',r'Labs\Lab4\im.jpg', r'Labs\Lab4\hk.jpg',r'Labs\Lab4\bw.jpg'
im = Image.new(mode="RGB", size=(512,512), color="white") # use mode 'RGB', color 'white'

image1 = Image.open(image1)
image2 = Image.open(image2)
image3 = Image.open(image3)
image4 = Image.open(image4)

im1 = image1.resize((256,256)) # resize to 256x256
im2 = image2.resize((256,256))
im3 = image3.resize((256,256))
im4 = image4.resize((256,256))

im.paste(im1, (0,0)) # paste image1 at (0,0)
im.paste(im2, (256,0)) # paste image2 at (256,0)
im.paste(im3, (0,256)) # paste image3 at (0,256)
im.paste(im4, (256,256)) # paste image4 at (256,256)

im.save("wallpaper.jpg") # save the image
im.show()