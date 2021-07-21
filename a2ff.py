'''a2ff.py
by Sonia Fereidooni
UWNetIDs: fereison
Student numbers: 1960788

Assignment 2, in CSE 473, Autumn 2020.

Part A
 
This file contains our problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''

# Put your formulation of the Farmer-Fox-Chicken-and-Grain problem here.
# Be sure your name, uwnetid, and 7-digit student number are given above in 
# the format shown.

#<METADATA>
SOLUZION_VERSION = "2.0"
PROBLEM_NAME = "Farmer-Fox-Chicken-Grain"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHORS = ['S. Fereidooni']
PROBLEM_CREATION_DATE = "22-OCT-2020"

# The following field is mainly for the human solver, via either the Text_SOLUZION_Client.
# or the SVG graphics client.
PROBLEM_DESC=\
 '''The <b>"Farmer-Fox-Chicken-Grain"</b> problem is a traditional puzzle where there is a river
 with a left and right bank opposite to each other. A farmer wants to cross this bank with his
 fox, chicken, and grain, but cannot leave the fox alone with the chicken, or the chicken alone with 
 the grain. The farmer must bring one of his three entities on his boat with him to the other side of
 the bank, and the farmer must always be present if the boat is being moved from one side of the bank
 to the other. The farmer can only bring one entity with him at a time (if he chooses to bring one at all)
 whenever he crosses the river. The farmer is trying to safely cross all his possessions from the 
 left side of the river bank to the right bank of the river.

'''
#</METADATA>

#<COMMON_DATA>
Farmer, Fox, Chicken, Grain = 0, 1, 2, 3
PEOPLE = [Farmer, Fox, Chicken, Grain]
left, right = 0, 1
LOCATIONS = [left, right]
#</COMMON_DATA>

#<COMMON_CODE>

class State():

  def __init__(self, d = None):
    self.d = d

  def __eq__(self, s2):
    for bank in LOCATIONS:
      for person in self.d[bank]:
        if (not (person in s2.d[bank])):
          return False
    return True

  def __str__(self):
    txt = "\n People in left bank (starting position):"
    for p in self.d[left]:
      if p == 0: txt += " Farmer"
      elif p == 1: txt += " Fox"
      elif p == 2: txt += " Chicken"
      elif p == 3: txt += " Grain"
    txt += "\n People in right bank (destination):"
    for p in self.d[right]:
      if p == 0: txt += " Farmer"
      elif p == 1: txt += " Fox"
      elif p == 2: txt += " Chicken"
      elif p == 3: txt += " Grain"
    return txt

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State([])
    news_left, news_right = [], []
    for people in self.d[left]:
      news_left.append(people)
    for people in self.d[right]:
      news_right.append(people)
    news.d.append(news_left)
    news.d.append(news_right)
    return news

  # takes in two arrays of what is being MOVED to left bank and right bank
  def can_move(self, l, r):
    '''Tests whether it's legal to move the boat and take
     certain person with (or without) farmer.'''
    # check that boat starting position is correct
    if (Farmer in self.d[left] and Farmer in l) or \
            (Farmer in self.d[right] and Farmer in r):
      return False
    # check that there are max 2 people in the boat being moved simultaneously
    if len(l) > 2 or len(r) > 2:
      return False
    # check that boat is moving to one bank direction per move
    if len(l) != 0 and len(r) != 0:
      return False
    # check that objects are being moved only once in the round
    for person in PEOPLE:
      if person in l and person in r:
        return False
    # check that farmer is also being moved
    if (not Farmer in l) and (not Farmer in r):
      return False
    # chicken can't be left alone with grain
    new_right, new_left = self.d[right][:], self.d[left][:]
    for person in r:
      if person in self.d[left]:
        new_left.remove(person)
        new_right.append(person)
    for person in l:
      if person in self.d[right]:
        new_right.remove(person)
        new_left.append(person)
    if (Chicken in new_right and Grain in new_right and (not Farmer in new_right)):
      return False
    if (Chicken in new_left and Grain in new_left and (not Farmer in new_left)):
      return False
    # fox can't be left alone with chicken
    if (Fox in new_right and Chicken in new_right and (not Farmer in new_right)):
      return False
    if (Fox in new_left and Chicken in new_left and (not Farmer in new_left)):
      return False
    return True

  # takes in two arrays of what is being MOVED to left bank and right bank
  def move(self, l, r):
    '''Assuming it's legal to make the move, this computes
     the new state resulting from moving the combination
     of chosen passengers from one side of the bank to the other.'''
    news = self.copy()
    for person in l:
      if person in news.d[right]:
        news.d[right].remove(person)
        news.d[left].append(person)
    for person in r:
      if person in news.d[left]:
        news.d[left].remove(person)
        news.d[right].append(person)
    return news

def goal_test(s):
  '''If all the people including the farmer are on the right bank of the river.'''
  # goal state = {'left':[], 'right':[Farmer, Fox, Chicken, Grain]}
  if len(s.d[left]) != 0:
    return False
  if len(s.d[right]) != 4:
    return False
  return (Farmer in s.d[right] and Fox in s.d[right]
          and Chicken in s.d[right] and Grain in s.d[right])

def goal_message(s):
  return "Congratulations on getting the farmer, fox, chicken, and grain to the right riverbank!"

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
CREATE_INITIAL_STATE = lambda : State(d=[[Farmer, Fox, Chicken, Grain], []]) # FIX THIS
#</INITIAL_STATE>

#<OPERATORS>
combinations = [([], [0]), ([], [0,1]), ([], [0,2]), ([], [0,3]), # boat moving to right
                ([0], []), ([0,1], []), ([0,2], []), ([0,3], [])] # boat moving to left

# FIX THIS
OPERATORS = [Operator(
  "Move Farmer" + str(lambda l, r: " and Fox" if (Fox in l or Fox in r) else "") +
  str(lambda l, r: " and Chicken" if (Chicken in l or Chicken in r) else "") +
  str(lambda l, r: " and Grain" if (Grain in l or Grain in r) else "") +  " from " +
  str(lambda l, r: "left to right" if len(l) == 0 else ("right to left")),
  lambda s, l1=l, r1 = r: s.can_move(l1, r1),
  lambda s, l1=l, r1 = r: s.move(l1,r1) )
  for (l,r) in combinations]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>
