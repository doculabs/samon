from io import BytesIO
from unittest import TestCase

from doculabs.samon import registry
from doculabs.samon.elements import BaseElement
from doculabs.samon.environment import Environment
from doculabs.samon.parser import Parser
from doculabs.samon.template import Template


class ParserTest(TestCase):
    def test_parse_result(self):
        parser = Parser(environment=Environment(loader=None))
        template = parser.parse(BytesIO(b'<root></root>'))
        self.assertIsInstance(template, Template)
        self.assertIsInstance(template.root_element, BaseElement)

    def test_parse_tree(self):
        tmpl = b"""
        <root>
            <child1>
                <subchild></subchild>
            </child1>
            <child2>
                <subchild></subchild>
                <subchildd></subchildd>
            </child2>
        </root>
        """
        parser = Parser(environment=Environment(loader=None))
        template = parser.parse(BytesIO(tmpl))

        root = template.root_element
        self.assertIsInstance(root, BaseElement)
        self.assertEqual(root.parent, None)
        self.assertEqual(len(root.children), 2)
        self.assertEqual(root.children[0].tag_name, 'child1')
        self.assertEqual(root.children[1].tag_name, 'child2')
        self.assertEqual(len(root.children[0].children), 1)
        self.assertEqual(len(root.children[1].children), 2)
        # template.show_element_tree()

    def test_parse_attributes(self):
        tmpl = b"""
        <root xmlns:c="http://example.org">
            <child attr1="val1" c:attr2="val2" />
            <child2></child2>
        </root>
        """
        parser = Parser(environment=Environment(loader=None))
        template = parser.parse(BytesIO(tmpl))

        child1 = template.root_element.children[0]
        self.assertSequenceEqual(list(child1.xml_attrs.keys()), ['attr1', '{http://example.org}attr2'])
        self.assertSequenceEqual(list(child1.xml_attrs.values()), ['val1', 'val2'])

        child2 = template.root_element.children[1]
        self.assertEqual(child2.xml_attrs, {})

    def test_parse_custom_element(self):
        tmpl = b"""
        <root>
            <example attr1="1" attr2="sdf" />
        </root>
        """

        @registry.element('example')
        class Example(BaseElement):
            pass

        parser = Parser(environment=Environment(loader=None))
        template = parser.parse(BytesIO(tmpl))

        self.assertIsInstance(template.root_element, BaseElement)
        self.assertIsInstance(template.root_element.children[0], Example)
