import os
from setuptools import setup

# Utility function to cat in a file (used for the README)
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "yotta",
    version = "0.0.1",
    author = "James Crosby",
    author_email = "James.Crosby@arm.com",
    description = ("Package management for embedded modules."),
    license = "Proprietary",
    keywords = "embedded package module dependency management",
    url = "about:blank",
    packages=['yotta', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: Proprietary",
        "Environment :: Console",
    ],
)