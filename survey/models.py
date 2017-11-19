from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

    # From a scale of 1 to 7 (1 = completely disagree; 4 = completely agree), please tell us how much you agree with the following statements:
    # Randomize order of rows
    ChoiceTable2 = {
         'q_CT2_publicsector':'I would rather work in public than private sector.',
         'q_CT2_familyimportance':'Family is more important than work.',
         'q_CT2_wagevshours':'I would work for higher wage even if there is less flexibility in working hours.',
         'q_CT2_incomecontribution':'Having a job is the best way for a woman to be an independent person.',
         'q_CT2_jobwomenindependence':'When a mother works for pay outside the home, the children suffer.',
         'q_CT2_workingmother':'A university education is more important for a boy than for a girl.',
         'q_CT2_fatherSuited':'Being a housewife is just as fulfilling as working for pay.',
         'q_CT2_preschoolWork':'Women are encouraged to study at the university.',
    } #see for loop below class

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
