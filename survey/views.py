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


class MajorDeclarationYN(Page):
    form_model=models.Player

    form_fields = ['q_majordeclarationYN']


class ExpectedStudyTrack(Page):
    form_model=models.Player
    form_fields = ['q_expectedstudytrack']

    def is_displayed(self):
        return self.player.q_majordeclarationYN == "No"


class DeclaredStudyTrack(Page):
    form_model=models.Player
    form_fields = ['q_declaredstudytrack']

    def is_displayed(self):
        return self.player.q_majordeclarationYN == "Yes"


class GPAStudyTrack(Page):
    form_model=models.Player
    form_fields = ['q_gpastudytrack']


class ProfitableStudyTrack(Page):
    form_model=models.Player
    form_fields = ['q_profitablestudytrack']


class MathLevelNYUAD(Page):
    form_model=models.Player
    form_fields = ['q_mathlevelnyuad']


class PassingGradeMath(Page):
    form_model=models.Player
    form_fields = ['q_passinggrade']


class Wealth(Page):
    form_model=models.Player
    form_fields = ['q_wealth']


class Statements1(Page):
    form_model = models.Player

    form_fields = [
        'q_CT_publicsector',
        'q_CT_familyimportance',
        'q_CT_wagevshours',
        'q_CT_incomecontribution',
    ]


class Statements2(Page):
    form_model = models.Player

    form_fields = [
        'q_CT_jobwomenindependence',
        'q_CT_workingmother',
        'q_CT_fatherSuited',
        'q_CT_preschoolWork',
    ]


class Results(Page):
    pass


page_sequence = [
    Rank,
    RiskAversion,
    RiskPreference,
    MathLevel,
    MajorDeclarationYN,
    ExpectedStudyTrack,
    DeclaredStudyTrack,
    GPAStudyTrack,
    ProfitableStudyTrack,
    MathLevelNYUAD,
    PassingGradeMath,
    Wealth,
    Statements1,
    Statements2,
    ResultsWaitPage,
    Results
]
