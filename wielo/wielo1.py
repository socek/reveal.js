class Dziadek(object):
    pass

class Ciocia(Dziadek):
    pass

class Wujek(Ciocia):
    pass

class Mama(Dziadek):
    pass

class Tata(Mama):
    pass

class Dziecko(Wujek, Tata):
    pass

help(Dziecko)
