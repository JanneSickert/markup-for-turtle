VALID_TAGS = ("rectangle", "pad", "circle", "fill", "border", "size")
VALID_SHAPES = (VALID_TAGS[0], VALID_TAGS[2])
VALID_SETTINGS = (VALID_TAGS[1], VALID_TAGS[3], VALID_TAGS[4], VALID_TAGS[5])

class Tree:
    def __init__(self):
        self.child = None
        self.root_tag = None
        self.settings = {}

    def set_root_tag(self, root_tag):
        self.root_tag = root_tag

    def add_setting(self, setting, value):
        self.settings[setting] = value

    def draw(self):
        pass

    def print_values(self, level):
        space = ""
        i = 0
        while i < level:
            space += "    "
            i += 1
        print(space, self.root_tag, ":", str(self.settings))
        if self.child is not None:
            self.child.print_values(level + 1)

def is_xml_valid(xml):
    for e in VALID_TAGS:
        if xml.count(e) % 2 != 0:
            return False
    return True

def parse_root_element(xml):
    b1 = xml.find("<")
    b2 = xml.find(">")
    root_tag = xml[b1+1:b2]
    close_tag_index = xml.find("</" + root_tag + ">")
    content = xml[len(root_tag) + 2 : close_tag_index]
    result = {"root_tag": root_tag, "content": content}
    return result

def parse_xml(parsed_element : dict, tree):
    r = []
    while True:
        r.append(parse_root_element(parsed_element["content"]))
        length_sub = len(r[-1]["content"]) + 5 + len(r[-1]["root_tag"]) * 2
        length = len(parsed_element["content"]) - length_sub
        if not length > 0:
            break
        else:
            parsed_element["content"] = parsed_element["content"][length_sub:]
    tree.set_root_tag(parsed_element["root_tag"])
    for e in r:
        if e["root_tag"] in VALID_SHAPES:
            tree.child = parse_xml({"root_tag": e["root_tag"], "content": e["content"]}, Tree())
        elif e["root_tag"] in VALID_SETTINGS:
            tree.add_setting(e["root_tag"], e["content"])
        else:
            print("ERROR: Invalid tag")
    return tree

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
    if is_xml_valid(merged_xml):
        tree = parse_xml(parse_root_element(merged_xml), Tree())
        tree.print_values(1)
    else:
        print("Syntax Error in Markup.xml")