

class TemplateError(Exception):
    """Base class for all template errors."""
    pass


class TemplateNotFound(TemplateError):
    pass
