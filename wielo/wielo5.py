class Rodzic(object):

    def metoda(self):
        print('Rodzic')


class Dziecko(Rodzic):

    def metoda(self):
        super().metoda()
        print('Dziecko')


class MockedDziecko(Rodzic):

    def metoda(self):
        print('Mock!')


class ExampleDziecko(Dziecko, MockedDziecko):

    def metoda(self):
        super().metoda()
        print('Example!')

Dziecko().metoda()
print('---')
ExampleDziecko().metoda()
