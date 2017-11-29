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
    name_in_url = 'task_sum'
    players_per_group = 4
    task_timer = 60 #see Subsession, before_session_starts setting.
    num_rounds = 100 # must be more than the max one person can do in task_timer seconds

    INTS_T1 = [
        [51, 47, 11, 38, 74],
        [10, 36, 62, 71, 88],
        [32, 56, 35, 40, 98],
        [22, 34, 17, 44, 72],
        [83, 76, 86, 34, 90],
        [52, 50, 41, 74, 15],
        [87, 72, 96, 80, 92],
        [27, 68, 58, 65, 92],
        [51, 18, 87, 59, 54],
        [88, 67, 27, 65, 29],
        [47, 24, 77, 80, 80],
        [19, 38, 32, 65, 38],
        [77, 11, 23, 56, 75],
        [64, 65, 66, 69, 94],
        [16, 65, 91, 92, 51],
        [93, 58, 47, 57, 60],
        [64, 97, 74, 95, 73],
        [40, 34, 90, 27, 42],
        [26, 42, 23, 19, 57],
        [37, 90, 14, 36, 34],
        [75, 97, 46, 24, 35],
        [72, 79, 73, 87, 84],
        [14, 81, 70, 98, 94],
        [60, 56, 45, 78, 29],
        [35, 46, 92, 91, 36],
        [80, 10, 61, 13, 76],
        [90, 17, 48, 84, 20],
        [43, 46, 78, 45, 63],
        [50, 51, 33, 26, 79],
        [63, 86, 46, 15, 28],
        [82, 60, 96, 95, 21],
        [47, 76, 30, 97, 51],
        [73, 18, 62, 24, 75],
        [18, 96, 91, 49, 63],
        [91, 67, 55, 65, 54],
        [99, 63, 57, 80, 74],
        [44, 82, 63, 17, 65],
        [67, 98, 73, 70, 77],
        [36, 34, 52, 68, 81],
        [31, 31, 14, 44, 64],
        [20, 17, 42, 61, 98],
        [92, 82, 41, 25, 30],
        [60, 81, 57, 69, 25],
        [87, 52, 76, 22, 30],
        [20, 88, 45, 80, 62],
        [90, 74, 28, 59, 83],
        [34, 47, 77, 29, 53],
        [57, 31, 69, 62, 45],
        [28, 69, 92, 96, 34],
        [73, 17, 55, 76, 72],
        [33, 89, 85, 45, 31],
        [44, 49, 18, 31, 28],
        [69, 86, 18, 42, 68],
        [92, 45, 46, 97, 82],
        [75, 24, 97, 81, 79],
        [96, 77, 26, 60, 39],
        [34, 93, 57, 80, 42],
        [77, 46, 87, 59, 43],
        [39, 48, 39, 41, 48],
        [10, 93, 94, 66, 61],
        [14, 26, 62, 51, 25],
        [77, 38, 21, 41, 82],
        [68, 77, 25, 60, 21],
        [26, 32, 85, 23, 22],
        [98, 62, 83, 52, 20],
        [36, 14, 80, 14, 54],
        [37, 17, 39, 20, 70],
        [44, 43, 83, 92, 56],
        [86, 34, 79, 16, 84],
        [99, 60, 47, 25, 31],
        [53, 30, 17, 64, 10],
        [58, 91, 16, 42, 43],
        [96, 43, 65, 37, 90],
        [50, 13, 15, 73, 54],
        [82, 26, 99, 10, 99],
        [84, 38, 76, 54, 58],
        [70, 45, 58, 58, 87],
        [32, 83, 40, 76, 98],
        [35, 96, 14, 84, 98],
        [11, 50, 18, 77, 56],
        [30, 10, 33, 91, 66],
        [16, 21, 88, 63, 78],
        [92, 94, 68, 90, 78],
        [74, 78, 50, 79, 24],
        [79, 53, 56, 85, 98],
        [83, 32, 65, 70, 44],
        [26, 27, 19, 43, 31],
        [19, 95, 32, 22, 56],
        [81, 48, 73, 19, 77],
        [24, 37, 62, 73, 36],
        [62, 89, 64, 93, 55],
        [22, 60, 98, 21, 96],
        [95, 73, 29, 58, 49],
        [71, 69, 62, 91, 44],
        [73, 87, 92, 55, 99],
        [40, 46, 32, 10, 97],
        [58, 75, 56, 37, 83],
        [31, 47, 68, 89, 54],
        [14, 83, 26, 42, 77],
        [58, 83, 26, 94, 33],
        [14, 83, 12, 94, 22],
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
            p.int1 = Constants.INTS_T1[self.round_number - 1][0]
            p.int2 = Constants.INTS_T1[self.round_number - 1][1]
            p.int3 = Constants.INTS_T1[self.round_number - 1][2]
            p.int4 = Constants.INTS_T1[self.round_number - 1][3]
            p.int5 = Constants.INTS_T1[self.round_number - 1][4]
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



