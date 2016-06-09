from setuptools import setup
import os.path

setup(
    name='md2reveal',
    version='0.0.1',
    author='Lirian Su',
    author_email='liriansu@gmail.com',
    url='https://github.com/LKI/md2reveal',
    license='WTFPL',
    description='Converting markdown to reveal.js html page',
    long_description=open('README.rst').read(),
    entry_points={
        'console_scripts': ['md2reveal = md2reveal.cmdline:execute']
    },
    packages=['md2reveal'],
)
