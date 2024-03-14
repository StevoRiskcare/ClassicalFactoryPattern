from Autos import BMW
from factories.abs_factory import AbsFactory


class BMWFactory(AbsFactory):
    def create_auto(self):
        self.bmw = bmw = BMW()
        bmw.name = "BMWFactory"
        return bmw
