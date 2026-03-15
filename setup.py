# Run with `python setup.py sdist bdist_wheel`
# Publish with `twine upload dist/*`

from setuptools import setup, find_packages

with open('README.md') as f:
    description = f.read()

setup(
    name='cross_streets',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
      'pydantic == 2.12',
      'OSMPythonTools == 0.3.6',
      'usaddress == 0.5.16',
      'rapidfuzz == 3.14.3'
    ],
    long_description=description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    package_data={
        "cross_streets": ["wikipedia_street_types.txt"],
    },
)