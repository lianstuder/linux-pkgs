from archinit.cfg_loader import ConfigLoader
import argparse

parser = argparse.ArgumentParser(description="ArchInit - Arch Linux Setup Utility")
parser.add_argument("-c", "--config", dest="pkgconfig", default="~/.config/archinit/packages.yml")
parser.add_argument("-p", "--packages", dest="pkgs", default="all")

args = parser.parse_args()

cfg_loader = ConfigLoader(args.pkgconfig).load()
print(cfg_loader)
