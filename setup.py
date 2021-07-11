import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'distnav',
    version = '0.0.1',
    author = 'Muchen Sun',
    description = 'DistNav crowd navigation toolbox',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    install_requires = ['numpy', 'numba'],
    url = 'https://github.com/MurpheyLab/DistNav',
    packages = setuptools.find_packages(),
    python_requires = '>=3.6'
)
