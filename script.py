import xml.dom.minidom

# ------------- 1
id = open("id.txt")
myList = []
for line in id:
    myList.append(line.strip())
id.close()

# ------------- 2
dom = xml.dom.minidom.parse("HM400041T40_190332398.xml")
dom.normalize()

# ------------- 3
for zap in dom.getElementsByTagName("ZAP"):
    for sl in zap.getElementsByTagName("Z_SL"):
        for idcase in sl.getElementsByTagName("IDCASE"):
            if idcase.firstChild.data in myList:
                # zap.getElementsByTagName("PACIENT")[0].getElementsByTagName("NPOLIS")[0].appendChild(tag)
                # newTag = dom.createElement("SMO_NAM")
                # newTagText = "наидентификацию"
                # newTagText.encode("utf-8").decode("cp1251")
                # newTag.appendChild(dom.createTextNode(newTagText))

                newTag = dom.createElement("SMO_NAM")
                newTag.appendChild(dom.createTextNode("наидентификацию"))
                newLine = dom.createTextNode("\n      ")

                levelParent = zap.getElementsByTagName("PACIENT")[0]
                levelChildren = levelParent.childNodes

                levelParent.insertBefore(newTag, levelChildren[7])
                levelParent.insertBefore(newLine, levelChildren[8])


# ------------- 4
new = open("new.xml", "wb")
new.write(dom.toxml(encoding="Windows-1251"))
new.close()

# new = open("new.xml", "a")
# dom.writexml(new, encoding="Windows-1251")
# new.close()