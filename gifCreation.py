import imageio.v2 as imageio
filenames = ["images/a.png","images/b.png"]
images = []
for filenames in filenames:
    images.append(imageio.imread(filenames))
imageio.imsave('newfile.gif',images,'GIF',duration=2)


