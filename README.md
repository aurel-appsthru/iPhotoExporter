IPhotoExporter
===

*[Voir la version Française](https://github.com/aurel-appsthru/iPhotoExporter/blob/master/README.FR.md)*

iPhotoExporter is a python script that exports and synchronizes iPhoto events or albums (MacOSX) simply to folders.

In less than 5 minutes*, archive the contents of iPhoto in folders to see them from a NAS, a SmartTV or Windows for example!

It was also easier to identify duplicates with third party software.

*4'30 for 12GB of photos (MBP / SSD) 



###Key features : 

- Exports albums or events
- Synchronization of the elements
- Backup of originals (optional)
- Adds the title of the photo to the file name

Tested with iPhoto 11 9.2.3 on MacOSX 10.7.4 Lion.


Use
-----------
 
* Copy the script (for example in Documents)
* Run a Terminal (Applications> Utilities> Terminal)
* Move to the location of the script
 
		cd $HOME/Documents 

* Run the script like this:

		python iphotoexporter.py [options] "iPhoto Library" "destination-folder"


    Options:

		-a, -albums		albums processes instead of events
		-o -original	also exports original master images
		-v, -verbose	print all actions
		-t, -test		does not copy files and does not create folders

See the examples below.

Examples
--------

You want to export all events, with the original images:

    python iphotoexporter.py -o "$HOME/Pictures/iPhoto Library" "$HOME/Pictures/iPhoto Export"


    
Results
---------
* By default, iPhotoExporter exports events. To export the albums use the -a option.

* The script created a different folder for each album or event.

* Originals photos are suffixed with [original].

* Photos whose title was edited are suffixed with the caption in brackets.
    
---
###Disclaimer : 
Derived from the script of [Derrick Childers](https://github.com/derrickchilders) on [macosxhints](http://www.macosxhints.com/article.php?story=20081108132735425), the iPhotoExplorer script is characterized by the addition of the synchronization, backup of originals, and works with accented characters.
