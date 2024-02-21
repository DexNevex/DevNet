import xmltodict

#open the xml file data.xml in the dir
stream = open('data.xml','r')

xml = xmltodict.parse(stream.read())

for e in xml["catalog"]["book"]:
  
    print("Id :" + e['@id'] + ", Title: [" + e['title'] + "]\n")