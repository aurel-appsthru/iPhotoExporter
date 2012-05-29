#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Appsthru.com
# http://appsthru.com
# Contact : aurel@appsthru.com
#
# IPhotoExporter is a python script that exports and synchronizes 
# events or iPhoto albums (MacOSX) simply in folders.
# 

__version__ = "0.1"

from xml.dom.minidom import parse, parseString, Node
from optparse import OptionParser
import os, time, stat, shutil, sys,codecs,locale,unicodedata,datetime


def findChildElementsByName(parent, name):
    result = []
    for child in parent.childNodes:
        if child.nodeName == name:
            result.append(child)
    return result

def getElementText(element):
    if element is None: return None
    if len(element.childNodes) == 0: return None
    else: return element.childNodes[0].nodeValue

def getValueElementForKey(parent, keyName):
    for key in findChildElementsByName(parent, "key"):
        if getElementText(key) == keyName:
            sib = key.nextSibling
            while(sib is not None and sib.nodeType != Node.ELEMENT_NODE):
                sib = sib.nextSibling
            return sib


def unormalize (text ) :
	
	if type(text) is not unicode : 
		#print ">>converting text",text,"(repr:", repr(text) , " )to unicode"
		text =   text.decode("utf-8")
	
	return unicodedata.normalize("NFC",text)

def copyImage( sourceImageFilePath, targetFilePath , doCopy = True ) : 
	
	bCopyFile = False
	basename = os.path.basename(targetFilePath)
	
	if os.path.exists(targetFilePath):
	# if file already exists, compare modification dates
		targetStat = os.stat(targetFilePath)
		modifiedStat = os.stat(sourceImageFilePath)
     
		printv( "\t\tFile exists : %s , compare : " % (basename) )
		printv( "\t\t - modified: %d %d" % (modifiedStat[stat.ST_MTIME], modifiedStat[stat.ST_SIZE]) )
		printv( "\t\t - target  : %d %d" % (targetStat[stat.ST_MTIME], targetStat[stat.ST_SIZE]) )
	
		#why oh why is modified time not getting copied over exactly the same?
		if abs(targetStat[stat.ST_MTIME] - modifiedStat[stat.ST_MTIME]) > 10 or targetStat[stat.ST_SIZE] != modifiedStat[stat.ST_SIZE]:
			 
			printv( "\t\t --> File modified" )
			bCopyFile = True
			
		else : 
			printv( "\t\t --> File identical" )
			 
	else:
		bCopyFile = True
		
	if bCopyFile :	
		print "\t\tCopy of %s" % ( basename ) 
		if doCopy:
			shutil.copy2(sourceImageFilePath, targetFilePath)
	
	
	return  

 

def printv(*args):
	if verbose :
		# Print each argument separately so caller doesn't need to
		# stuff everything to be printed into a single string
		for arg in args:
		   print arg,
		print

# -----  MAIN  ----------

usage   = "Usage: %prog [options] <iPhoto Library dir> <destination dir>"
version = "iPhotoExporter version %s" % __version__

option_parser = OptionParser(usage=usage, version=version)
option_parser.set_defaults(
        albums=False,
        test=False,
        verbose=False,
        original=True
)

option_parser.add_option("-a", "--albums",
                             action="store_true", dest="albums",
                             help="use albums instead of events"
)
option_parser.add_option("-t", "--test",
                             action="store_true", dest="test",
                             help="don't actually copy files or create folders"
)   

option_parser.add_option("-v", "--verbose",
                             action="store_true", dest="verbose",
                             help="display most of the actions"
)  

option_parser.add_option("-o", "--original",
                             action="store_true", dest="original",
                             help="also copy original photos"
)  

(options, args) = option_parser.parse_args()

if len(args) != 2:
        option_parser.error(
            "Please specify an iPhoto library and a destination."
        )


iPhotoLibrary = unormalize( args[0] )
targetDir = unormalize( args[1] )

doCopy = not options.test  
useEvents = not options.albums  
verbose = options.verbose
copyOriginal = options.original

albumDataXml = os.path.join( iPhotoLibrary , "AlbumData.xml")

print ("Parsing AlbumData.xml")
startTime = time.time()

#minidom.parse produce Unicode strings
albumDataDom = parse(albumDataXml)
topElement = albumDataDom.documentElement
topMostDict = topElement.getElementsByTagName('dict')[0]
masterImageListDict = getValueElementForKey(topMostDict, "Master Image List")
folderList = []

