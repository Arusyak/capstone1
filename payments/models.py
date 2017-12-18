from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    showup_Fee = 30
    name_in_url = 'payments'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):

    def before_session_starts(self):
        for p in self.get_players():
            p.payoff = 0
            if 'showupfee' in self.session.config:
                p.showupfee = self.session.config['showupfee']
            else:
                p.showupfee = Constants.showup_Fee


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

    task_1_score = models.PositiveIntegerField(
        doc='subject score in task 1')

    task_2_score = models.PositiveIntegerField(
        doc='subject score on task 2, num task correct')
    op_scores = models.CharField(
        doc='this subjects opposing player scores from task 2. also used in task 3')
    op_top_score = models.PositiveIntegerField(
        doc='the top score this player faced')
    task_2_final_score = models.PositiveIntegerField(
        doc='subject final score, after comparision')

    payment_method_selection = models.CharField(
        doc='subjects payment method selection, individual or comparision')
    task_3_score = models.PositiveIntegerField(
        doc='subject score on task 3, num tasks correct')
    task_3_final_score = models.PositiveIntegerField(
        doc='subjects final score on task 3. if subject chose comparison, score after . otherwise individual score')

    task_4_payment = models.CharField(
        doc='the task randomly selected for payment. task 1, 2 or 3')
    final_task_earnings = models.FloatField(
        doc='earnings from the task randomly selected, before showup fee and risk aversion score')

    risk_aversion_score = models.PositiveIntegerField(
        doc='the risk aversion score from survey')

    showup_Fee = models.FloatField(
        doc='showup fee')
    final_earnings = models.FloatField(
        doc='final earnings, in currency. including task earnings and showup fee, before charity')
