from setuptools import setup

setup(
    name='favorites',
    version='1.0',
    py_modules=['favorites'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        favorites=favorites:cli
    ''',
)