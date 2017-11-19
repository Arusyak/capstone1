from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        # yield (views.Rank)
        yield (views.RiskAversion)
        # yield (views.RiskPreference)
        # yield (views.MathLevel)
        # yield (views.MajorDeclarationYN)
        # yield (views.ExpectedStudyTrack)
        # yield (views.DeclaredStudyTrack)
        # yield (views.GPAStudyTrack)
        # yield (views.ProfitableStudyTrack)
        # yield (views.MathLevelNYUAD)
        # yield (views.PassingGradeMath)
        # yield (views.Wealth)
        # yield (views.Statements1)
        # yield (views.Statements2)
        yield (views.ResultsWaitPage)
        yield (views.Results)