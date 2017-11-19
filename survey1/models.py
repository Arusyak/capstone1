from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey1'
    players_per_group = None
    num_rounds = 1

    # From a scale of 1 to 4 (1 = completely disagree; 4 = completely agree), please tell us how much you agree with the following statements:
    # Randomize order of rows
    ChoiceTable = {
         'q_CT_publicsector':'I would rather work in public than private sector.',
         'q_CT_familyimportance':'Family is more important than work.',
         'q_CT_wagevshours':'I would work for higher wage even if there is less flexibility in working hours.',
         'q_CT_incomecontribution':'Having a job is the best way for a woman to be an independent person.',
         'q_CT_jobwomenindependence':'When a mother works for pay outside the home, the children suffer.',
         'q_CT_workingmother':'A university education is more important for a boy than for a girl.',
         'q_CT_fatherSuited':'Being a housewife is just as fulfilling as working for pay.',
         'q_CT_preschoolWork':'Women are encouraged to study at the university.',
    } #see for loop below class

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # ret_timer = models.PositiveIntegerField(
    #     doc="""The length of the real effort task timer."""
    # )
    #
    # showupfee = models.PositiveIntegerField(
    #     doc="""Showup fee, in AED."""
    # )
    #
    # def set_payoff(self):
    #     """Calculate payoff, which is zero for the survey"""
    #     self.payoff = 0
    #
    # task_1_score = models.PositiveIntegerField(
    #     doc='subject score in task 1')
    #
    # task_2_score = models.PositiveIntegerField(
    #     doc='subject score on task 2, num task correct')
    # op_scores = models.CharField(
    #     doc='this subjects opposing player scores from task 2. also used in task 3')
    # op_top_score = models.PositiveIntegerField(
    #     doc='the top score this player faced')
    # task_2_final_score = models.PositiveIntegerField(
    #     doc='subject final score, after comparision')
    #
    # payment_method_selection = models.CharField(
    #     doc='subjects payment method selection, individual or tournament')
    # task_3_score = models.PositiveIntegerField(
    #     doc='subject score on task 3, num tasks correct')
    # task_3_final_score = models.PositiveIntegerField(
    #     doc='subjects final score on task 3. if subject chose tournament, score after. otherwise individual score')
    #
    # task_4_payment = models.CharField(
    #     doc='the task randomly selected for payment. task 1, 2 or 3')
    # final_task_earnings = models.FloatField(
    #     doc='earnings from the task randomly selected, before showup fee')
    # showup_Fee = models.FloatField(
    #     doc='showup fee')
    # final_earnings = models.FloatField(
    #     doc='final earnings, in currency. including task earnings and showup fee')

    ###### Performance question ##########################################################################################

    q_rank = models.CharField(
            initial=None,
            choices=['1','2','3','4'],
            verbose_name='What do you think was your rank within your Task 2 group in terms of sums solved correctly? Please choose a number from 1 (meaning you gave the most correct answers in your group) to 4 (meaning you gave the least correct answers in your group). ',
            doc='What do you think was your rank within your Task 2 group in terms of sums solved correctly? Please choose a number from 1 (meaning you gave the most correct answers in your group) to 4 (meaning you gave the least correct answers in your group).',
            widget=widgets.RadioSelect())

    q_riskaversion = models.CharField(
            initial=None,
            choices=['8 AED for certain','12 AED or 6 AED with a 50% chance','16 AED or 4 AED with a 50% chance','20 AED or 2 AED with a 50% chance', '24 AED or 0 AED with a 50% chance'],
            verbose_name='Please pick one of the following. At the end of the experiment this amount will be added to the rest of your payment. If you choose an option with an uncertain payment, the program will randomly choose either the higher or lower payment.',
            doc='Please pick one of the following.',
            widget=widgets.RadioSelect())

    q_riskpreference = models.CharField(
            initial=None,
            choices=['1','2','3','4','5','6','7','8','9','1'],
            verbose_name='Are you generally a person who is fully prepared to take risks or do you try to avoid taking risks?',
            doc='Are you generally a person who is fully prepared to take risks or do you try to avoid taking risks?',
            widget=widgets.RadioSelect())

    q_mathlevel = models.CharField(
        initial=None,
        choices=[
            'Pre-calculus',
            'Calculus',
            'Multivariable calculus',
            'Beyond multivariable calculus'
        ],
        verbose_name='What is the highest mathematics level you have taken thus far?',
        doc='What is the highest mathematics level you have taken thus far?',
        widget=widgets.RadioSelect())


    q_majordeclarationYN = models.CharField(
        initial=None,
        choices=[
        'Yes',
        'No'
        ],
        verbose_name='Have you declared your major?',
        doc='Have you declared your major?',
        widget=widgets.RadioSelect())

    q_expectedstudytrack = models.CharField(
        initial=None,
        choices=[
        'Arts and Humanities',
        'Engineering',
        'Multidisciplinary Track (Interactive Media, Arab Crossroads',
        'Science',
        'Social Science',
        ],
        verbose_name='What is your expected study track? Which of the academic divisions does your expectad major fall'
                     'under? If you are unsure, mark the division you are most interested in. If you plan to double'
                     'major, tick both.',
        doc='What is your expected study track? Which of the academic divisions does your expectad major fall under?'
            'If you are unsure, mark the division you are most interested in. If you plan to double major, tick both.',
        widget=widgets.RadioSelect())

    q_declaredstudytrack = models.CharField(
        initial=None,
        choices=[
        'Arts and Humanities',
        'Engineering',
        'Multidisciplinary Track (Interactive Media, Arab Crossroads',
        'Science',
        'Social Science',
        ],
        verbose_name='Which academic division does your major fall under?',
        doc='Which academic division does your major fall under?',
        widget=widgets.RadioSelect())

    q_gpastudytrack = models.CharField(
        initial=None,
        choices=[
        'Arts and Humanities',
        'Engineering',
        'Multidisciplinary Track (Interactive Media, Arab Crossroads',
        'Science',
        'Social Science',
        ],
        verbose_name='In which academic division do you think it is more difficult to receive a high GPA?'
                     'Rank these from 1 which means it is the most difficult to 5 which means it is least difficult to'
                     'receive a high GPA.',
        doc='In which academic division do you think it is more difficult to receive a high GPA?',
        widget=widgets.RadioSelect())

    q_profitablestudytrack = models.CharField(
        initial=None,
        choices=[
        'Arts and Humanities',
        'Engineering',
        'Multidisciplinary Track (Interactive Media, Arab Crossroads',
        'Science',
        'Social Science',
        ],
        verbose_name='With which academic background do you think a person would earn most in ten year’s time?'
                     'Rank the divisions from 1 to 5 where 1 means that they would earn most if they chose that'
                     'division and 5 that they would earn least if they chose that division.',
        doc='With which academic background do you think a person would earn most in ten year’s time?',
        widget=widgets.RadioSelect())

    q_mathlevelnyuad = models.CharField(
        initial=None,
        choices=[
        [1,'...in the top 25%?'],
        [2,'...in the top 25-50%?'],
        [3,'...in the top 50-75%?'],
        [4,'...in the bottom 25%?'],
        ],
        verbose_name='Compared to other NYUAD students, do you think your mathematics abilitiy is...',
        doc='Compared to other NYUAD students, do you think your mathematics abilitiy is...',
        widget=widgets.RadioSelect())

    q_passinggrade = models.CharField(
        initial=None,
        choices=[
        [1,""],
        [2,""],
        [3,""],
        [4,""],
        [5,""],
        [6,""],
        [7,""],
        [8,""],
        [9,""],
        [10,""],
        ],
        verbose_name='How difficult is it for you to get a passing grade in mathematics?'
                     'Please answer on a scale from 1 to 10 where 1 means very easy and 10 means very difficult.',
        doc='How difficult is it for you to get a passing grade in mathematics?'
            'Please answer on a scale from 1 to 10 where 1 means very easy and 10 means very difficult.',
        widget=widgets.RadioSelect())

    q_wealth = models.CharField(
        initial=None,
        choices=[
        [1,"very poor"],
        [2,"poor"],
        [3,"rather poor"],
        [4,"rather wealthy"],
        [5,"wealthy"],
        [6,"very wealthy"],
        ],
)

for key in Constants.ChoiceTable:
    Player.add_to_class(key,
        models.IntegerField(initial=None,
        choices=[
        [1,""],
        [2,""],
        [3,""],
        [4,""]
        ],
        verbose_name = Constants.ChoiceTable[key],
        doc = Constants.ChoiceTable[key] + str("""From a scale of 1 to 4 (1 = fully disagree, 4 = fully agree),
        please tell us how much you agree with the following statements:.""")
        ))
