from setuptools import setup, find_packages

setup(
    name='EvenList',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Anup Timsina',
    author_email='timsinaanup23@gmail.com',
    description='Returns a list of even numbers from a given list',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)