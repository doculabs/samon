from xml.sax.xmlreader import AttributesImpl


class BaseElement:
    def __init__(self, tag_name: str, xml_attrs: AttributesImpl):
        self.tag_name = tag_name
        self.xml_attrs = xml_attrs

        self.parent = None
        self.children = []

    def add_child(self, element: 'BaseElement'):
        element.parent = self
        self.children.append(element)
