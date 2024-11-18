tclass SampleClass:

    def __init__(self, a: int, b: str) -> None:
        ## Private variable or property in Python
        self.__a = a
        self.b = b

    ## Getter method to get the properties using an object
    def get_a(self) -> int:
        return self.__a

    ## Setter method to change the value 'a' using an object
    def set_a(self, a: int) -> None:
        self.__a = a

    def get_b(self) -> str:
        return self.b

    def set_b(self, b: str) -> None:
        self.b = b

## Creating an object
obj = SampleClass(10, 'alexis')

## Getting the value of 'a' using get_a method
print(obj.get_a())
print(obj.get_b())

## Setting a new value to the 'a' using set_a method
obj.set_a(1974)
obj.set_b('Duda')

print(obj.get_a())
print(obj.get_b())











