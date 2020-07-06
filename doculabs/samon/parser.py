from xml import sax

from .elements import BaseElement
from .environment import Environment
from .template import Template


class Parser(sax.ContentHandler):
    def __init__(self, environment: Environment):
        self.environment = environment
        self.template = Template()

        self.act_parent = None

    def parse(self, source: bytes):
        parser = sax.make_parser()
        #parser.setFeature(sax.handler.feature_external_pes, False)
        #parser.setFeature(sax.handler.feature_external_ges, False)
        parser.setFeature(sax.handler.feature_namespaces, True)
        #parser.setProperty(sax.handler.property_lexical_handler, self)
        parser.setContentHandler(self)
        parser.parse(source)

        return self.template

    def startElementNS(self, name, qname, attrs):
        ns, name = name

        if ns:
            fqdn = '{' + ns + '}' + name
        else:
            fqdn = name

        klass = self.environment.registry.get_class_by_name(fqdn)
        element = klass(tag_name=name, xml_attrs=attrs)
        if self.act_parent is None:
            assert self.template.root_element is None
            self.template.root_element = self.act_parent = element
        else:
            self.act_parent.add_child(element)
            self.act_parent = element

    def endElementNS(self, *args, **kwargs):
        self.act_parent = self.act_parent.parent
