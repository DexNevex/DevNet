import xml.etree.ElementTree as ET

#open the xml file data.xml in the dir
stream = open('data.xml','r')

xml = ET.parse(stream)

root = xml.getroot()

for e in root:
    print(ET.tostring(e)) 
    print("")

    print(e.get("id"))