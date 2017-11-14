from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants, check_and_ok
from django.conf import settings
import time
import random

class holdon(Page):
    def is_displayed(self):
        return self.round_number == 1


class Init(Page):

  
    form_model = models.Player
    form_fields = [
    'subject_netid',
    ]

    def is_displayed(self):

        if self.round_number == 1:
            self.participant.vars['start_time'] = None
        return self.round_number == 1


class Intro1(Page):
    # timeout_seconds = 300

    def is_displayed(self):

        if self.round_number == 1:
            self.participant.vars['start_time'] = None

        return self.round_number == 1


class Intro2(Page):
    timeout_seconds = 180

    def is_displayed(self):
        return self.round_number < 2




page_sequence = [
    holdon,
    Init,
    Intro1,
    ]






