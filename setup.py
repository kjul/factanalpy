import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent
readme = (here / "readme.md").read_text()
setup(
    name="factanal",
    version="0.1.8",
    description="A python wrapper for the R function factanal.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/kjul/factanalpy",
    author="kjul",
    author_email="juliankunschke@yahoo.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["rpy2"],
)
