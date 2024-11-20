class AnotherWay:

    def __init__(self, var):
        # Calling the set_a() method to set the value 'a' by checking certain conditions
        self.set_a(var)

    ## get method to get the properties using and object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using and object
    def set_a(self, var):

        ## Condition to check whether 'var' is suitable or not
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2

    a = property(get_a, set_a)

# Creating an object for 'AnotherWay' class
obj = AnotherWay(28)

print(obj.a)













