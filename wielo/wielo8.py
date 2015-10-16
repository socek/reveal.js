class FirstMeta(type): pass
class SecondMeta(type): pass

class First(object, metaclass=FirstMeta): pass
class Second(object, metaclass=SecondMeta): pass

class ThirdMeta(FirstMeta, SecondMeta): pass

class Third(First, Second, metaclass=ThirdMeta): pass

