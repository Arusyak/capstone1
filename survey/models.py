from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q_rank = models.CharField(
            initial=None,
            choices=['1','2','3','4'],
            verbose_name='',
            doc='What do you think was your rank within your Task 2 group in terms of sums solved correctly? Please choose a number from 1 (meaning you gave the most correct answers in your group) to 4 (meaning you gave the least correct answers in your group).',
            widget=widgets.RadioSelect())

    q_riskaversion = models.CharField(
            initial=None,
            choices=['8 AED for certain','12 AED or 6 AED with a 50% chance','16 AED or 4 AED with a 50% chance','20 AED or 2 AED with a 50% chance', '24 AED or 0 AED with a 50% chance'],
            verbose_name='',
            doc='Please pick one of the following.',
            widget=widgets.RadioSelect())

    q_riskpreference = models.CharField(
            initial=None,
            choices=['1','2','3','4','5','6','7','8','9','10'],
            verbose_name='',
            doc='Are you generally a person who is fully prepared to take risks or do you try to avoid taking risks?',
            widget=widgets.RadioSelect())

    q_mathlevel = models.CharField(
            initial=None,
            choices=[
            'Pre-Calculus', 'Calculus','Mutivariable calculus','Beyond multivariable calculus'
            ],
            verbose_name='',
            doc='What is the highest mathematics level you have taken thus far?',
            widget=widgets.RadioSelect())

    q_majordeclarationYN = models.CharField(
        initial=None,
        choices=[
        '1',
        '0'
        ],
        verbose_name='',
        doc='Have you declared your major?',
        widget=widgets.RadioSelect())
