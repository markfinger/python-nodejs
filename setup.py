from setuptools import setup, find_packages
import nodejs

setup(
    name='nodejs',
    version=nodejs.VERSION,
    packages=find_packages(exclude=('tests',)),
    description='Python bindings and utils for Node.js and io.js',
    long_description='Documentation at https://github.com/markfinger/python-nodejs',
    author='Mark Finger',
    author_email='markfinger@gmail.com',
    url='https://github.com/markfinger/python-nodejs',
)