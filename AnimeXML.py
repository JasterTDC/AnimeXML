#! /usr/bin/Python

# Import xml parser.
import xml.etree.ElementTree as ElementTree

# Import url library.
from urllib.request import urlopen

# XML to parse.
sampleUrl = "http://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=16989"

# Read the xml as a file.
content = urlopen (sampleUrl)

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
