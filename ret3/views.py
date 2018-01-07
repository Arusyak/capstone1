import copy

from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from django.conf import settings
import time
import random


class Intro(Page):
    def is_displayed(self):
        if self.round_number == 1:
            self.participant.vars['start_time'] = None
            self.participant.vars['end_time'] = None
            self.participant.vars['task_2_score'] = 0

            return self.round_number == 1

    def before_next_page(self):
        # user has ret_timer seconds to complete as many pages as possible
        self.participant.vars['expiry_timestamp'] = time.time() + self.player.task_timer

    def vars_for_template(self):
        return {
            'debug': settings.DEBUG,
        }


class SumTask(Page):
    form_model = models.Player
    form_fields = ['user_total']

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3

    def vars_for_template(self):
        self.player.solution = sum(Constants.INTS_T4[self.round_number - 1])

        def html_table_64(arr):  # converts Constants.INTS_2 array into an html matrix
            cnt = 0
            result = ""
            result = result + '<table align="center" class="mat">'  # note class mat, see task template.
            for row in range(8):
                result = result + '  <tr>'
                for cell in range(8):
                    result = result + '    <td>' + str(arr[cnt]) + '</td>'
                    cnt = cnt + 1
                result = result + '</tr>'
            result = result + '</table>'

            return (result)

        # current number of correctly done tasks
        total_payoff = 0
        for p in self.player.in_all_rounds():
            if p.payoff_score != None:
                total_payoff += p.payoff_score

        # set up messgaes in transcription task
        if self.round_number == 1:  # on very first task
            correct_last_round = "<br>"
        else:  # all subsequent tasks
            if self.player.in_previous_rounds()[-1].is_correct:
                correct_last_round = "Your last sum was <font color='green'>correct</font>"
            else:
                correct_last_round = "Your last sum was <font color='red'>incorrect</font>"

        return {
            'total_payoff': round(total_payoff),
            'round_count': (self.round_number - 1),
            'debug': settings.DEBUG,
            'correct_last_round': correct_last_round,
            'matrix_array': Constants.INTS_T4[self.round_number - 1],
            'matrix': html_table_64(Constants.INTS_T4[self.round_number - 1]),
            'correct_sum': self.player.solution
        }

    def before_next_page(self):
        self.player.score_round()

class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def after_all_players_arrive(self):
        self.group.score_round()


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        total_payoff = 0
        for p in self.player.in_all_rounds():
            if p.payoff_score != None:
                total_payoff += p.payoff_score

        self.participant.vars['task_3_score'] = total_payoff

        for prev_player in self.player.in_all_rounds():
            if prev_player.task_payment_choose != None:
                payment_method_selection = prev_player.task_payment_choose
            if prev_player.task_payment_choose == None:
                payment_method_selection = "no input (compared scoring)"
        self.participant.vars['payment_method_selection'] = payment_method_selection

        # retrive other player's scores from task 2
        # just error handling, if op_scores are None, say in testing
        if 'task_2_op_scores' in self.participant.vars:
            op_scores = self.participant.vars['task_2_op_scores']
        else:
            op_scores = [1, 2, 3]

        top_score = max(op_scores)  # find top score

        # calc final score "compared payment" method
        # from "task_3_final_score" from "task_3_score" and "op_scores"
        if self.participant.vars['task_3_score'] > top_score:
            result_print = "You have the top score."
            self.participant.vars['task_3_cp_score'] = 4 * self.participant.vars['task_3_score']
        elif self.participant.vars['task_3_score'] == top_score:

            # get list of all score
            z = copy.copy(op_scores)
            z.append(self.participant.vars['task_3_score'])

            # count number of top scores
            cnt = 0
            for i in z:
                if i == top_score:
                    cnt += 1
            # roll a cnt sided die (there are at least two)
            if random.uniform(0, 1) <= 1 / cnt:
                result_print = "You are tied for the top score. Including you, there were " + str(
                    cnt) + " players with the top score. The winner was chosen randomly among the top scorers. Good news, you won!"
                self.participant.vars['task_3_cp_score'] = 4 * self.participant.vars['task_3_score']
            else:
                result_print = "You are tied for the top score. Including you, there were " + str(
                    cnt) + " players with the top score. The winner was chosen randomly among the top scorers. Sorry, you didn't win."
                self.participant.vars['task_3_cp_score'] = 0

        else:
            result_print = "You do not have the top score."
            self.participant.vars['task_3_cp_score'] = 0

        if ("compared" in payment_method_selection) | (payment_method_selection == "no input (compared scoring)"):
            self.participant.vars['task_3_final_score'] = self.participant.vars['task_3_cp_score']  # compared scoring
        else:
            self.participant.vars['task_3_final_score'] = self.participant.vars['task_3_score']  # other kind of scoring

        #######################################################################

        # only keep obs if YourEntry player_sum, is not None.
        table_rows = []
        for prev_player in self.player.in_all_rounds():
            if prev_player.user_total != None:
                row = {
                    'round_number': prev_player.round_number,
                    'Ints_sum': prev_player.solution,
                    'player_sum': prev_player.user_total,
                    'is_correct': prev_player.is_correct,
                    'payoff': round(prev_player.payoff_score),
                }
                table_rows.append(row)

        self.participant.vars['t3_results'] = table_rows

        return {
            'debug': settings.DEBUG,
            'table_rows': table_rows,
            'total_payoff': round(self.participant.vars['task_3_score']),
            'op_scores': op_scores,
            'top_score': round(top_score),
            'task_3_cp_score': round(self.participant.vars['task_3_cp_score']),
            'final_score': round(self.participant.vars['task_3_final_score']),
            'result_print': (result_print),
            'payment_method_selection': payment_method_selection,
        }


page_sequence = [Intro, SumTask, ResultsWaitPage, Results]
