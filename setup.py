from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ascii-art-tool",
    version="4.0.0",
    author="MeFocus",
    author_email="pishvarimani2@gmail.com",
    description="A powerful ASCII art generator with multiple fonts, colors, and animations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MeFocus/ascii-art-tool",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)