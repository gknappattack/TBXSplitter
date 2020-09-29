# TBXSplitter

A project as part of the Brigham Young University Translation and Research Group in hopes of making TBX termbase storage a common and viable option for CAT (Computer-Assisted Translation) companies and users across the world.

TBX Splitter will allow a user to enter in the file (.xml and .tbx) into a pop-up window and determine the number of conceptEntries they would like each file to be split into. After a short run time, the resulting files will be placed in the selected directory, titled after the original with an incrementing number trailing at the end of the file name before the extension.

TBX Splitter uses python.sax handling to process large sized files without strain on low-end devices, and can handle termbases of millions of entries, dividing them into more managable 1000+ entries modeled after the base file.

XMLSplitter.py's code is heavily based on nicwolff's (https://gist.github.com/nicwolff/b4da6ec84ba9c23c8e59) XML_Breaker.py script with slight modifications for different parameters and usability within a tkinter GUI and all credit is due to nicwolff for his simple yet effective SAX large XML file processer and splitter. 
