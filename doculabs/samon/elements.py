from xml.sax.xmlreader import AttributesNSImpl

from doculabs.samon.expressions import Bind, Condition, ForLoop


class BaseElement:
    def __init__(self, tag_name: str, xml_attrs: AttributesNSImpl):
        self.tag_name = tag_name

        self.xml_attrs = self._parse_xml_attrs(xml_attrs)
        self.parent = None
        self.children = []

    def _parse_xml_attrs(self, xml_attrs: AttributesNSImpl):
        attrs = {}
        for (namespace, attr_name), attr_value in xml_attrs.items():
            if namespace is None:
                attrs[attr_name] = attr_value
            else:
                key = '{' + namespace + '}' + attr_name
                if namespace == 'https://doculabs.io/2020/xtmpl#data-binding':
                    value = Bind(expr=attr_value)
                elif namespace == 'https://doculabs.io/2020/xtmpl#control':
                    if attr_name == 'if':
                        value = Condition(expr=attr_value)
                    elif attr_name == 'for':
                        value = ForLoop(expr=attr_value)
                    else:
                        raise ValueError  # TODO: raise custom error
                else:
                    value = attr_value

                attrs[key] = value

        return attrs

    def add_child(self, element: 'BaseElement'):
        element.parent = self
        self.children.append(element)
