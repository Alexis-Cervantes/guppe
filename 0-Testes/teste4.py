class Property:

    def __init__(self, var):
        ## Initializen the attributes
        self.var = var

    @property
    def a(self):
        return self.__a

