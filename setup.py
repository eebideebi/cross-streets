# Run with `python setup.py sdist bdist_wheel`
# Publish with `twine upload dist/*`

from setuptools import setup, find_packages

with open('README.md') as f:
    description = f.read()

setup(
    name='cross_streets',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
      'pydantic >= 2.12'  
    ],
    long_description=description,
    long_description_content_type='text/markdown'
)