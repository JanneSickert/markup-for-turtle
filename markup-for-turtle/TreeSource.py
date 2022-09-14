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
                    self.settings["pad"]
                except:
                    try:
                        self.settings["fill"]
                        Draw.rectangle_with_color(int(self.settings["size"]), self.settings["fill"])
                    except:
                        Draw.rectangle(int(self.settings["size"]), self.settings["border"])
            except:
                print("ERROR: Markup Tags bei <rectangle> sind unvollständig")
        else:
            try:
                try:
                    self.settings["pad"]
                except:
                    try:
                        self.settings["fill"]
                        Draw.circle_with_color(int(self.settings["size"]), self.settings["fill"])
                    except:
                        Draw.circle(int(self.settings["size"]), self.settings["border"])
            except:
                print("ERROR: Markup Tags bei <circle> sind unvollständig")
        if self.child is not None:
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