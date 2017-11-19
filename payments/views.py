import copy
import random

import settings
from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label or participant.code,
        }


page_sequence = [PaymentInfo]


class HoldOn(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):

        ############# task 1 ##############################################################################################
        # retrieve task 1 score
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
        ############# task 2 #########################################################################
        # retrieve task 2 score
        if 'task_2_score' in self.participant.vars:  # just error handling
            task_2_score = self.participant.vars['task_2_score']
        else:
            task_2_score = 6902

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

        op_top_score = max(op_scores)

        # For task 2 results, generate text to help player understand their score.
        # the logic of how this is handled is in views.py for task 2
        if task_2_score > op_top_score:
            t2_result_print = "You have the top score."
        elif task_2_score == op_top_score:

            # get list of all score
            z = copy.copy(op_scores)
            z.append(task_2_score)

            # count number of top scores
            cnt = 0
            for i in z:
                if i == op_top_score:
                    cnt += 1

            # Go to task_2_final_score, is it zero? (didnt win the die toss) or >op_top_score (did win the die toss)?
            if task_2_final_score > op_top_score:
                t2_result_print = "You are tied for the top score. Including you, there were " + str(
                    cnt) + " players with the top score. The winner was chosen randomly among the top scorers. Good news, you won!"
            else:
                t2_result_print = "You are tied for the top score. Including you, there were " + str(
                    cnt) + " players with the top score. The winner was chosen randomly among the top scorers. Sorry, you didn't win."

        else:
            t2_result_print = "You do not have the top score."
        self.participant.vars['t2_result_print'] = t2_result_print

        ##############################################################################################
        ############# task 3 #########################################################################

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

        # For task 3 results, generate text to help player understand their score.
        # the logic of how this is handled is in views.py for task 3
        if task_3_score > op_top_score:
            t3_result_print = "You have the top score."
        elif task_3_score == op_top_score:

            # get list of all score
            z = copy.copy(op_scores)
            z.append(task_2_score)

            # count number of top scores
            cnt = 0
            for i in z:
                if i == op_top_score:
                    cnt += 1

            # Go to task_3_final_score, is it zero? (didnt win the die toss) or >op_top_score (did win the die toss)?
            if task_3_final_score > op_top_score:
                t3_result_print = "You are tied for the top score. Including you, there were " + str(
                    cnt) + " players with the top score. The winner was chosen randomly among the top scorers. Good news, you won!"
            else:
                t3_result_print = "You are tied for the top score. Including you, there were " + str(
                    cnt) + " players with the top score. The winner was chosen randomly among the top scorers. Sorry, you didn't win."

        else:
            t3_result_print = "You do not have the top score."
        self.participant.vars['t3_result_print'] = t3_result_print


        t1_results_table = self.participant.vars['t1_results']
        t2_results_table = self.participant.vars['t2_results']
        t3_results_table = self.participant.vars['t3_results']

        ########################################################################################
        ######## select a task randomly for payment ############################################

        if random.uniform(0, 1) <= 1 / 3:
            self.participant.vars['task_4_payment'] = "Task 1"
            self.participant.vars['final_task_earnings'] = int(task_1_score) * 5
        elif random.uniform(0, 1) <= 1 / 2:
            self.participant.vars['task_4_payment'] = "Task 2"
            self.participant.vars['final_task_earnings'] = int(task_2_final_score) * 5
        else:
            self.participant.vars['task_4_payment'] = "Task 3"
            self.participant.vars['final_task_earnings'] = int(task_3_final_score) * 5

        self.participant.vars['final_earnings'] = self.participant.vars['final_task_earnings'] + Constants.showup_Fee

        ########################################################################################
        ########## save to data structures @####################################################

        self.player.task_1_score = task_1_score

        self.player.op_scores = op_scores
        self.player.op_top_score = op_top_score
        self.player.task_2_score = task_2_score
        self.player.task_2_final_score = task_2_final_score

        self.player.payment_method_selection = payment_method_selection
        self.player.task_3_score = task_3_score
        self.player.task_3_final_score = task_3_final_score

        self.player.task_4_payment = self.participant.vars['task_4_payment']
        self.player.final_task_earnings = self.participant.vars['final_task_earnings']
        self.player.showup_Fee = Constants.showup_Fee
        self.player.final_earnings = self.participant.vars['final_earnings']

        ########################################################################################


        ########################################################################################
        return {
            't1_results_table': t1_results_table,
            't1_results_table_2': self.participant.vars['t1_results'],

            'task_1_score': task_1_score,
            'task_1_score_2': self.player.task_1_score,

            'op_scores': op_scores,
            'op_top_score': op_top_score,
            't2_results_table': t2_results_table,
            'task_2_score': task_2_score,
            'task_2_final_score': task_2_final_score,
            't2_result_print': t2_result_print,

            'op_scores_2': self.player.op_scores,
            'op_top_score_2': self.player.op_top_score,
            't2_results_table_2': self.participant.vars['t2_results'],
            'task_2_score_2': self.player.task_2_score,
            'task_2_final_score_2': self.player.task_2_final_score,
            't2_result_print_2': self.participant.vars['t2_result_print'],

            'payment_method_selection': payment_method_selection,
            't3_results_table': t3_results_table,
            'task_3_score': task_3_score,
            'task_3_score_4X': task_3_score * 4,
            'task_3_final_score': task_3_final_score,
            't3_result_print': t3_result_print,

            'payment_method_selection_2': self.participant.vars['payment_method_selection'],
            't3_results_table_2': self.participant.vars['t3_results'],
            'task_3_score_2': self.player.task_3_score,
            'task_3_score_4X_2': self.player.task_3_score * 4,
            'task_3_final_score_2': self.player.task_3_final_score,
            't3_result_print_2': self.participant.vars['t3_result_print'],

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