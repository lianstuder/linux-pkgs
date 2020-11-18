import yaml, os

class ConfigLoader:
    def __init__(self, cfg_file):
        self.cfg_file = cfg_file
        self.packages = {}

    def load(self):
        with open(self.cfg_file, "r") as pkgs:
            self.packages = yaml.safe_load(pkgs)
        return self.packages


