__author__ = 'aelkikhia'

# -*- coding: utf-8 -*-exit
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='spotify-cloner',
    version='0.1',
    description='copy data a spotify account to another to escape facebook',
    author='Taz El-Kikhia',
    author_email='aelkikhia@gmail.com',
    tests_require=[
        "pep8",
        "mock",
        "nose",
        "nosexcover",
        "testtools"
    ],
    install_requires=["requests>=2.18.4,<3"],
    test_suite='nose.collector',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup'])
)