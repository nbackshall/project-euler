"""Setup.py"""
import setuptools

core_requirements = [
    "numpy",
]

setuptools.setup(
    version="0.0.1",
    name="euler-project",
    author="Nicholas Backshall",
    author_email="nicholas.backshall@gmail.com",
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    install_requires=core_requirements,
)
