import pyhop 

def write_email(state,a,x,y):
	if state.problem_state[a] == x: 
		state.problem_state[a] = y
		return state 
	else: return False 

def move_to_singer(state, a, x):
	state.problem_state['singer'] = x
	return state 

def ask_for_autograph(state, a, x, y):
	if state.problem_state['singer'] == x and state.problem_state == x: 
		state.problem_state['singer'] = y
		state.problem_state[a] = y
		state.required_number_of_cards_to_give = 1
		return state
	else: return False 

def give_singer_card(state,a):
	if state.robot_business_cards >= state.required_number_of_cards_to_give[a]:
		state.robot_business_cards[a] = state.robot_business_cards[a] - state.required_number_of_cards_to_give[a]
		state.required_number_of_cards_to_give[a] = 0 
		return state 
	else: return False 

pyhop.declare_operators(write_email, move_to_merchandise_table, ask_for_autograph, give_singer_card)
print('')
pyhop.print_operators()

def write_singer_a_email(state, a, x, y):
	"""
	If robot thinks too many people are talking to Singer and Singer unlikely to move, 
	just write him an email requesting a sit-down as to avoid waiting for autogragh signing
	"""
	if state.threshold_of_people_talking_to_singer < 3: 
		return [('write_email'),a,x,y)]
	return False 

def move_to_merchandise_table(state, a, x, y):
	if state.threshold_of_people_talking_to_singer => 3: 
		return [('move_to_singer'),a,x), ('ask_for_autograph', a, x, y), ('give_singer_card', a)]
	return False 

pyhop.declare_methods('get P.W. Singer autograph',write_singer_a_email, move_to_merchandise_table)
print('')
pyhop.print_methods()

""" State information 

Creates a state object and implements state 
values as key-value pairs. 
"""

state1 = pyhop.State('state1')
state1.problem_state = {'robot':'at_event'}
state1.threshold_of_people_talking_to_singer = {'robot':3}
state1.robot_business_cards = {'robot':5}
state1.required_number_of_cards_to_give = {'robot':0}

print("""
********************************************************************************
Call pyhop.pyhop(state1,[('get P.W. Singer autograph,'robot','at_event','book_signed')]) with different verbosity levels
********************************************************************************
""")

print("- If verbose=0 (the default), Pyhop returns the solution but prints nothing.\n")
pyhop.pyhop(state1,[('get P.W. Singer autograph','robot','ticket','book signed')])

print('- If verbose=1, Pyhop prints the problem and solution, and returns the solution:')
pyhop.pyhop(state1,[('get P.W. Singer autograph','robot','ticket','book signed')],verbose=1)

print('- If verbose=2, Pyhop also prints a note at each recursive call:')
pyhop.pyhop(state1,[('get P.W. Singer autograph','robot','ticket','book signed')],verbose=2)

print('- If verbose=3, Pyhop also prints the intermediate states:')
pyhop.pyhop(state1,[('get P.W. Singer autograph','robot','ticket','book signed')],verbose=3)