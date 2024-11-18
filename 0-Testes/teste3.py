class SampleClass1:

    def __init__(self, a):
        ## calling the 'set_a() method' to set the value 'a' by ckecking certain conditions
        self.set_a(a)

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, a):

        ## condition ckeck whether 'a' is suitable or not
        if a > 0 and a % 2 == 0:
            self.__a = a
        else:
            self.__a = 2

obj = SampleClass1(15)

print(obj.get_a())