from dataclasses import dataclass


@dataclass
class Klass:
    pass


# BEGIN (write your solution here)
def to_Klass(dictionary):
    instance = Klass()
    for key, value in dictionary.items():
        setattr(instance, key, value)
    return instance
# END


# BEGIN reference solution
def to_Klass_ref(data):
    klass = Klass()
    for key, value in data.items():
        setattr(klass, key, value)
    return klass
# END reference solution
