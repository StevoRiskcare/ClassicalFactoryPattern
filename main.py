import loader

for factory_name in "chevy_factory", "mazda", "bmw_factory":
    factory = loader.load_factory(factory_name)
    car = factory.create_auto()
    car.start()
    car.stop()