# TBXSplitter

A project as part of the Brigham Young University Translation and Research Group in hopes of making TBX termbase storage a common and viable option for CAT (Computer-Assisted Translation) companies and users across the world.


TBX Splitter uses python.sax handling to process large sized files without strain on low-end devices, and can handle termbases of millions of entries, dividing them into more managable files with 1000's of entires that are modeled after the base file.

## Usage

TBX Splitter will allow a user to enter in the file (.xml and .tbx) into a pop-up window and determine the number of conceptEntries they would like each file to be split into. After a short run time, the resulting files will be placed in the selected directory, titled after the original with an incrementing number trailing at the end of the file name before the extension.

The following file should be run from the command line.

```
python TBXSplitter.py
```

This will run the tkinter GUI that allows for file selection. Once the window appears, the file to be split and the directory to write the split files out to can be selected. Selecting run will begin the proccess and pop up a success or failure window when the proccess is completed.

## Future Updates

I am no longer working with TBX/BYU Translation and Research Group so this code will no longer be updated or supported, but should still function for parsing and splitting XML and XML-based file types such as TBX.

## Attributions

XMLSplitter.py's code is adapted from nicwolff's (https://gist.github.com/nicwolff/b4da6ec84ba9c23c8e59) XML_Breaker.py script with slight modifications for different parameters and usability within a tkinter GUI. 

All credit is due to nicwolff for his simple yet effective SAX large XML file processer and splitter. 
