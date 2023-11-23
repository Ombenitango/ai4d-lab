# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    # If you are changing from the default layout of your extension, you may
    # have to change the message extractors, you can read more about babel
    # message extraction at
    # http://babel.pocoo.org/docs/messages/#extraction-method-mapping-and-configuration
    entry_points='''
    [ckan.plugins]
    ai4dlab=ckanext.ai4dlab.plugin:Ai4DlabPlugin
    [paste.paster_command]
    initdb = ai4dlab.commands.initdb:InitDB
    ''',
    name='ai4dlab',
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
