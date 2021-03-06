class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("singleton called...")
        if cls not in cls._instances.keys():
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
