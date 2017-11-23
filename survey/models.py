from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from django.forms import widgets as django_widgets

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

    ChoiceTable = {
        'q_CT_publicsector': 'I would rather work in public than private sector.',
        'q_CT_familyimportance': 'Family is more important than work.',
        'q_CT_wagevshours': 'I would work for higher wage even if there is less flexibility in working hours.',
        'q_CT_incomecontribution': 'Having a job is the best way for a woman to be an independent person.',
        'q_CT_jobwomenindependence': 'When a mother works for pay outside the home, the children suffer.',
        'q_CT_workingmother': 'A working mother can establish just as warm and secure a relationship with her children as a mother who does not work',
        'q_CT_fatherSuited': 'In general, fathers are as fit to look after children as mothers',
        'q_CT_preschoolWork': 'A pre-school child is likely to suffer if his or her mother works',
    }  # see for loop below class


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_rank = models.CharField(
        initial=None,
        choices=[
            ['1', "1..."],
            ['2', "2..."],
            ['3', "3..."],
            ['4', "4..."]
        ],
        verbose_name='',
        doc='What do you think was your rank within your Task 2 group in terms of sums solved correctly? Please choose a number from 1 (meaning you gave the most correct answers in your group) to 4 (meaning you gave the least correct answers in your group).',
        widget=widgets.RadioSelect())

    q_riskaversion = models.CharField(
        initial=None,
        choices=['8 AED for certain', '12 AED or 6 AED with a 50% chance', '16 AED or 4 AED with a 50% chance',
                 '20 AED or 2 AED with a 50% chance', '24 AED or 0 AED with a 50% chance'],
        verbose_name='',
        doc='Please pick one of the following.',
        widget=widgets.RadioSelect())


    def riskaversion_score(self):

        x = random.randint(0,1)

        return {
            '8 AED for certain': [8,8],
            '12 AED or 6 AED with a 50% chance':[12,6],
            '16 AED or 4 AED with a 50% chance':[16,4],
            '20 AED or 2 AED with a 50% chance':[20,2],
            '24 AED or 0 AED with a 50% chance':[24,0]

        }[self.q_riskaversion][x]

    # q_riskaversion_score = models.FloatField(
    #     doc = """the score they got in the risk averaion think""")


    q_riskpreference = models.CharField(
        initial=None,
        choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        verbose_name='',
        doc='Are you generally a person who is fully prepared to take risks or do you try to avoid taking risks?',
        widget=widgets.RadioSelect())

    q_mathlevel = models.CharField(
        initial=None,
        choices=[
            'Pre-Calculus', 'Calculus', 'Mutivariable calculus', 'Beyond multivariable calculus'
        ],
        verbose_name='',
        doc='What is the highest mathematics level you have taken thus far?',
        widget=widgets.RadioSelect())

    q_GPA_2ndSchool_HighSchool = models.CharField(
        verbose_name="What was your final GPA in secondary school or high school?",
            doc="""...."""
        )


    q_majordeclarationYN = models.CharField(
        initial=None,
        choices=[
            'Yes',
            'No'
        ],
        verbose_name='',
        doc='Have you declared your major?',
        widget=widgets.RadioSelect())


    # how to input checkboxes. 
    #https://groups.google.com/forum/#!searchin/otree/checkbox%7Csort:date/otree/CLmiH595UDM/LrItGoXvAAAJ
    q_expectedstudytrack = models.CharField(
        initial=None,
        choices=[
            'Arts and Humanities',
            'Engineering',
            'Multidisciplinary Track (Interactive Media, Arab Crossroads',
            'Science',
            'Social Science',
        ],
        verbose_name='',
        doc='What is your expected study track? Which of the academic divisions does your expectad major fall under?'
            'If you are unsure, mark the division you are most interested in. If you plan to double major, tick both.',
<<<<<<< HEAD
        widget=widgets.RadioSelect())
=======
            widget=django_widgets.CheckboxInput())


