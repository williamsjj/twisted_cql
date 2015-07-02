#!/usr/bin/python
####################################################################
# FILENAME: setup.py
# PROJECT: twisted_cql
# DESCRIPTION: Install Twisted CQL client 
#              (thin wrapper around Datastax cassandra-driver client.)
# 
#               Requires: Twisted >= 15.0.0
#                         cassandra-driver >= 2.6.0
#
####################################################################
# (C)2015 DigiTar Inc., All Rights Reserved
# Licensed under BSD license. See LICENSE file.
####################################################################

from setuptools import setup, find_packages
 
version = '0.5.1'
 
setup(name='twisted_cql',
      version=version,
      description="Twisted",
      long_description="""Shiji makes it easy to build HTTP & RESTful APIs using Twisted Web.""",
      classifiers=[],
      keywords='twisted,cql,cassandra,datastax',
      author='DigiTar',
      author_email='support@digitar.com',
      url='https://github.com/williamsjj/twisted_cql',
      license='BSD Simplified',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests', 'old*']),
      zip_safe=False,
      install_requires=["Twisted>=15.0",
                        "cassandra-driver>=2.6.0"]
    )
