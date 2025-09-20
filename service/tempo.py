class MyClass:

    def __init__(self, attr1, attr2, attr3):
        self.attr_1 = attr1
        self.attr_2 = attr2
        self.attr_3 = attr3

    def get_attr_1(self):
        return self.attr_1

    def set_attr_1(self, value):
        self.attr_1 = value


obj_1 = MyClass(attr1=1.1, attr2=2.1, attr3=3.1)
obj_2 = MyClass(attr1=1.2, attr2=2.2, attr3=3.2)
obj_3 = MyClass(attr1=1.3, attr2=2.3, attr3=3.3)

obj_dict = {
    '1': obj_1.__dict__,
    '2': obj_2.__dict__,
    '3': obj_3.__dict__,

}

print(MyClass.get_attr_1(obj_2))

def dict_save():
    attr_dict = {
        'attr_1': MyClass.get_attr_1,
    }
