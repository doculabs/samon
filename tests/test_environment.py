from pathlib import Path

from unittest import TestCase

from doculabs.samon.environment import Environment
from doculabs.samon.loaders import FileSystemLoader


class EnvironmentTest(TestCase):
    def test_initialize(self):
        env = Environment(loader=FileSystemLoader('~'))
        self.assertEqual(env.loader.search_path, [Path.home()])

    """def test_element_mapping(self):
        env = Environment('templates')
        self.assertEqual(env.element_registry, {})"""
