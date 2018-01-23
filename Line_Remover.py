from ij import IJ, ImagePlus  
from ij.process import FloatProcessor
from ij.io import FileSaver
from array import zeros
from random import random
#from numpy import ndarray


  
# Grab the last activated image  
imp = IJ.getImage()  
  
# Print image details  
print "title:", imp.title  
print "width:", imp.width  
print "height:", imp.height  
print "number of pixels:", imp.width * imp.height  
print "number of slices:", imp.getNSlices()  
print "number of channels:", imp.getNChannels()  
print "number of time frames:", imp.getNFrames()  

ip = imp.getProcessor().convertToFloat()
pixels = ip.getPixels()

pixels3 = pixels	

x = [1607,1608]
y = [47]

#print pixels[1610*y+x]
for i in x:
	for j in y:
		pixels3[1609*j+i] = 0

ip3 = FloatProcessor(ip.width, ip.height, pixels3, None)  
imp3 = ImagePlus(imp.title, ip3)

imp3.show()
 
#print "image type:", types[imp.type]

  




#for i in range (



#os.path.abspath(__file__)

#ary = [4095]*1024

#a = ndarray((1024),int)
#arr = [4095 for i in xrange(1024)]
#a = 1024 * [0]




#PC = ip.getPixelsCopy()


  
#imp = IJ.getImage()  
#fs = FileSaver(imp)  
  
# A known folder to store the image at:  
#folder = "/home/albert/Desktop/t2/fiji-tutorial"  
#folder = "/Users/AMETH/Dropbox/PhD-INI/Fiji_Script"
  
#filepath = folder + "/" + "output.tif"  
#fs.saveAsTiff(filepath):  


#print PC[0]







#line = ip.getRow(1,1,PC,1)

#print line
#print pixels[]

#pixels = imp.getPixels()           