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

    def vars_for_template(self):
        return {
            "risk aversion result":self.player.riskaversion_score()
        }


class MathLevel(Page):
    form_model=models.Player
    form_fields = ['q_mathlevel', 'q_GPA_highschool', 'q_GPA_highschool_max']


class MajorDeclarationYN(Page):
    form_model=models.Player

    form_fields = ['q_majordeclarationYN']


class ExpectedStudyTrack(Page):
    form_model=models.Player
    form_fields = ['q_expectedstudytrack_AH',
                   'q_expectedstudytrack_EG',
                   'q_expectedstudytrack_MD',
                   'q_expectedstudytrack_SC',
                   'q_expectedstudytrack_SS']
    def is_displayed(self):
        return self.player.q_majordeclarationYN == "No"

    # def error_message(self):

    #         return 'Please select only one or two choices'


class DeclaredStudyTrack(Page):
    form_model=models.Player
    form_fields = ['q_declaredstudytrack_AH',
                   'q_declaredstudytrack_EG',
                   'q_declaredstudytrack_MD',
                   'q_declaredstudytrack_SC',
                   'q_declaredstudytrack_SS']
    def is_displayed(self):
        return self.player.q_majordeclarationYN == "Yes"


class GPAStudyTrack(Page):
    form_model=models.Player
    form_fields = ['q_gpastudytrack_AH',
                   'q_gpastudytrack_EG',
                   'q_gpastudytrack_MD',
                   'q_gpastudytrack_SC',
                   'q_gpastudytrack_SS']

    def error_message(self, values):
        if values['q_gpastudytrack_AH'] + values['q_gpastudytrack_EG']+values['q_gpastudytrack_MD'] + values['q_gpastudytrack_SC']+ values['q_gpastudytrack_SS'] !=15:
            return 'Please select each rank only once'



class ProfitableStudyTrack(Page):
    form_model=models.Player
    form_fields = ['q_profitablestudytrack_AH',
                   'q_profitablestudytrack_EG',
                   'q_profitablestudytrack_MD',
                   'q_profitablestudytrack_SC',
                   'q_profitablestudytrack_SS']

    def error_message(self, values):
        if values['q_profitablestudytrack_AH'] + values['q_profitablestudytrack_EG']+values['q_profitablestudytrack_MD'] + values['q_profitablestudytrack_SC']+ values['q_profitablestudytrack_SS'] !=15:
            return 'Please select each rank only once'

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

    def before_next_page(self):
        pass


class Results(Page):
    def vars_for_template(self):
        return {
            "risk aversion result":self.player.riskaversion_score()
        }


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
