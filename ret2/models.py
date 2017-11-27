# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random




# </standard imports>



author = 'Curtis Kephart (economicurtis@gmail.com)'

doc = """
Real Effort Task. Add as many ints as possible.  
"""

class Constants(BaseConstants):
    name_in_url = 'task_sum2'
    players_per_group = 4
    task_timer = 300 #see Subsession, before_session_starts setting.
    num_rounds = 60 # must be more than the max one person can do in task_timer seconds

    INTS_T2 = [
        [42, 19, 90, 51, 92],
        [88, 84, 24, 50, 39],
        [37, 15, 72, 43, 68],
        [54, 88, 64, 29, 20],
        [71, 54, 73, 91, 45],
        [30, 80, 79, 36, 12],
        [53, 33, 65, 36, 29],
        [50, 99, 74, 24, 53],
        [22, 80, 21, 64, 49],
        [57, 62, 67, 84, 21],
        [18, 33, 57, 91, 52],
        [59, 69, 91, 90, 46],
        [68, 83, 59, 68, 46],
        [67, 41, 10, 20, 99],
        [31, 83, 45, 68, 77],
        [94, 38, 86, 55, 91],
        [54, 57, 82, 27, 48],
        [25, 62, 51, 97, 11],
        [30, 40, 16, 25, 68],
        [59, 84, 91, 79, 36],
        [22, 37, 70, 48, 38],
        [62, 15, 58, 89, 64],
        [47, 92, 38, 13, 52],
        [37, 11, 64, 78, 34],
        [11, 52, 66, 87, 77],
        [83, 16, 55, 92, 86],
        [98, 63, 32, 64, 43],
        [96, 12, 72, 36, 24],
        [64, 64, 19, 48, 70],
        [72, 62, 75, 59, 57],
        [34, 90, 46, 96, 54],
        [89, 64, 82, 40, 53],
        [40, 38, 17, 29, 13],
        [44, 27, 82, 52, 89],
        [59, 51, 63, 81, 46],
        [97, 12, 86, 84, 99],
        [32, 23, 58, 13, 69],
        [54, 70, 45, 52, 56],
        [77, 43, 34, 32, 88],
        [95, 23, 11, 37, 31],
        [32, 19, 18, 20, 60],
        [22, 85, 49, 25, 34],
        [63, 93, 82, 52, 64],
        [83, 78, 88, 61, 30],
        [16, 39, 45, 73, 78],
        [42, 68, 93, 74, 88],
        [70, 39, 54, 59, 62],
        [93, 45, 47, 86, 69],
        [78, 11, 47, 60, 76],
        [22, 33, 60, 64, 42],
        [26, 27, 47, 55, 59],
        [79, 86, 19, 14, 12],
        [46, 13, 33, 33, 70],
        [56, 53, 40, 16, 21],
        [40, 16, 13, 49, 54],
        [71, 79, 47, 63, 18],
        [30, 43, 50, 96, 36],
        [40, 76, 40, 38, 60],
        [73, 29, 51, 37, 48],
        [81, 78, 64, 82, 78],
        [68, 62, 50, 40, 73],
        [25, 92, 20, 63, 99],
        [88, 37, 78, 59, 79],
        [28, 78, 36, 38, 77],
        [81, 55, 81, 37, 33],
        [70, 88, 66, 97, 98],
        [95, 71, 72, 67, 43],
        [87, 84, 77, 34, 24],
        [99, 89, 19, 27, 36],
        [18, 20, 62, 95, 76],
    ]


class Subsession(BaseSubsession):

    def before_session_starts(self):

        players = self.get_players()
        if 'task_timer' in self.session.config:
            task_timer = self.session.config['task_timer']
        else:
            task_timer = Constants.task_timer

        for p in self.get_players():
            p.task_timer = task_timer
            p.int1 = Constants.INTS_T2[self.round_number-1][0]
            p.int2 = Constants.INTS_T2[self.round_number-1][1]
            p.int3 = Constants.INTS_T2[self.round_number-1][2]
            p.int4 = Constants.INTS_T2[self.round_number-1][3]
            p.int5 = Constants.INTS_T2[self.round_number-1][4]
            p.solution = p.int1 + p.int2 + p.int3 + p.int4 + p.int5

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    def score_round(self):
        # update player payoffs
        if (self.solution == self.user_total):
            self.is_correct = True
            self.payoff_score = 1
        else:
            self.is_correct = False
            self.payoff_score = c(0)



    task_timer = models.PositiveIntegerField(
        doc="""The length of the real effort task timer."""
    )

    int1 = models.PositiveIntegerField(
        doc="this round's first int")

    int2 = models.PositiveIntegerField(
        doc="this round's second int")

    int3 = models.PositiveIntegerField(
        doc="this round's third int")

    int4 = models.PositiveIntegerField(
        doc="this round's fourth int")

    int5 = models.PositiveIntegerField(
        doc="this round's fifth int")

    solution = models.PositiveIntegerField(
        doc="this round's correct summation")

    user_total = models.PositiveIntegerField(
        min = 1,
        max = 9999,
        doc="user's summation",
        widget=widgets.TextInput(attrs={'autocomplete':'off'}))

    is_correct = models.BooleanField(
        doc="did the user get the task correct?")

    payoff_score = models.FloatField(
            doc = '''score in this task'''
        )

