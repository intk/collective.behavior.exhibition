from setuptools import find_packages
from setuptools import setup

import os


long_description = (
    open(os.path.join("src", "collective", "behavior", "exhibition", "docs", "README.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "behavior", "exhibition", "docs", "HISTORY.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "behavior", "exhibition", "docs", "CONTRIBUTORS.rst")).read())


setup(
    name='collective.behavior.exhibition',
    version='0.1',
    description="Provides fields tipically used by museum exhibitions for dexterity content types.",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone Museum',
    author='Andre Goncalves',
    author_email='andre@intk.com',
    url='https://github.com/collective/collective.behavior.exhibition/',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['collective', 'collective.behavior'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'plone.behavior',
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
