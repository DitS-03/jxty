from setuptools import setup, find_packages

setup(
    name="jxty",
    version="0.0.1",
    istall_requires=["pyyaml", "xmltodict", "dicttoxml", "toml"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "jxty = jxty.cmd:main"
        ]
    }
)

 