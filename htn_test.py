import pyhop 

"""
Small variation on Dana Nau's "travel from home to the park" example of 
hierarchal task network AI algorithm -- with plenty of pop culture snark. 

Utilizes Nau's pyhop hierarchal task network planner algorithm and a lot 
of spaghetti-coding. 
"""
def battery_loss(length_of_line, decay_rate):
	"""
	calculate how much Ah-nuld will lose while waiting for Singer. 
	"""
	decay = decay_rate["ah_nuld"]
	return (decay * length_of_line)

def register_for_event(state,a,x):
	"""
	Ah-nuld is in town and notices Singer is speaking today. 
	Seeking a chance to get his copy of Wired for War signed, Ah-nuld 
	registers online. 
	"""
	state.problem_state['at_new_america_foundation'] = x
	return state 

def wait_for_singer(state,a,x):
	"""
	Ah-nuld gets to the New America Foundation and plants himself awkwardly 
	in a chair.  
	"""
	if state.problem_state['at_new_america_foundation'] == x and state.problem_state[a]== x:
		state.problem_state['waiting_for_singer'] = x
		return state 
	else: return False 

def ask_for_autograph(state, a, x):
	"""
	If Ah-nuld has enough battery power, he can wait until 
	Singer is not occupied and politely ask for an autograph. 
	"""
	if state.problem_state['waiting_for_singer'] == x and state.problem_state[a] == x: 
		state.problem_state['ask_for_autograph'] = x
		return state 
	else: return False 

def play_terminator_music(state, a, x):
	"""
	Time's up. Ah-nuld plays the 'da dum dum dum' Terminator theme from his 
	onboard speakers to clear a path for his autograph.
	"""
	if state.problem_state['waiting_for_singer'] == x and state.problem_state[a] == x: 
		state.problem_state['play teh terminator music'] = x
		return state 
	else: return False 

def thank_singer_for_autograph(state,a):
	"""
	Ah-nuld is, if anything, unfailingly polite. 
	"""
	return state 

# all primitive operators 
pyhop.declare_operators(register_for_event, wait_for_singer, ask_for_autograph, play_terminator_music, thank_singer_for_autograph)
print('')
pyhop.print_operators() 

# all methods declared, each tied to calculation about battery loss.

def get_autograph_politely(state,a,x,y):
	if state.battery_power[a] > battery_loss(state.length_of_line[x][y], state.battery_decay_rate): 
		return [('register_for_event',a,x),('wait_for_singer',a,x),('ask_for_autograph',a,x),('thank_singer_for_autograph',a)]
	return False 
	
def hasta_la_vista_baby(state,a,x,y):
	if state.battery_power[a] < battery_loss(state.length_of_line[x][y], state.battery_decay_rate): 
		return [('register_for_event',a,x),('wait_for_singer',a,x),('play_terminator_music',a,x),('thank_singer_for_autograph',a)]
	return False 

pyhop.declare_methods('get_autograph', get_autograph_politely, hasta_la_vista_baby)
print('')
pyhop.print_methods()

print("""
********************************************************************************
Inputs
********************************************************************************

Arnold S. -- or rather, Ah-nuld the robot -- wants to get his copy of Wired 
for War autographed by PW Singer. But first Ah-nuld needs to get to the New 
America Foundation to see Singer talk. The metro ride alone is going to 
take a lot out of Ah-buld's battery power -- humans struggle to use WMATA 
all the time, and the same holds true for cyborgs with thick Austrian 
accents and a willingness to be ordered around by Edward Furlong. 

By the time Ah-nuld gets to the PW Singer talk, he will have lost a lot of 
power and will be subsisting on reserves. Ah-nuld still needs to brave a 
potentially long line to be able to get his Wired for War copy signed and 
autographed. Luckily, Arnold has a nifty little thing called a 
Hierarchal Task Network (HTN) algorithm. Arnold can decompose the larger 
problem of getting an autograph into smaller pieces. Consult Nau and Au 
2003) for more details, but the most important thing is that Ah-nuld 
suddenly has a solution to solving a complex AI planning problem with 
multiple levels of abstraction.

Let us assume that battery loss = (length of line to see Singer)(battery 
decay rate). If Ah-nuld can afford the battery expenditure, he'll patiently 
wait for Singer to become available and then politely ask for an autograph. 
If Ah-nuld doesn't have enough battery power he might just get impatient and 
blast the Terminator theme music to scare everyone away, thus allowing him 
to bypass the line and collect his autograph. 

You can determine Ah-nuld's choices by specifying his max battery power, the 
number of people in front of him in line, and the rate at which his battery 
decays. 
""") 

print("""
********************************************************************************
Inputs
********************************************************************************
""")

line_length = int(input("enter integer for line length: ")) 
robot_battery_power = int(input("enter int for Ah-nuld battery power: "))
robot_battery_decay_rate = int(input("enter int for Ah-nuld battery decay rate: "))


# initialize all ah-nuld inputs
state1 = pyhop.State('state1')
state1.problem_state = {'ah_nuld':'no_autograph'}
state1.length_of_line = {'no_autograph':{'book_signed':line_length}, 'book_signed':{'no_autograph':line_length}}
state1.battery_power = {'ah_nuld':robot_battery_power}
state1.required_battery_expenditure = {'ah-nuld':0}
state1.battery_decay_rate = {'ah_nuld':robot_battery_decay_rate}

print("""
********************************************************************************
Call pyhop.pyhop(state1,[('get_autograph,'ah_nuld','no_autograph','book_signed')]) with different verbosity levels
********************************************************************************
""")

print("- If verbose=0 (the default), Pyhop returns the solution but prints nothing.\n")
pyhop.pyhop(state1,[('get_autogragh','ah_nuld','no_autograph','book_signed')])

print('- If verbose=1, Pyhop prints the problem and solution, and returns the solution:')
pyhop.pyhop(state1,[('get_autograph','ah_nuld','no_autograph','book_signed')],verbose=1)

print('- If verbose=2, Pyhop also prints a note at each recursive call:')
pyhop.pyhop(state1,[('get_autograph','ah_nuld','no_autograph','book_signed')],verbose=2)

print('- If verbose=3, Pyhop also prints the intermediate states:')
pyhop.pyhop(state1,[('get_autograph','ah_nuld','no_autograph','book_signed')],verbose=3)
