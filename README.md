IPhotoExporter
---

IPhotoExporter est un script python qui exporte et synchronise les événements ou les albums iPhoto ( MacOSX ) simplement vers des dossiers.

En moins de 5 minutes*, archivez le contenu de iPhoto dans des dossiers traditionnels et consultables par exemple depuis un NAS, une SmartTV ou Windows par exemple !

Plus facile aussi pour repérer les doublons grâce à des logiciels tiers. 

*4'30 pour 12Go de photos ( MBP/SSD ) 

###Fonctionnalités clés : 

- exporte les albums ou les événements
- synchronisation des éléments
- sauvegarde des originaux ( option )
- ajoute le titre de la photo au nom du fichier

Testé avec iPhoto 11 9.2.3 sur MacOSX Lion 10.7.4.


Utilisation
-----------
* [Téléchargez le script](https://github.com/aurel-appsthru/iPhotoExporter/downloads) ( dans Documents par exemple )
* Lancez un Terminal ( Applications > Utilitaires > Terminal )
* Placez vous à l'emplacement du script

		cd $HOME/Documents 

* Lancez le script comme ceci :

		python iphotoexporter.py [options] "Librairie-iPhoto" "dossier-destination"


    Options:

        -a, --albums		traite les albums à la place des événements
        -o, --original		exporte aussi les images originales    
        -v, --verbose		affiche toutes les actions
        -t, --test			ne copie pas les fichiers et ne créé pas les dossiers

Consultez les exemples ci-dessous.

Examples
--------

Vous souhaitez exporter tous les événements, avec les images originales :

    python exportiphoto.py -o "$HOME/Pictures/Bibliothèque iPhoto" "$HOME/Pictures/iPhoto Export"


    
Résultat
---------

* Par défaut, iPhotoExporter exporte les événements. Pour exporter les albums utilisez l'option -a.

* Le script créé un dossier différent pour chaque événement ou album.

* Les photos d'origines sont suffixées avec le texte [original].

* Les photos dont le titre a été édité sont suffixées avec ce titre entre crochets. 

    
---
###Confession : 
Dérivé du script de [Derrick Childers](https://github.com/derrickchilders) sur [macosxhints](http://www.macosxhints.com/article.php?story=20081108132735425), le script iPhotoExplorer se distingue par l'apport de la synchronisation, de la sauvegarde des originaux et fonctionne avec les caractères accentués.
