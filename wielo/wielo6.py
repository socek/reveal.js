class Controller(object):

    def make(self):
        self.context['var'] = 1


class ControllerHtml(Controller, RenderHtml):
    pass

class RenderJson(Controller, RenderJson):
    pass

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
