import pickle


CONFIG_PATH = "./config.dat"


class Config:
    def __init__(self):
        pass


def save_config(config):
    pickle.dump(config, open(CONFIG_PATH, "wb"))


def load_config():
    return pickle.load(open(CONFIG_PATH, "rb"))