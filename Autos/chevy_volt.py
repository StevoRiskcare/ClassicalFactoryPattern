from Autos.abs_auto import AbsAuto


class ChevyVolt(AbsAuto):
    def start(self):
        print("Starting for {}".format(self.name))


    def stop(self):
        print("Stopping for {}".format(self.name))