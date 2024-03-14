from Autos.abs_auto import AbsAuto


class NullCar(AbsAuto):
    def start(self):
        print("Nothing for {}".format(self.name))

    def stop(self):
        pass