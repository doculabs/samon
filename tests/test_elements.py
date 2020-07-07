from unittest import TestCase

from doculabs.samon.elements import BaseElement
from doculabs.samon.expressions import Condition, ForLoop, Bind


class BaseElementTest(TestCase):
    def test_parse_xml_attributes(self):
        xml_attrs = {  # AttributesNSImpl like object
            (None, 'attr1'): 'val1',  # NS, attr_name
            ('http://example.org', 'attr2'): 'val2'
        }

        element = BaseElement(xml_tag='tag', xml_attrs=xml_attrs)
        self.assertEqual(element.xml_attrs, {'attr1': 'val1', '{http://example.org}attr2': 'val2'})

    def test_parse_expressions(self):
        xml_attrs = {
            ('https://doculabs.io/2020/xtmpl#control', 'if'): 'val == 7',
            ('https://doculabs.io/2020/xtmpl#control', 'for'): 'a in val',
            ('https://doculabs.io/2020/xtmpl#data-binding', 'attr2'): 'val'
        }

        e = BaseElement(xml_tag='tag', xml_attrs=xml_attrs)
        self.assertIsInstance(e.xml_attrs['{https://doculabs.io/2020/xtmpl#control}if'], Condition)
        self.assertIsInstance(e.xml_attrs['{https://doculabs.io/2020/xtmpl#control}for'], ForLoop)
        self.assertIsInstance(e.xml_attrs['{https://doculabs.io/2020/xtmpl#data-binding}attr2'], Bind)
