from setuptools import setup

with open("./requirements.txt", "r") as reqs:
    requirements = reqs.read().splitlines()

with open("./README.md", "r") as rdme:
    ldesc = rdme.read()
    rdme.close()

setup(
    name="os-init",
    version="1.0.0",
    license="GNU General Public License v3.0",
    long_description=ldesc,
    author="Lian Studer",
    author_email="ln.studer@protonmail.ch",
    url="https://github.com/lianstuder/osinit",
    install_requires=requirements
)
