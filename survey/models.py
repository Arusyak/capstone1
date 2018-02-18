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
    showup_Fee = 30
    name_in_url = 'survey'
    players_per_group = 4
    num_rounds = 1

    ChoiceTable = {
        'q_CT_publicsector': 'I would rather work in public than private sector.',
        'q_CT_familyimportance': 'Family is more important than work.',
        'q_CT_wagevshours': 'I would work for higher wage even if there is less flexibility in working hours.',
        'q_CT_incomecontribution': 'Having a job is the best way for a woman to be an independent person.',
        'q_CT_jobwomenindependence': 'When a mother works for pay outside the home, the children suffer.',
        'q_CT_workingmother': 'A working mother can establish just as warm and secure a relationship with her '
                              'children as a mother who does not work',
        'q_CT_fatherSuited': 'In general, fathers are as fit to look after children as mothers',
        'q_CT_preschoolWork': 'A pre-school child is likely to suffer if his or her mother works',
    }  # see for loop below class

    ChoiceTable1 = {
        'q_gpastudytrack_AH': 'Arts and Humanities',
        'q_gpastudytrack_EG': 'Engineering',
        'q_gpastudytrack_MD': 'Multidisciplinary (Arab Crossroads or Interactive Media)',
        'q_gpastudytrack_SC': 'Science',
        'q_gpastudytrack_SS': 'Social Science'
    }

    ChoiceTable2 = {
        'q_profitablestudytrack_AH': 'Arts and Humanities',
        'q_profitablestudytrack_EG': 'Engineering',
        'q_profitablestudytrack_MD': 'Multidisciplinary (Arab Crossroads or Interactive Media)',
        'q_profitablestudytrack_SC': 'Science',
        'q_profitablestudytrack_SS': 'Social Science'
    }


class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.payoff = 0
            if 'showupfee' in self.session.config:
                p.showupfee = self.session.config['showupfee']
            else:
                p.showupfee = Constants.showup_Fee


class Group(BaseGroup):
    def identify_payment(self):
        task_choice = random.uniform(0, 1)

        for PLAYER in self.get_players():
            # ############ task 1 #####################################################################################
            #  retrieve task 1 score
            if 'task_1_score' in PLAYER.participant.vars:  # just error handling
                task_1_score = PLAYER.participant.vars['task_1_score']
            else:
                task_1_score = 0

            # #############################################################################################
            # ############ task 2 #########################################################################

            # retrieve task 2 final score
            # final may differn from initial, since we need to break tie breakers.
            if 'task_2_final_score' in PLAYER.participant.vars:  # just error handling
                task_2_final_score = PLAYER.participant.vars['task_2_final_score']
            else:
                task_2_final_score = 0

            # ############ task 3 #########################################################################

            if 'task_3_final_score' in PLAYER.participant.vars:  # just error handling
                task_3_final_score = PLAYER.participant.vars['task_3_final_score']
            else:
                task_3_final_score = 0

            if task_choice <= 1 / 3:
                PLAYER.participant.vars['task_4_payment'] = "Task 1"
                PLAYER.participant.vars['final_task_earnings'] = task_1_score * 4
            elif 2 / 3 >= task_choice > 1/3:
                PLAYER.participant.vars['task_4_payment'] = "Task 2"
                PLAYER.participant.vars['final_task_earnings'] = task_2_final_score * 4
            else:
                PLAYER.participant.vars['task_4_payment'] = "Task 3"
                PLAYER.participant.vars['final_task_earnings'] = task_3_final_score * 4


