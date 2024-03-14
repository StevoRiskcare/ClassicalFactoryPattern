from Autos.null_car import NullCar
from factories.abs_factory import AbsFactory


class NullFactory(AbsFactory):
    def create_auto(self):
        self.nullfactory = nullfactory = NullCar()
        nullfactory.name = "this model"
        return nullfactory