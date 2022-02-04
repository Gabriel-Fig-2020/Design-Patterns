class Monostate(object):
    _estado = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._estado
        return obj

b = Monostate()
b1 = Monostate()
b.x = 4
print(dir(Monostate))
print(dir(b))
print("Monostate Object 'b': ", b)  ## b and b1 are distinct objects
print("Monostate Object 'b1': ", b1)
print("Object State 'b':", b.__dict__) ## b and b1 share same state
print("Object State 'b1':", b1.__dict__)
print("Object State id'b1':", id(b.__dict__)) ## b and b1 share same state
print("Object State id'b1':", id(b1.__dict__))