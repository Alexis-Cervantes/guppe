class Property:

    def __init__(self, var):
        ## Initializing the attribute
        self.a = var

    @property
    def a(self):
        return self.__a

    ## The attribute name and the method name must be same which is used to set the value for attribute
    @a.setter
    def a(self, var):
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2

# Creating an object for the class 'Property'
obj = Property(23)

print(obj.a)

