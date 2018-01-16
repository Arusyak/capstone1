import random

from otree.api import Currency as c, currency_range

import settings
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Rank(Page):
    form_model = models.Player
    form_fields = ['q_rank']


class RiskAversion(Page):
    form_model = models.Player
    form_fields = ['q_riskaversion']


class RiskPreference(Page):
    form_model = models.Player
    form_fields = ['q_riskpreference']

    def vars_for_template(self):
        return {
            'risk_aversion_score':self.player.risk_aversion_score()
        }


class MathLevel(Page):
    form_model = models.Player
    form_fields = ['q_mathplacement', 'q_mathlevel', 'q_GPA_highschool', 'q_GPA_highschool_max']

    def error_message(self, values):
        if values['q_GPA_highschool'] != str and values['q_GPA_highschool_max'] != str:
            if values['q_GPA_highschool'] > values['q_GPA_highschool_max']:
                return 'Your GPA must not exceed the maximum possible GPA.'
        elif values['q_GPA_highschool'] == str:
            return 'Please enter a valid value.'
        elif values['q_GPA_highschool_max'] == str:
            return 'Please enter a valid value.'


class MajorDeclarationYN(Page):
    form_model = models.Player

    form_fields = ['q_majordeclarationYN']


class ExpectedStudyTrack(Page):
    form_model = models.Player
    form_fields = ['q_expectedstudytrack_AH',
                   'q_expectedstudytrack_EG',
                   'q_expectedstudytrack_MD',
                   'q_expectedstudytrack_SC',
                   'q_expectedstudytrack_SS']

    def is_displayed(self):
        return self.player.q_majordeclarationYN == "No"

    def error_message(self, values):
        if values['q_expectedstudytrack_AH'] + values['q_expectedstudytrack_EG'] + values['q_expectedstudytrack_MD'] \
                + values['q_expectedstudytrack_SC'] + values['q_expectedstudytrack_SS'] > 2:
            return 'You may not check more than two academic divisions.'


class DeclaredStudyTrack(Page):
    form_model = models.Player
    form_fields = ['q_declaredstudytrack_AH',
                   'q_declaredstudytrack_EG',
                   'q_declaredstudytrack_MD',
                   'q_declaredstudytrack_SC',
                   'q_declaredstudytrack_SS']

    def is_displayed(self):
        return self.player.q_majordeclarationYN == "Yes"

    def error_message(self, values):
        if values['q_declaredstudytrack_AH'] + values['q_declaredstudytrack_EG'] + values['q_declaredstudytrack_MD'] \
                + values['q_declaredstudytrack_SC'] + values['q_declaredstudytrack_SS'] > 2:
            return 'You may not check more than two academic divisions.'


class GPAStudyTrack(Page):
    form_model = models.Player
    form_fields = ['q_gpastudytrack_AH',
                   'q_gpastudytrack_EG',
                   'q_gpastudytrack_MD',
                   'q_gpastudytrack_SC',
                   'q_gpastudytrack_SS']

    def error_message(self, values):
        if values['q_gpastudytrack_AH'] + values['q_gpastudytrack_EG'] + values['q_gpastudytrack_MD'] \
                + values['q_gpastudytrack_SC'] + values['q_gpastudytrack_SS'] != 15:
            return 'Please select each rank only once'
        if values['q_gpastudytrack_AH'] == values['q_gpastudytrack_EG'] == values['q_gpastudytrack_MD'] \
                == values['q_gpastudytrack_SC'] == values['q_gpastudytrack_SS'] == 3:
            return 'Please select each rank only once'
        if values['q_gpastudytrack_AH'] != 1 and values['q_gpastudytrack_EG'] != 1 \
                and values['q_gpastudytrack_MD'] != 1 and values['q_gpastudytrack_SC'] != 1 \
                and values['q_gpastudytrack_SS'] != 1:
            return 'Please select each rank only once'


class ProfitableStudyTrack(Page):
    form_model = models.Player
    form_fields = ['q_profitablestudytrack_AH',
                   'q_profitablestudytrack_EG',
                   'q_profitablestudytrack_MD',
                   'q_profitablestudytrack_SC',
                   'q_profitablestudytrack_SS']

    def error_message(self, values):
        if values['q_profitablestudytrack_AH'] + values['q_profitablestudytrack_EG'] \
                + values['q_profitablestudytrack_MD'] + values['q_profitablestudytrack_SC'] \
                + values['q_profitablestudytrack_SS'] != 15:
            return 'Please select each rank only once'
        if values['q_profitablestudytrack_AH'] == values['q_profitablestudytrack_EG'] \
                == values['q_profitablestudytrack_MD'] == values['q_profitablestudytrack_SC'] \
                == values['q_profitablestudytrack_SS']:
            return 'Please select each rank only once'
        if values['q_profitablestudytrack_AH'] != 1 and values['q_profitablestudytrack_EG'] != 1 \
                and values['q_profitablestudytrack_MD'] != 1 and values['q_profitablestudytrack_SC'] != 1 \
                and values['q_profitablestudytrack_SS'] != 1:
            return 'Please select each rank only once'


class MathLevelNYUAD(Page):
    form_model = models.Player
    form_fields = ['q_mathlevelnyuad']


class PassingGradeMath(Page):
    form_model = models.Player
    form_fields = ['q_passinggrade']


class Wealth(Page):
    form_model = models.Player
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
            'risk_aversion_score':self.player.risk_aversion_score()
        }


