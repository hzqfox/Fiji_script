import os
import shutil
from ij.io import DirectoryChooser

#Get source directory from user selection.
srcDir = DirectoryChooser("Choose!").getDirectory()

#Create Rearranged directory to store copied images
reArrDir = os.path.join(srcDir,"Rearranged")
reArrDir_1 = os.path.join(reArrDir,"BF")
reArrDir_2 = os.path.join(reArrDir,"BF2")
if not os.path.exists(reArrDir):
    os.makedirs(reArrDir)    
    os.makedirs(reArrDir_1)
    os.makedirs(reArrDir_2)

#Loop through sub-directories inside source directory.
for name in os.listdir(srcDir):
	#check if path is a directory
	dirName = os.path.join(srcDir,name)
	if os.path.isdir(dirName):
		#Get source and target image
		src_1 = os.path.join(dirName,"BF.tif")
		dst_1 = os.path.join(reArrDir_1,(name+".tif"))
		src_2 = os.path.join(dirName,"BF2.tif")
		dst_2 = os.path.join(reArrDir_2,(name+".tif"))
		#Copy and rename image
		shutil.copyfile(src_1,dst_1)
		shutil.copyfile(src_2,dst_2)