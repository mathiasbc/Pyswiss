

class AutoParams(object):
    """
    This base class is supposed to be used as a base class or mixin.
    Is assigns all the arguments passed to the init method as instance
    named attributes.
    """
    def __init__(self, **kwargs):
        self.__dict__.update({k: v for k, v in kwargs.items() if k != 'self'})