class HoldOn(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):

        # ############ task 1 #####################################################################################
        #  retrieve task 1 score
        if 'task_1_score' in self.participant.vars:  # just error handling
            task_1_score = self.participant.vars['task_1_score']
        else:
            task_1_score = 6901

        # retrive other player's scores from task 2
        # just error handling, if op_scores are None, say in testing
        if 'task_2_op_scores' in self.participant.vars:
            op_scores = self.participant.vars['task_2_op_scores']
        else:
            op_scores = [1, 2, 3]

        ##############################################################################################
        # ############ task 2 #########################################################################

        # retrieve task 2 score
        if 'task_2_score' in self.participant.vars:  # just error handling
            task_2_score = self.participant.vars['task_2_score']
        else:
            task_2_score = 6902

        # retrieve task 2 final score
        # final may differn from initial, since we need to break tie breakers.
        if 'task_2_final_score' in self.participant.vars:  # just error handling
            task_2_final_score = self.participant.vars['task_2_final_score']
        else:
            task_2_final_score = 6902

        # ############ task 3 #########################################################################

        # retrive user's payment_method_selection from task 3
        if 'payment_method_selection' in self.participant.vars:
            payment_method_selection = self.participant.vars['payment_method_selection']
        else:
            payment_method_selection = "individual performance"
        self.participant.vars['payment_method_selection'] = payment_method_selection

        # retrieve task 3 score
        if 'task_3_score' in self.participant.vars:  # just error handling
            task_3_score = self.participant.vars['task_3_score']
        else:
            task_3_score = 6903

        # retrieve task 3 final score
        # final may differn from initial, since we need to break tie breakers.
        if 'task_3_final_score' in self.participant.vars:  # just error handling
            task_3_final_score = self.participant.vars['task_3_final_score']
        else:
            task_3_final_score = 6903

        if 'risk_aversion_score' in self.participant.vars:
            risk_aversion_score = self.participant.vars['risk_aversion_score']
        else:
            risk_aversion_score = 6904

        # #######################################################################################
        # ####### select a task randomly for payment ############################################
        if random.uniform(0, 1) <= 1 / 3:
            self.participant.vars['task_4_payment'] = "Task 1"
            self.participant.vars['final_task_earnings'] = int(task_1_score) * 5
        elif random.uniform(0, 1) <= 1 / 2:
            self.participant.vars['task_4_payment'] = "Task 2"
            self.participant.vars['final_task_earnings'] = int(task_2_final_score) * 5
        else:
            self.participant.vars['task_4_payment'] = "Task 3"
            self.participant.vars['final_task_earnings'] = int(task_3_final_score) * 5

        self.participant.vars['final_earnings'] = self.participant.vars['final_task_earnings'] + Constants.showup_Fee + risk_aversion_score

        # #######################################################################################
        # ######### save to data structures @####################################################

        self.player.task_1_score = task_1_score

        self.player.op_scores = op_scores
        self.player.task_2_score = task_2_score
        self.player.task_2_final_score = task_2_final_score

        self.player.payment_method_selection = payment_method_selection
        self.player.task_3_score = task_3_score
        self.player.task_3_final_score = task_3_final_score

        self.player.risk_aversion_score = risk_aversion_score

        self.player.task_4_payment = self.participant.vars['task_4_payment']
        self.player.final_task_earnings = self.participant.vars['final_task_earnings']
        self.player.showup_Fee = Constants.showup_Fee
        self.player.final_earnings = self.participant.vars['final_earnings']

        ########################################################################################

        ########################################################################################
        return {

            'task_1_score': task_1_score,
            'task_1_score_2': self.player.task_1_score,

            'op_scores': op_scores,
            'task_2_score': task_2_score,
            'task_2_final_score': task_2_final_score,

            'op_scores_2': self.player.op_scores,
            'op_top_score_2': self.player.op_top_score,
            'task_2_score_2': self.player.task_2_score,
            'task_2_final_score_2': self.player.task_2_final_score,

            'payment_method_selection': payment_method_selection,
            'task_3_score': task_3_score,
            'task_3_score_4X': task_3_score * 4,
            'task_3_final_score': task_3_final_score,

            'payment_method_selection_2': self.participant.vars['payment_method_selection'],
            'task_3_score_2': self.player.task_3_score,
            'task_3_score_4X_2': self.player.task_3_score * 4,
            'task_3_final_score_2': self.player.task_3_final_score,

            'risk_aversion_score': self.player.risk_aversion_score,

            'task_4_payment': self.participant.vars['task_4_payment'],
            'final_task_earnings': self.participant.vars['final_task_earnings'],
            'showup_Fee': Constants.showup_Fee,
            'final_earnings': self.participant.vars['final_earnings'],

            'task_4_payment_2': self.participant.vars['task_4_payment'],
            'final_task_earnings_2': self.participant.vars['final_task_earnings'],
            'showup_Fee_2': Constants.showup_Fee,
            'final_earnings_2': self.participant.vars['final_earnings'],

            'debug': settings.DEBUG,
        }


class PaymentInfo(Page):
    def vars_for_template(self):
        return {

            'task_1_score': self.player.task_1_score,

            'op_scores': self.player.op_scores,
            'op_top_score': self.player.op_top_score,
            'task_2_score': self.player.task_2_score,
            'task_2_final_score': self.player.task_2_final_score,

            'payment_method_selection': self.participant.vars['payment_method_selection'],
            'task_3_score': self.player.task_3_score,
            'task_3_score_4X': self.player.task_3_score * 4,
            'task_3_final_score': self.player.task_3_final_score,

            'risk_aversion_score': self.participant.vars['risk_aversion_score'],

            'task_4_payment': self.participant.vars['task_4_payment'],
            'final_task_earnings': self.participant.vars['final_task_earnings'],
            'showup_Fee': Constants.showup_Fee,
            'final_earnings': self.participant.vars['final_earnings'],

            'debug': settings.DEBUG,

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
    Results,
    HoldOn,
    PaymentInfo
]
