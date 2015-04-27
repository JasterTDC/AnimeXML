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

        # Extract classic data.
        for info in root.iter("anime"):
            print ("Id: " + info.get("id"))
            print ("Gid: " + info.get("gid"))
            print ("Name: " + info.get("name"))
            print ("Precision: " + info.get("precision"))
            print ("Type: " + info.get("type"))

        # Extract date and general poster.
        for info in root.iter ("info"):
            if ("Vintage" in info.get("type")):
                print ("Date: " + info.text)

            if ("Picture" in info.get("type")):
                print ("Poster: " + info.get("src"))

        # Extract aditional posters.
        for img in root.iter ("img"):
            print ("Poster: " + img.get("src"))

        print ("")

        # Extract all the staff of this anime.
        result = {}
        for staff in root.getiterator ("staff"):
            # Initialize values.
            task = ""
            value = {}

            for elem in staff.getchildren():
                if elem.tag == "task" :
                    task = elem.text
                elif elem.tag == "person" :
                    tmp = elem.attrib

                    if "id" in tmp:
                        value["id"] = tmp["id"]
                    value["name"] = elem.text
            if task :
                result[task] = value

        print (result)

        # Extract cast data.
        cast_results = {}
        for cast in root.getiterator ("cast"):
            # Initializce values.
            role = ""
            value = {}

            for elem in cast.getchildren():
                if elem.tag == "role" :
                    role = elem.text
                elif elem.tag == "person" :
                    tmp = elem.attrib

                    if "id" in tmp:
                        value["id"] = tmp["id"]
                    value["name"] = elem.text

            if role :
                cast_results[role] = value
                
        result["cast"] = cast_results

        # Print data.
        print (result)
