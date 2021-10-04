from setuptools import setup

setup(
    name='PineIDE',
    version='0.0.0',
    packages=['pineide'],
    url='https://github.com/GrandMoff100/PineIDE',
    license='GNU',
    author='GrandMoff100',
    author_email='nlarsen23.student@gmail.com',
    description='An interactive Python IDE in your terminal',
    install_requires=['textual', 'click', 'rich'],
    entry_points={
        'console_scripts': ['pine = pineide.cli:cli']
    }
)
