IPhotoExporter
---

*[Voir la version Française](README.FR.MD)*

<<<<<<< HEAD
En moins de 5 minutes*, archivez le contenu de iPhoto dans des dossiers traditionnels et consultables par exemple depuis un NAS, une SmartTV ou Windows par exemple !
=======
IPhotoExporter is a python script that exports and synchronizes iPhoto events or albums (MacOSX) simply to folders.
>>>>>>> English translation of the readme file

In less than 5 minutes*, archive the contents of iPhoto in folders to see them from a NAS, a SmartTV or Windows for example!

<<<<<<< HEAD
*4'30 pour 12Go de photos ( MBP/SSD ) 

###Fonctionnalités clés : 
=======
It was also easier to identify duplicates with third party software.
>>>>>>> English translation of the readme file

*4'30 for 12GB of photos (MBP / SSD) 



###Key features : 

- Exports albums or events
- Synchronization of the elements
- Backup of originals (optional)
- Adds the title of the photo to the file name

Tested with iPhoto 11 9.2.3 on MacOSX 10.7.4 Lion.


Use
-----------
<<<<<<< HEAD
* [Téléchargez le script](https://github.com/aurel-appsthru/iPhotoExporter/downloads) ( dans Documents par exemple )
* Lancez un Terminal ( Applications > Utilitaires > Terminal )
* Placez vous à l'emplacement du script
=======
* Copy the script (for example in Documents)
* Run a Terminal (Applications> Utilities> Terminal)
* Move to the location of the script
>>>>>>> English translation of the readme file

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

<<<<<<< HEAD
Vous souhaitez exporter tous les événements, avec les images originales :
=======
You want to export all events, with the original images:
>>>>>>> English translation of the readme file

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
