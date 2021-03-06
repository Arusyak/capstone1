import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = False

ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# don't share this with anybody.
SECRET_KEY = '17apabcvsj2df0&z=i&*pg%6wv5w36pb9n%%%5_by8ro8$*r9l'

SENTRY_DSN = 'http://75193a0cc46d4243b073fdcfc6d42993:bff465d07bb144f5974bc49d3a3a0b8c@sentry.otree.org/265'

DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'AED'
USE_POINTS = False


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<p>
    <a href="http://www.otree.org/" target="_blank">oTree homepage</a>.
</p>
<p>
    <strong>Motherhood</strong> refers to Motherhood experiments 
</p>
"""

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': '...',
    'description': '...',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    # to use qualification requirements, you need to uncomment the 'qualification' import
    # at the top of this file.
    'qualification_requirements': [],
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.000,
    'participation_fee': 00.00,
    'doc': "otree real effort task",
    'mturk_hit_settings': mturk_hit_settings,
}


SESSION_CONFIGS = [
    {
        'name': 'experiment',
        'display_name': "The whole experiment",
        'num_demo_participants': 4,
        'app_sequence': [
            'intro', 'ret1', 'ret2', 'ret3', 'survey'
        ],
        'task_timer': 300,
        'showupfee': 30,
    },
    {
        'name': 'ret1',
        'display_name': "Real Effort Task - Adding Task",
        'num_demo_participants': 4,
        'app_sequence': [
           'intro', 'ret1',
        ],
        'task_timer': 120,
        'showupfee':30,
        },
    {
        'name': 'ret2',
        'display_name': "Real Effort Task 2 - Adding Task",
        'num_demo_participants': 4,
        'app_sequence': [
            'ret2', 'survey'
        ],
        'ret_timer': 60,
        'showupfee': 30,
    },
    {
        'name': 'ret3',
        'display_name': "Real Effort Task 3 - Adding Task",
        'num_demo_participants': 4,
        'app_sequence': [
            'ret2', 'ret3', 'survey'
        ],
        'task_timer': 300,
        'showupfee': 30,
    },
    {
        'name': 'survey',
        'display_name': "Survey",
        'num_demo_participants': 4,
        'app_sequence': [
            'survey',
        ],
        'ret_timer': 100,
        'showupfee': 30,
    },
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
