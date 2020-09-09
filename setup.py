from setuptools import setup, find_packages
import warnings


with open('README.rst') as f:
    README = f.read()

setup(
    name='howtopackage',
    version='v0.0.1',
    url='',
    license='MIT',
    author='Andreas Philippi',
    author_email='',
    description='Dummy package',
    long_description=README,
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=['PuLP>=2.0', 'numpy>=1.18.2'],
)
