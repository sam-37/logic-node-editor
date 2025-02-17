from node_editor.gui.node import Node


class Print_Node(Node):
    def __init__(self):
        super().__init__()

        self.title = "Print"
        self.type_text = "Debug Nodes"
        self.set_color(title_color=(160, 32, 240))

        self.add_port(name="Ex In", is_output=False, execution=True)

        self.add_port(name="input", is_output=False)
        self.build()
