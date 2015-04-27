#! /usr/bin/Python

# Import xml parser.
import xml.etree.ElementTree as ElementTree

# Import url library.
from urllib.request import urlopen

# Import sys library.
import sys

# XML to parse.
sampleUrl = "http://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime="

# Get the number of params we have in our application.
params = len (sys.argv)

# Check the number of params we have.
if (params == 1):
    print ("We need at least 1 anime identifier.")
else:
    for aid in range (1, params):
        # Read the xml as a file.
        content = urlopen (sampleUrl + sys.argv[aid])

        # XML content is stored here to start working on it.
        xmlData = content.readall().decode('utf-8')

        # Close the file.
        content.close()

        # Start parsing XML.
        root = ElementTree.fromstring (xmlData)

        for info in root.iter("anime"):
            print ("Id: " + info.get("id"))
            print ("Gid: " + info.get("gid"))
            print ("Name: " + info.get("name"))
            print ("Precision: " + info.get("precision"))
            print ("Type: " + info.get("type"))

        for info in root.iter ("info"):
            if ("Vintage" in info.get("type")):
                print ("Date: " + info.text)