class Player(BasePlayer):
    q_rank = models.StringField(
        initial=None,
        choices=[
            ['1', "1 (you solved the most questions right)"],
            ['2', "2"],
            ['3', "3"],
            ['4', "4 (you solved the least questions right)"]
        ],
        verbose_name='',
        doc='What do you think was your rank within your Task 2 group in terms of sums solved correctly? Please '
            'choose a number from 1 (meaning you gave the most correct answers in your group) to 4 (meaning you gave '
            'the least correct answers in your group).',
        widget=widgets.RadioSelect())

    q_riskaversion = models.StringField(
        initial=None,
        choices=['8 AED for certain',
                 '12 AED with a 50% chance or 6 AED with a 50% chance',
                 '16 AED with a 50% chance or 4 AED with a 50% chance',
                 '20 AED with a 50% chance or 2 AED with a 50% chance',
                 '24 AED with a 50% chance or 0 AED with a 50% chance'],
        verbose_name='',
        doc='Please pick one of the following.',
        widget=widgets.RadioSelect())

    def risk_aversion_score(self):
        x = random.randint(0, 1)
        return {
            '8 AED for certain': [8, 8],
            '12 AED with a 50% chance or 6 AED with a 50% chance': [12, 6],
            '16 AED with a 50% chance or 4 AED with a 50% chance': [16, 4],
            '20 AED with a 50% chance or 2 AED with a 50% chance': [20, 2],
            '24 AED with a 50% chance or 0 AED with a 50% chance': [24, 0]
        }[self.q_riskaversion][x]

    def vars_for_template(self):
        self.participant.vars['risk_aversion_score'] = self.risk_aversion_score()

    q_riskpreference = models.StringField(
        initial=None,
        choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        verbose_name='',
        doc='Are you generally a person who is fully prepared to take risks or do you try to avoid taking risks?',
        widget=widgets.RadioSelect())

    # def vars_for_template(self):
    #     return {
    #         "risk_aversion_score": self.risk_aversion_score()
    #     }

    q_mathplacement = models.StringField(
        initial=None,
        choices=['Mathematical Functions', 'Introduction to Vector Mathematics', 'Trigonometry and Differential Equations','Calculus', 'Multivariable Calculus'],
        verbose_name='',
        doc='Which course were you placed based on Math Assessment test?',
        widget=widgets.RadioSelect()
    )

    q_mathlevel = models.StringField(
        initial=None,
        choices=[
            'Pre-Calculus', 'Calculus', 'Mutivariable calculus', 'Beyond multivariable calculus'],
        verbose_name='',
        doc='What is the highest mathematics level you have taken thus far?',
        widget=widgets.RadioSelect()
    )

    q_GPA_highschool = models.FloatField(
        verbose_name='',
        doc="""GPA real""",
    )

    q_GPA_highschool_max = models.FloatField(
        verbose_name='',
        doc="""GPA max"""
    )

    q_majordeclarationYN = models.StringField(
        initial=None,
        choices=[
            'Yes',
            'No'
        ],
        verbose_name='',
        doc='Have you declared your major?',
        widget=widgets.RadioSelect())

    # how to input checkboxes.
    # https://groups.google.com/forum/#!searchin/otree/checkbox%7Csort:date/otree/CLmiH595UDM/LrItGoXvAAAJ
    q_expectedstudytrack_AH = models.BooleanField(
        initial=None,
        # choices = [
        #      0,1
        # ],
        verbose_name='Arts and Humanities',
        doc='Arts and Humanities expected',
        widget=django_widgets.CheckboxInput()
    )

    q_expectedstudytrack_EG = models.BooleanField(
        initial=None,
        # choices = [
        #     0,1],
        verbose_name='Engineering',
        doc='Engineering expected',
        widget=django_widgets.CheckboxInput()
    )

    q_expectedstudytrack_MD = models.BooleanField(
        initial=None,
        # choices = [
        #   0, 1],
        verbose_name='Multidisciplinary (Arab Crossroads or Interactive Media)',
        doc='Multidisciplinary expected',
        widget=django_widgets.CheckboxInput()
    )

    q_expectedstudytrack_SC = models.BooleanField(
        initial=None,
        # choices=[
        #     0, 1],
        verbose_name='Science',
        doc='Science expected',
        widget=django_widgets.CheckboxInput()
    )

    q_expectedstudytrack_SS = models.BooleanField(
        initial=None,
        # choices=[
        #     0, 1],
        verbose_name='Social Science',
        doc='Social Science expected',
        widget=django_widgets.CheckboxInput()
    )

    q_declaredstudytrack_AH = models.BooleanField(
        initial=None,
        verbose_name='Arts and Humanities',
        doc='Arts and Humanities declared',
        widget=django_widgets.CheckboxInput())

    q_declaredstudytrack_EG = models.BooleanField(
        initial=None,
        verbose_name='Engineering',
        doc='Engineering declared',
        widget=django_widgets.CheckboxInput()
    )

    q_declaredstudytrack_MD = models.BooleanField(
        initial=None,
        verbose_name='Multidisciplinary (Arab Crossroads or Interactive Media)',
        doc='Multidisciplinary declared',
        widget=django_widgets.CheckboxInput()
    )

    q_declaredstudytrack_SC = models.BooleanField(
        initial=None,
        verbose_name='Science',
        doc='Science declared',
        widget=django_widgets.CheckboxInput()
    )

    q_declaredstudytrack_SS = models.BooleanField(
        initial=None,
        verbose_name='Social Science',
        doc='Social Science declared',
        widget=django_widgets.CheckboxInput()
    )

    q_gpastudytrack = models.StringField(
        initial=None,
        choices=[
            'Arts and Humanities',
            'Engineering',
            'Multidisciplinary Track (Interactive Media, Arab Crossroads',
            'Science',
            'Social Science'
        ],
        verbose_name='',
        doc='In which academic division do you think it is more difficult to receive a high GPA?',
        widget=django_widgets.SelectMultiple()
    )

    q_profitablestudytrack = models.StringField(
        initial=None,
        choices=[
            'Arts and Humanities',
            'Engineering',
            'Multidisciplinary Track (Interactive Media, Arab Crossroads',
            'Science',
            'Social Science'
        ],
        verbose_name='',
        doc='In which academic division do you think it is more difficult to receive a high GPA?',
        widget=django_widgets.SelectMultiple()
    )

    q_mathlevelnyuad = models.StringField(
        initial=None,
        choices=[
            '...in the top 25%?',
            '...in the top 25-50%?',
            '...in the top 50-75%?',
            '...in the bottom 25%?'
        ],
        verbose_name='',
        doc='Compared to other NYUAD students, do you think your mathematics ability is...',
        widget=widgets.RadioSelect())

    q_passinggrade = models.StringField(
        initial=None,
        choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        verbose_name='',
        doc='How difficult is it for you to get a passing grade in mathematics?',
        widget=widgets.RadioSelect())

    q_wealth = models.StringField(
        initial=None,
        choices=[
            '1', '2', '3', '4', '5', '6'],
        verbose_name='',
        doc="Please rank your family's wealth based on your home country's standards",
        widget=widgets.RadioSelect())

    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

    task_1_score = models.PositiveIntegerField(
        doc='subject score in task 1')

    task_2_score = models.PositiveIntegerField(
        doc='subject score on task 2, num task correct')
    op_scores = models.StringField(
        doc='this subjects opposing player scores from task 2. also used in task 3')
    op_top_score = models.PositiveIntegerField(
        doc='the top score this player faced')
    task_2_final_score = models.PositiveIntegerField(
        doc='subject final score, after comparision')

    payment_method_selection = models.StringField(
        doc='subjects payment method selection, individual or comparision')
    task_3_score = models.PositiveIntegerField(
        doc='subject score on task 3, num tasks correct')
    task_3_final_score = models.PositiveIntegerField(
        doc='subjects final score on task 3. if subject chose comparison, score after . otherwise individual score')

    task_4_payment = models.StringField(
        doc='the task randomly selected for payment. task 1, 2 or 3')
    final_task_earnings = models.FloatField(
        doc='earnings from the task randomly selected, before showup fee and risk aversion score')

    risk_aversion_payment = models.PositiveIntegerField(
        doc='the risk aversion score from survey')

    showup_Fee = models.FloatField(
        doc='showup fee')
    final_earnings = models.FloatField(
        doc='final earnings, in currency. including task earnings and showup fee, before charity')


