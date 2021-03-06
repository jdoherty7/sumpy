#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

ver_dic = {}
version_file = open("sumpy/version.py")
try:
    version_file_contents = version_file.read()
finally:
    version_file.close()

exec(compile(version_file_contents, "sumpy/version.py", 'exec'), ver_dic)

setup(name="sumpy",
      version=ver_dic["VERSION_TEXT"],
      description="Fast summation in Python",
      long_description="""
      Code-generating FMM etc.
      """,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Other Audience',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Scientific/Engineering :: Visualization',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities',
          ],

      author="Andreas Kloeckner",
      author_email="inform@tiker.net",
      license="MIT",
      packages=["sumpy", "sumpy.expansion"],

      install_requires=[
          "loo.py>=2017.2",
          "pytools>=2017.6",
          "boxtree>=2013.1",
          "pytest>=2.3",
          "six",

          # If this causes issues, see:
          # https://code.google.com/p/sympy/issues/detail?id=3874
          "sympy>=0.7.2",
          ])
