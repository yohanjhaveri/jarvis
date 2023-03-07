from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = "jarvis-chat",
    version = "0.1.2",
    author = "Yohan Jhaveri",
    author_email = "yohanjhaveri@gmail.com",
    license = "MIT",
    description = "A simple CLI tool for interacting with ChatGPT",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/yohanjhaveri/jarvis",
    py_modules = ["jarvis", "app"],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = """""""""
        [console_scripts]
        jarvis=jarvis:main
    """
)