if useEvents:
	listOfSomethingArray = getValueElementForKey(topMostDict, "List of Rolls")
else:
	listOfSomethingArray = getValueElementForKey(topMostDict, "List of Albums")
    

#walk through all the rolls (events) / albums

for folderDict in findChildElementsByName(listOfSomethingArray, 'dict'):
    if useEvents:
        folderName = getElementText(getValueElementForKey(folderDict, "RollName"))
    else:
        folderName = getElementText(getValueElementForKey(folderDict, "AlbumName"))
        if folderName == 'Photos':
            continue

    #walk through all the images in this roll/event/album
    imageIdArray = getValueElementForKey(folderDict, "KeyList")
    
    #add this event/album in the folderList for later root dir cleaning
    folderName = unormalize( folderName )
    folderList.append( folderName )
	
    print "\n\n*Processing folder : %s" % (folderName)
    #print repr(folderName)
    #print repr(targetDir)

    #create event/album folder
    targetFileDir = os.path.join(targetDir, folderName)
    if not os.path.exists(targetFileDir) :
	
	printv( "\t*Directory does not exist - Creating: %s" % targetFileDir )
	if doCopy:
		os.makedirs(targetFileDir)
    
    #image list for later folder cleaning
    imageList = [] 
    
    for imageIdElement in findChildElementsByName(imageIdArray, 'string'):
    
        imageId = getElementText(imageIdElement)
        imageDict = getValueElementForKey(masterImageListDict, imageId)
        modifiedFilePath = getElementText(getValueElementForKey(imageDict, "ImagePath"))
        originalFilePath = getElementText(getValueElementForKey(imageDict, "OriginalPath"))
        caption = getElementText(getValueElementForKey(imageDict, "Caption"))

        sourceImageFilePath = modifiedFilePath


	basename = os.path.basename(sourceImageFilePath)
	
	#basename = unormalize( basename )
        spname, spext = os.path.splitext(basename)
        
        # use the caption name if exists
	if spname != caption :
        	basename = spname  + " [" + caption.strip() + "]" + spext
        
        basename = unormalize( basename )
        print "\t*Processing image '%s' , ID : %s , Caption : %s" % ( spname, imageId, caption )
        
	targetFilePath = os.path.join(targetFileDir , basename ) 
 
        #add this image to the imageList for later folder cleaning
         
	imageList.append( basename )
	#print repr(basename)

	copyImage ( sourceImageFilePath, targetFilePath , doCopy  ) 
	
	# check if there is an original image
	if copyOriginal and originalFilePath != None : 
        	printv( "\t  *There is an original image")
        	basename = os.path.basename(originalFilePath)
        	
		spname, spext = os.path.splitext(basename)
		targetName = spname  + " [original]" + spext  
		
		targetName = unormalize( targetName )
		
        	targetFilePath = os.path.join(targetFileDir , targetName )
		imageList.append( targetName )
        	
        	copyImage ( originalFilePath, targetFilePath , doCopy  )
        	
        
    # Cleaning of this folder
 
    #searches the directory for files and compare to imageList
    #delete files not present in imageList
    print "\n\t*Cleaning of the folder :"
    for root, dirs, files in os.walk( targetFileDir ):
	for name in files:
		
		#print "file ", name 
		#print "type : ",type(name)
		#print "repr : ",repr(name)
		name = unormalize(name)
		#print repr(name)
		
		if name not in imageList : 
			printv( "\t - remove image : ",  name)
			
			os.remove( targetFileDir + "/" + name )
			
    print "\tcleaning done."		 



#Cleaning Root Folder
print "\n===================\n"
print "Cleaning Root folder :"

for root, dirs,files in os.walk( targetDir ):
	for name in dirs:
		
		#print "folder ", name 
		#print "type : ",type(name)
		#print "repr : ",repr(name)
		
			
		name = unormalize(name)
		
		if name not in folderList : 
			
			printv( "- remove '%s' " % name)
			#print repr(name)
			shutil.rmtree( os.path.join( targetDir, name )  )
	  			
print "cleaning done."
print ""

albumDataDom.unlink()

stopTime = time.time()

elapsedTime = stopTime - startTime

print "Elapsed time : ", datetime.timedelta(seconds=elapsedTime )
print ""



	    
		 
	
	 
	    
 
 