>>>>>>> d66d461f3d6df7107f9f454aad531bdd021130f7

    q_declaredstudytrack = models.CharField(
        initial=None,
        choices=[
            'Arts and Humanities',
            'Engineering',
            'Multidisciplinary Track (Interactive Media, Arab Crossroads',
            'Science',
            'Social Science',
<<<<<<< HEAD
        ],
        verbose_name='',
        doc='Which academic division does your major fall under?',
        widget=widgets.RadioSelect())
=======
            ],
            verbose_name='...',
            doc='Which academic division does your major fall under?',
            widget=django_widgets.CheckboxInput()
            )
>>>>>>> d66d461f3d6df7107f9f454aad531bdd021130f7

    q_gpastudytrack = models.CharField(
        initial=None,
        choices=[
            'Arts and Humanities',
            'Engineering',
            'Multidisciplinary Track (Interactive Media, Arab Crossroads',
            'Science',
            'Social Science',
<<<<<<< HEAD
        ],
        verbose_name='',
        doc='In which academic division do you think it is more difficult to receive a high GPA?',
        widget=widgets.RadioSelect())
=======
            ],
            verbose_name='',
            doc='In which academic division do you think it is more difficult to receive a high GPA?',
             widget=django_widgets.SelectMultiple()
             )
>>>>>>> d66d461f3d6df7107f9f454aad531bdd021130f7

    q_profitablestudytrack = models.CharField(
        initial=None,
        choices=[
            'Arts and Humanities',
            'Engineering',
            'Multidisciplinary Track (Interactive Media, Arab Crossroads',
            'Science',
            'Social Science',
<<<<<<< HEAD
        ],
        verbose_name='',
        doc='In which academic division do you think it is more difficult to receive a high GPA?',
        widget=widgets.RadioSelect())
=======
            ],
            verbose_name='',
            doc='In which academic division do you think it is more difficult to receive a high GPA?',
             widget=django_widgets.SelectMultiple()
             )
>>>>>>> d66d461f3d6df7107f9f454aad531bdd021130f7

    q_mathlevelnyuad = models.CharField(
        initial=None,
        choices=[
            '...in the top 25%?',
            '...in the top 25-50%?',
            '...in the top 50-75%?',
            '...in the bottom 25%?',
        ],
        verbose_name='Compared to other NYUAD students, do you think your mathematics abilitiy is...',
        doc='Compared to other NYUAD students, do you think your mathematics abilitiy is...',
        widget=widgets.RadioSelect())

    q_passinggrade = models.CharField(
        initial=None,
        choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        verbose_name='',
        doc='How difficult is it for you to get a passing grade in mathematics?',
        widget=widgets.RadioSelect())

    q_wealth = models.CharField(
        initial=None,
        choices=[
            '1', '2', '3', '4', '5', '6'],
        verbose_name='',
        doc="Please rank your family's wealth based on your home country's standards",
        widget=widgets.RadioSelect())



for key in Constants.ChoiceTable:
    Player.add_to_class(key,
        models.IntegerField(initial=None,
<<<<<<< HEAD
                                            choices=[
                                                [1, ""],
                                                [2, ""],
                                                [3, ""],
                                                [4, ""]
                                            ],
                                            verbose_name=Constants.ChoiceTable[key],
                                            doc=Constants.ChoiceTable[key] + str(
                                                "From a scale of 1 to 4 (1 = fully disagree, 4 = fully agree),\n"
                                                "please tell us how much you agree with the following statements:")
                                            ))
=======
            choices=[
            [1, ""],
            [2, ""],
            [3, ""],
            [4, ""]
            ],
            verbose_name=Constants.ChoiceTable[key],
            doc=Constants.ChoiceTable[key] + str("From a scale of 1 to 4 (1 = fully disagree, 4 = fully agree),\n"
                                                 "please tell us how much you agree with the following statements:")
            ))

>>>>>>> d66d461f3d6df7107f9f454aad531bdd021130f7
