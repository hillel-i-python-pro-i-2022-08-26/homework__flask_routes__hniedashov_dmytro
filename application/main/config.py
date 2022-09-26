class Config:
    DEBUG: bool = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


configurations: dict[str, type[Config]] = dict(dev=DevelopmentConfig, prod=ProductionConfig)
