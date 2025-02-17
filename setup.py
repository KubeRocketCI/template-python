"""Setup file for application."""
from setuptools import find_packages, setup
from setuptools import Command
from version import __version__


class VersionCommand(Command):
    """Custom command to print the version."""
    description = "print the version"
    user_options = []

    def initialize_options(self):
        """Override default one if needed"""

    def finalize_options(self):
        """Override default one if needed"""

    def run(self):
        """Custom function to print the version"""
        print(__version__)


def read_requirements():
    """Reads dependencies from requirements.txt file."""
    try:
        with open("requirements.txt", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


setup(
    name="hello_world",
    version=__version__,
    cmdclass={"version": VersionCommand},
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=read_requirements(),
)
