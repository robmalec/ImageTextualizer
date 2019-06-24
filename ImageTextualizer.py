from PIL import Image
import math
import sys

if len(sys.argv) < 2:
	print("Please provide a file path to the target image as a command line argument, like so:")
	print("python ImageTextualizer.py [Your/file/path/image.jpg]")
	exit()

i = Image.open(sys.argv[1])

gradFile = open("charGradient.txt", mode='r')
gradient=gradFile.read()
gradLength = len(gradient) - 1

w = i.width
h = i.height
s = ""
px = i.load()
for y in range(0,h):
    for x in range(0,w):
        thisPx = px[x,y]
        thisBrightness = ((thisPx[0] + thisPx[1] + thisPx[2]) / 3)
        gradChar = math.floor((thisBrightness/255) * gradLength)
        s += gradient[gradChar]
    s += "\n"

with open("output.txt", mode='w') as outputFile:
    outputFile.write(s)

print("Image has been textualized")
i.close()
gradFile.close()