from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class Rank(Page):
    form_model = models.Player
    form_fields= ['q_rank']


class RiskAversion(Page):
    form_model = models.Player
    form_fields = ['q_riskaversion']

class RiskPreference(Page):
    form_model=models.Player
    form_fields = ['q_riskpreference']

class MathLevel(Page):
    form_model=models.Player
    form_fields = ['q_mathlevel']

class Results(Page):
    pass


page_sequence = [
    Rank,
    RiskAversion,
    RiskPreference,
    ResultsWaitPage,
    Results
]
