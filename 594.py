from setuptools import setup

setup(
        name= "myproject",
        packages=["myproject"]
        entry_points={"pytest11":["name_of_plugin = myproject.pluginmodule"]},
        classifiers = ["Framework::Pytest"]
        )
