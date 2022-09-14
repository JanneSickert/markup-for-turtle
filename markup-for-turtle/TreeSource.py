import Draw

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
        if self.root_tag == "rectangle":
            try:
                try:
                    try:
                        f = self.settings["fill"]
                        b = self.settings["border"]
                        Draw.two_colors_rechteck(int(self.settings["size"]), self.settings["fill"], self.settings["border"])
                    except:
                        pass
                    try:
                        Draw.rectangle_with_color(self.settings["pad"], self.settings["fill"])
                    except:
                        Draw.rectangle(self.settings["pad"], self.settings["border"])
                except:
                    try:
                        f = self.settings["fill"]
                        b = self.settings["border"]
                        Draw.two_colors_rechteck(int(self.settings["size"]), self.settings["fill"], self.settings["border"])
                    except:
                        pass
                    try:
                        Draw.rectangle_with_color(int(self.settings["size"]), self.settings["fill"])
                    except:
                        Draw.rectangle(int(self.settings["size"]), self.settings["border"])
            except:
                print("ERROR: Markup Tags bei <rectangle> sind unvollständig")
        else:
            try:
                f = True
                try:
                    try:
                        f = self.settings["fill"]
                        b = self.settings["border"]
                        Draw.two_colors_circle(int(self.settings["size"]), self.settings["fill"], self.settings["border"])
                        f = False
                    except:
                        pass
                    try:
                        if f:
                            Draw.circle_with_color(self.settings["pad"], self.settings["fill"])
                    except:
                        if f:
                            Draw.circle(self.settings["pad"], self.settings["border"])
                except:
                    try:
                        f = self.settings["fill"]
                        b = self.settings["border"]
                        Draw.two_colors_circle(int(self.settings["size"]), self.settings["fill"], self.settings["border"])
                        f = False
                    except:
                        pass
                    try:
                        if f:
                            Draw.circle_with_color(int(self.settings["size"]), self.settings["fill"])
                    except:
                        if f:
                            Draw.circle(int(self.settings["size"]), self.settings["border"])
            except:
                print("ERROR: Markup Tags bei <circle> sind unvollständig")
        if self.child is not None:
            try:
                self.child.settings["pad"] = int(self.settings["size"]) - int(self.child.settings["pad"])
            except:
                pass
            self.child.draw()

    def print_values(self, level):
        space = ""
        i = 0
        while i < level:
            space += "    "
            i += 1
        print(space, self.root_tag, ":", str(self.settings))
        if self.child is not None:
            self.child.print_values(level + 1)
    
    def clean_values(self):
        TAGS = ("pad", "fill", "border", "size")
        for e in TAGS:
            try:
                if "<" in self.settings[e]:
                    self.settings[e] = self.settings[e].split("<")[0]
            except:
                pass
        if self.child != None:
            self.child.clean_values()