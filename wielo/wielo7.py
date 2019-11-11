from copy import deepcopy


class Original(object):

    def __init__(self):
        self._hidden = 10


class MyOriginal(Original):

    def __init__(self, original):
        self.__dict__ = deepcopy(original.__dict__)

print(MyOriginal(Original())._hidden)
