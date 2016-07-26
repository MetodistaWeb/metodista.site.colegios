# -*- coding:utf-8 -*-
from setuptools import find_packages
from setuptools import setup
import os

version = '20151214.02.dev0'
long_description = (open("README.txt").read() + "\n" +
                    open(os.path.join("docs", "INSTALL.txt")).read() + "\n" +
                    open(os.path.join("docs", "CREDITS.txt")).read() + "\n" +
                    open(os.path.join("docs", "HISTORY.txt")).read())

setup(name='metodista.site.colegios',
      version=version,
      description="Configuracao dos portais de colégios",
      long_description=long_description,
      classifiers=[
          "Development Status :: 1 - Alpha",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
          "Intended Audience :: Developers",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: JavaScript",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary",
          "Topic :: Multimedia",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='metodista colegios plone4.3',
      author='Danilo Sartorelli Barbato',
      author_email='danilo.barbato@metodista.br',
      url='http://metodista.br',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['metodista', 'metodista.site'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Pillow',
          'Plone',
          'collective.cover',
          'collective.polls',
          'collective.upload',
          'Products.PloneFormGen',
          'plone.app.contenttypes',
          'plone.app.event',
          'sc.banner',
          'sc.social.like',
          'sc.microsite',
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
