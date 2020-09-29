import shutil
import os
from lxml import etree
from XMLSplitter import XMLSplitter


class XMLReader:
    def __init__(self):
        print("XML Reader started")

    @classmethod
    def readXML(cls, split_file_name, save_file_path, concept_entry_count):
        # Get arguments from commandline

        print("User file name: ", split_file_name, " Save folder path: ", save_file_path, " Concepts per file: ",
              concept_entry_count)

        # User input error checking

        fileExtension = ".tbx" in split_file_name

        if not fileExtension:  # check for correct file extension (.xml)
            print("Incorrect file extension detected")
            exit(1)

        print("No problems detected with input!")

        # tidy up tbx file for processing
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(split_file_name, parser)
        fileencoding = tree.docinfo.encoding
        tree.write(split_file_name, xml_declaration=True, encoding=fileencoding, pretty_print=True)

        # Get base of names to make copy files

        # Process file and split into copies
        newpath = shutil.copy(split_file_name, save_file_path)
        splitText = "conceptEntry"

        print(newpath)
        XMLSplitter.runSplitter(newpath, splitText, concept_entry_count)

        # os.system(f"XMLSplitter.py {newpath} conceptEntry {concept_entry_count}")
        os.remove(newpath)