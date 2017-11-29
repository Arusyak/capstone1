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

    # timeout_seconds = self.player.ret_timer # time? no, only works on specific pages

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3

    def vars_for_template(self):

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
        }

    def before_next_page(self):
        self.group.score_round()




class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def after_all_players_arrive(self):
        self.group.score_round()

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):



        # get other player's scores
        op_scores = []

        # loop over scores
        for op in self.player.get_others_in_group():
            op_scores.append(int(op.participant.vars['task_2_score']))

        # # randomly draw op scores...
        # while (len(op_scores) < 3):
        #     op = self.player.get_others_in_group()[random.randint(0,len(self.player.get_others_in_group())-1)] #draw a random competitor
        #     if int(op.participant.vars['task_2_score']) > 0: # may have null players, check if they are before including their scores.
        #         op_scores.append(int(op.participant.vars['task_2_score']))

        self.participant.vars['task_2_op_scores'] = op_scores  # save other player scores for score task3

        top_score = max(op_scores)

        if self.participant.vars['task_2_score'] > top_score:
            result_print = "You have the top score."
            self.participant.vars['task_2_final_score'] = 4 * self.participant.vars['task_2_score']
        elif self.participant.vars['task_2_score'] == top_score:

            # get list of all score
            z = copy.copy(op_scores)
            z.append(self.participant.vars['task_2_score'])

            # count number of top scores
            cnt = 0
            for i in z:
                if i == top_score:
                    cnt += 1
            # roll a cnt sided die (there are at least two)
            if random.uniform(0, 1) <= 1 / cnt:
                result_print = "You are tied for the top score. Including you, there were " + str(
                    cnt) + " players with the top score. The winner was chosen randomly among the  " + str(
                    cnt) + " top scorers. Good news, you won!"
                self.participant.vars['task_2_final_score'] = 4 * self.participant.vars['task_2_score']
            else:
                result_print = "You are tied for the top score. Including you, there were " + str(
                    cnt) + " players with the top score. The winner was chosen randomly among the  " + str(
                    cnt) + " top scorers. Sorry, you didn't win."
                self.participant.vars['task_2_final_score'] = 0

        else:
            result_print = "You do not have the top score."
            self.participant.vars['task_2_final_score'] = 0

        # only keep obs if YourEntry player_sum, is not None.
        table_rows = []
        for prev_player in self.player.in_all_rounds():
            if (prev_player.user_total != None):
                if (prev_player.user_total > 0):
                    row = {
                        'round_number': prev_player.round_number,
                        'int1': prev_player.int1,
                        'int2': prev_player.int2,
                        'int3': prev_player.int3,
                        'int4': prev_player.int4,
                        'int5': prev_player.int5,
                        'Ints_sum': prev_player.solution,
                        'player_sum': round(prev_player.user_total),
                        'is_correct': prev_player.is_correct,
                        'payoff': round(prev_player.payoff_score),
                    }
                    table_rows.append(row)

        self.participant.vars['t2_results'] = table_rows

        return {
            'debug': settings.DEBUG,
            'table_rows': table_rows,
            'total_payoff':round(self.participant.vars['task_2_score']),
            'op_scores':op_scores,
            'top_score':round(top_score),
            'final_score':round(self.participant.vars['task_2_final_score']),
            'result_print':result_print,
        }

        # def before_next_page(self):
        #     self.participant.vars['start_time'] = None


page_sequence = [
    Intro,
    SumTask,
    ResultsWaitPage,
    Results
]
