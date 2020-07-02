import sys

from doculabs.samon.elements import BaseElement


class Template:
    def __init__(self):
        self.root_element = None

    def _show_element_subtree(self, element: BaseElement, stdout, indent: int=1):
        spaces = ' ' * (indent - 1) * 4
        print(f'{spaces} {element.__class__.__name__} <{element.tag_name}>', file=stdout)
        for child in element.children:
            self._show_element_subtree(child, stdout=stdout, indent=indent + 1)

    def show_element_tree(self, stdout=sys.stdout):
        return self._show_element_subtree(element=self.root_element, stdout=stdout)
