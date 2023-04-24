from setuptools import setup, find_packages

setup(
    name="foot-trajectory",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A foot trajectory generation library using various methods",
    license="MIT",
    keywords="robotics trajectory foot",
)