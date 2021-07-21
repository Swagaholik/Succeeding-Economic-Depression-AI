'''a2wp.py
by Sonia Fereidooni
UWNetIDs: fereison
Student numbers: 1960788

Assignment 2, in CSE 473, Autumn 2020.
PART B
 
This file contains our problem formulation for the problem of
avoiding a severe economic depression in the United States.
'''

# Put your formulation of your chosen wicked problem here.
# Be sure your name, uwnetid, and 7-digit student number are given above in 
# the format shown.

#<METADATA>
SOLUZION_VERSION = "2.0"
PROBLEM_NAME = "Avoiding a severe economic depression in the United States"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHORS = ['S. Fereidooni']
PROBLEM_CREATION_DATE = "22-Oct-2020"

# The following field is mainly for the human solver, via either the Text_SOLUZION_Client.
# or the SVG graphics client.
PROBLEM_DESC=\
 '''The <b>"severe US economic depression"</b> problem is modeled around the Great Depression
 of the late 20s to early 30s, as well as the 2008 economic recession. For this wicked problem, 
 we will start at a state where the US is undergoing severe economic depression (we have unemployment and 
 inflation rates high enough that constitute those of an economic depression). Our goal state is
 to try and reduce both of these rates (unemployment and inflation) until we are at economic upswing standards. 
 Our goal is to try and reach this goal state in the least number of years (starting at the year 2020). 
 Each year, we are given three options of actions to take in order to reduce either the country's
 unemployment rate (which may increase the country's inflation rate) or reduce the country's 
 inflation rate (which may increase the country's unemployment rate). When we reach the unemployment 
 rate and inflation rate of economic upswing standards (opposite of economic depression), then we win. The 
 three options we have to choose from every year is to increase government spending (which will decrease
 unemployment and increase inflation rates), invest in banks (which will increase unemployment and decrease
 inflation rates), and reduce taxes (which will decrease unemployment and increase inflation). Some rules
 that must be followed when choosing an action every year are that (1) the government cannot choose to make the
 same action every year, (2) the unemployment rate cannot spill over a 20% threshold, and (3) the inflation 
 rate cannot spill over a 15% threshold, (4) if a certain rate is already below the threshold for economic
 upswing then we must choose the action that prioritizes the reduction of the other rate. 

'''
#</METADATA>

#<COMMON_DATA>
INCREASE_GOVT_SPENDING = [-1.5, 0.6]
INVEST_IN_BANKS = [0.4, -2.2]
REDUCE_TAXES = [-1.9, 0.8]
UNEMPLOYMENT_RATE, INFLATION_RATE, LAST_ACTION = 0, 1, 2
STATS = [UNEMPLOYMENT_RATE, INFLATION_RATE, LAST_ACTION]
#</COMMON_DATA>

#<COMMON_CODE>

class State():

  def __init__(self, d=None):
    self.d = d

  def __eq__(self, s2):
    for factor in STATS:
      if self.d[factor] != s2.d[factor]: return False
    return True

  def __str__(self):
    txt = "\n Current Unemployment Rate: " + str(self.d[UNEMPLOYMENT_RATE]) + "%"
    txt += "\n Current Inflation Rate: " + str(self.d[INFLATION_RATE]) + "%"
    txt += "\n Last Government Action Taken: "
    if (self.d[LAST_ACTION] == INCREASE_GOVT_SPENDING):
      txt += "Increase Government Spending to Increase Welfare"
    elif self.d[LAST_ACTION] == INVEST_IN_BANKS:
      txt += "Invest in Banks for Financial Stability"
    elif self.d[LAST_ACTION] == REDUCE_TAXES:
      txt += "Reduce Taxes to Stimulate Consumer Spending"
    return txt

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    news = State([])
    for factor in STATS:
      news.d.append(self.d[factor])
    return news

  def can_move(self, action):
    '''Tests whether it's legal to perform the action
    without going further down into depression (passing severe
    depression rate thresholds for either unemployment or inflation).'''
    print(self)
    # check if government is choosing same action two years in a row
    if (action == self.d[LAST_ACTION]):
      return False
    # check if action will go over unemployment or inflation rate thresholds
    if (action[UNEMPLOYMENT_RATE] + self.d[UNEMPLOYMENT_RATE] >= 20.0 or
            action[INFLATION_RATE] + self.d[INFLATION_RATE] >= 15.0):
      return False
    if (self.d[UNEMPLOYMENT_RATE] <= 2.50 and not (action == INVEST_IN_BANKS)
            and not (self.d[INFLATION_RATE] <= -10.00)):
      return False
    if (self.d[INFLATION_RATE] <= -10.00 and not
    (action == INCREASE_GOVT_SPENDING or action == REDUCE_TAXES)
            and not (self.d[UNEMPLOYMENT_RATE] <= 2.50)):
      return False
    return True

  def move(self, action):
    '''Assuming it's legal to make the move, this computes
     the new state resulting from performing the chosen
     government action this year.'''
    news = self.copy()
    news.d[UNEMPLOYMENT_RATE] += action[UNEMPLOYMENT_RATE]
    news.d[INFLATION_RATE] += action[INFLATION_RATE]
    news.d[LAST_ACTION] = action
    return news

def goal_test(s):
  return s.d[UNEMPLOYMENT_RATE] <= 2.50 and s.d[INFLATION_RATE] <= -10.00

def goal_message(s):
  return "You saved us from another economic depression! Thank you!" # CHANGE THE MESSAGE

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
CREATE_INITIAL_STATE = lambda : State(d=[15,3, -1]) # FIX THIS
#</INITIAL_STATE>

#<OPERATORS>
GOVERNMENT_ACTIONS = [INCREASE_GOVT_SPENDING, INVEST_IN_BANKS, REDUCE_TAXES]

OPERATORS = [Operator(
  "This year the government will " +
  str(lambda action: "increase government spending" if (action == 0) else "") +
  str(lambda action: "invest in banks" if (action == 1) else "") +
  str(lambda action: "reduce taxes" if (action == 2) else "") + ".",
  lambda s, action1 = action: s.can_move(action1),
  lambda s, action1 = action: s.move(action1) )
  for (action) in GOVERNMENT_ACTIONS]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>
