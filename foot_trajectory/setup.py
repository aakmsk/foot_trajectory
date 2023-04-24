from setuptools import setup, find_packages

setup(
    name="foot-trajectory",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib"
    ],
    author="a_akmsk",
    author_email="",
    description="A foot trajectory generation library using various methods",
    license="MIT",
    keywords="robotics trajectory foot",
)
