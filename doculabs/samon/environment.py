from copy import copy

from doculabs.samon import registry


class Environment:
    def __init__(self, loader):
        self.loader = loader
        self.registry = copy(registry)
