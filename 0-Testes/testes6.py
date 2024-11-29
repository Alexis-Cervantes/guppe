class FinalClass:

    def __init__(self, var):
        self.__set_a(var)

    def __get_a(self):
        return self.__a

    def __set_a(self, var):
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2

    a = property(__get_a, __set_a)

obj = FinalClass(12)

print(obj.a)
