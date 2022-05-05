import os
import sys

from setuptools import setup


current_path = os.path.abspath(os.path.dirname(__file__))

with open("requirements.txt","r") as file:
    requirement = file.readlines()




setup(
    name="hasura_demo",
    version="0.1.0",
    author_email="abhai.katiyar@srijan.net",
    author="srijan",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Natural Language :: English",
    ],
    install_requires=requirement,
    packages=["hasura_demo"],
    package_dir={"":"src"},
    python_requires=">=3.9"

)
