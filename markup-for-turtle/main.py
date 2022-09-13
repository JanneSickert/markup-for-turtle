from fileinput import close
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
    
    def parse_root_element(self):
        b1 = self.xml.find("<")
        b2 = self.xml.find(">")
        root_tag = self.xml[b1+1:b2]
        close_tag_index = self.xml.find("</" + root_tag + ">")
        content = self.xml[len(root_tag) + 2 : close_tag_index]
        result = {"root_tag": root_tag, "content": content}
        return result

    def is_tag(self, xml):
        if xml.find("<"):
            return True
        else:
            return False

    def parse_xml(self) -> str:
        content = self.xml
        while is_tag(content):
            flag = True
            while flag:
                r = self.parse_root_element(content)
                # erstelle geparste elemente.
                length = len(r["root_tag"]) * 2 + 5 + len(r["content"])
                if length < len(content):
                    content = content[length:]
                else:
                    flag = False

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