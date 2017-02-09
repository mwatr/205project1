from PIL import Image

def medianOdd(myList):
 listLength = len(myList)
 sortedValues = sorted(myList)
 middleIndex = ((listLength + 1)/2) - 1
 return sortedValues[middleIndex]

img = []
img.append(Image.open("1.png"))
img.append(Image.open("2.png"))
img.append(Image.open("3.png"))
img.append(Image.open("4.png"))
img.append(Image.open("5.png"))
img.append(Image.open("6.png"))
img.append(Image.open("7.png"))
img.append(Image.open("8.png"))
img.append(Image.open("9.png"))

pWidth, pHeight = img[0].size
print pHeight, pWidth
rPixel = []
gPixel = []    #To clear a list, re-initializa it.
bPixel = []
image = Image.new("RGB", (pWidth, pHeight), "white") 

for x in range(pWidth):
 for y in range(pHeight):
  for myImg in img:  #<----What does this do? In?
   myRed, myGreen, myBlue = myImg.getpixel((x,y))
   
   rPixel.append(myRed)
   gPixel.append(myGreen)
   bPixel.append(myBlue)
  
  aRedmedian = medianOdd(rPixel)
  aGrnmedian = medianOdd(gPixel)
  aBlumedian = medianOdd(bPixel)
  image.putpixel((x, y), (aRedmedian, aGrnmedian, aBlumedian))
  rPixel = []
  gPixel = [] #reinitialized!
  bPixel = []


image.save("Monument.png")  

#Apply the median filter
#Insert new pixels into new image <img.putpixel(xy, median value)>