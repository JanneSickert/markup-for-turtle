import turtle

VALID_TAGS = ("rectangle", "pad", "circle", "fill", "border", "size")
VALID_SHAPES = (VALID_TAGS[0], VALID_TAGS[2])

def is_xml_valid(xml):
    for e in VALID_TAGS:
        if xml.count(e) % 2 != 0:
            return False
    return True

class Parser:
    def __init__(self, xml):
        self.xml = xml
        self.obj = {}
    
    def parse_xml(self):
        xml2 = self.xml.split("<", 1)[1]
        xml3 = xml2.split(">", 1)
        root_tag = xml3[0]
        rest = xml[1]
        close_tag_index = rest.find(root_tag)
        close_tag = xml[1][close_tag_index : close_tag_index + len(root_tag)]
        print(close_tag)

if __name__ == "__main__":
    print("start MARKUP-FOR-TURTLE")
    datei = open('Markup.xml','r')
    xml = datei.read()
    xml_lines = xml.split("\n", xml.count("\n"))
    i = 0
    merged_xml = ""
    while i < len(xml_lines):
        merged_xml += xml_lines[i].lstrip()
        i = i + 1
    if is_xml_valid(xml):
        parser = Parser(merged_xml)
        parser.parse_xml()
    else:
        print("Syntax Error in Markup.xml")