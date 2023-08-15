# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

setup(
    name = "ckanext-template_ons",
    version = "0.0.1",
    description = "Template Dados Aberto ONS",
    long_description='',
    url = "https://github.com/ons/ckanext-template_ons",
    author = "ONS",
    author_email = "ons@ons.org.br",
    license = "AGPL",
    classifiers =[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
    ],
    namespace_packages=["ckanext"],
    packages=["ckanext.template_ons"],
    keywords = 'CKAN ONS Template Dados Abertos',
    include_package_data=True,
    zip_safe=False,
     entry_points='''
        [ckan.plugins]
        template_ons = ckanext.template_ons.plugin:TemplateOnsPlugin
        [babel.extractors]
        ckan = ckan.lib.extract:extract_ckan
    ''',
    # If you are changing from the default layout of your extension, you may
    # have to change the message extractors, you can read more about babel
    # message extraction at
    # http://babel.pocoo.org/docs/messages/#extraction-method-mapping-and-configuration
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
