import pathlib
from setuptools import setup

here = pathlib.Path(__file__).parent
readme = (here / "README.md").read_text()
setup(
    name="factanal",
    version="0.1.0",
    description="A python wrapper for the R function factanal.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/kjul/factanalpy",
    author="Julian Kunschke",
    author_email="juliankunschke@yahoo.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8.2",
    ],
    packages=[],
    include_package_data=True,
    install_requires=["rpy2"],
)