for key in Constants.ChoiceTable:
    Player.add_to_class(key,
                        models.IntegerField(initial=None,
                                            choices=[
                                                [1, ""],
                                                [2, ""],
                                                [3, ""],
                                                [4, ""]
                                            ],
                                            verbose_name=Constants.ChoiceTable[key],
                                            doc=Constants.ChoiceTable[key] + str(
                                                "From a scale of 1 to 4 (1 = fully disagree, 4 = fully agree),\n"
                                                "please tell us how much you agree with the following statements:")))

for key in Constants.ChoiceTable1:
    Player.add_to_class(key,
                        models.IntegerField(initial=None,
                                            choices=[
                                                [1, ""],
                                                [2, ""],
                                                [3, ""],
                                                [4, ""],
                                                [5, ""],
                                            ],
                                            verbose_name=Constants.ChoiceTable1[key],
                                            doc=Constants.ChoiceTable1[key] + str(
                                                """Rank these divisions in terms of how difficult it is to get a high 
                                                GPA.""")
                                            ))

for key in Constants.ChoiceTable2:
    Player.add_to_class(key,
                        models.IntegerField(initial=None,
                                            choices=[
                                                [1, ""],
                                                [2, ""],
                                                [3, ""],
                                                [4, ""],
                                                [5, ""],
                                            ],
                                            verbose_name=Constants.ChoiceTable2[key],
                                            doc=Constants.ChoiceTable2[key] + str(
                                                """Rank these divisions in terms of how much money you expect a 
                                                student would earn in 10 years.""")
                                            ))
