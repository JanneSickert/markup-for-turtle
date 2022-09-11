import turtle

VALID_TAGS = ("rectangle", "pad", "circle", "fill", "border", "size")
VALID_SHAPES = (VALID_TAGS[0], VALID_TAGS[2])

def is_xml_valid(xml):
    for e in VALID_TAGS:
        if xml.count(e) % 2 != 0:
            return False
        else:
            return True

if __name__ == "__main__":
    print("start MARKUP-FOR-TURTLE")
    datei = open('Markup.xml','r')
    xml = datei.read()
    if is_xml_valid(xml):
        pass
    else:
        print("Syntax Error in Markup.xml")