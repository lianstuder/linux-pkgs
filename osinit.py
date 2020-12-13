import argparse
import platform
import yaml
import os
import subprocess
from tqdm import tqdm
import time


class Package:
    def __init__(self, pkg_name, pkg_version):
        self.pkg_name = pkg_name
        self.pkg_version = pkg_version

    def __str__(self):
        return "{}:{}".format(self.pkg_name, self.pkg_version)

    def install(self):
        if self.pkg_version == "latest":
            subprocess.call(f"pacman -Syy {self.pkg_name}", shell=True)
        else:
            subprocess.call(f"pacman -Syy {self.pkg_name}", shell=True)
        print(self.pkg_name, self.pkg_version)


class Config:
    def __init__(self, cfg_file):
        self.cfg_file = cfg_file
        self.packages = {}

    def load(self):
        with open(self.cfg_file, "r") as pkgs:
            self.packages = yaml.safe_load(pkgs)
        return self.packages


if platform.system() != "Linux":
    print("Not compatible with your OS. This command line utility is for Linux only.")
    quit()

parser = argparse.ArgumentParser(
    description="osinit - Arch Linux Setup Utility")
parser.add_argument("-c", "--config", dest="pkgconfig",
                    default="~/.config/osinit/packages.yml")

args = parser.parse_args()

config = Config(args.pkgconfig).load()

print(f"Installing {len(config)} packages: ")

for i in tqdm(range(len(config)),
              desc="Installing...",
              ncols=69):
    package = pkg_list[i]
    package_version = package["version"]
    package_name = package["name"]
    package = Package(package_name, package_version).install()

    print("\nInstallation complete.\n\n")
