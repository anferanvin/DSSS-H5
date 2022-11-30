from setuptools import setup, find_packages

setup(
      name='snowflake',
      version='1.0',
      description='Python Distribution Utilities',
      author='DSSS - Andrey Arango',
      author_email='andrey.arango@fau.de',
      packages=find_packages(),
      install_requires=["numpy", "turtles"],
)