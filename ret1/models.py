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
    task_timer = 300 #see Subsession, before_session_starts setting.
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
        [14, 83, 26, 94, 69],
        [82, 99, 70, 61, 54],
        [64, 56, 83, 93, 99],
        [61, 34, 41, 37, 37],
        [28, 51, 92, 44, 11],
        [77, 14, 95, 57, 66],
        [50, 94, 28, 96, 60],
        [30, 69, 71, 21, 18],
        [82, 83, 24, 97, 64],
        [11, 70, 26, 35, 95],
        [32, 12, 96, 65, 70],
        [32, 64, 76, 41, 56],
        [23, 20, 48, 90, 79],
        [10, 48, 91, 93, 13],
        [78, 51, 50, 24, 67],
        [18, 53, 95, 38, 36],
        [82, 25, 95, 66, 85],
        [75, 46, 91, 71, 88],
        [38, 39, 81, 95, 27],
        [40, 70, 99, 43, 53],
        [29, 56, 96, 45, 31],
        [66, 75, 19, 79, 47],
        [94, 99, 25, 22, 32],
        [67, 35, 10, 70, 79],
        [46, 60, 97, 23, 27],
        [50, 11, 82, 58, 46],
        [36, 57, 22, 74, 87],
        [40, 55, 38, 43, 68],
        [28, 95, 59, 83, 21],
        [53, 61, 62, 91, 36],
        [63, 64, 81, 65, 23],
        [81, 16, 98, 45, 24],
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



