Ahnuld_AI_Planner
==============================

# Summary 

A rather snarky attempt to play around with hierarchal task network planning algorithms and make fun of the DC metro. I hacked Dana Nau's simple travel example of HTN planning to detail a situation in a cybernetically enhanced Austrian wants to get his copy of *Wired for War* signed and autographed -- and he won't take no for an answer. Most of the edits I've done have been in problem operators and methods -- haven't touched hard code of Nau's SHOP implementation in Python. 

# Theory 

I was interested in exploring HTN systems, described (Nau *et al.* 2003) [as follows](https://www.jair.org/media/1141/live-1141-2152-jair.pdf):

>HTN planning is like classical AI planning in that each state of the world is represented by a set of atoms, and each action corresponds to a deterministic state transition. However, HTN planners differ from classical AI planners in what they plan for, and how they plan for it.The objective of an HTN planner is to produce a sequence of actions that perform some activity or task. The description of a planning domain includes a set of operators similar to those of classical planning, and also a set of methods, each of which is a prescription for how to decompose a task into subtasks (smaller tasks). Given a planning domain, the description of a planning problem will contain an initial state like that of classical planning -- but instead of a goal formula, the problem specification will contain a partially ordered set of tasks to accomplish. Planning proceeds by using the methods to decompose tasks recursively into smaller and smaller subtasks, until the planner reaches primitive tasks that can be performed directly using the planning operators.

Since I'm interested in using HTN for something I'm building in Python, I decided to find a Python implementation. I'm not entirely sure I understand Nau's [Python version](https://bitbucket.org/dananau/pyhop) of the [SHOP](http://www.cs.umd.edu/~nau/papers/nau2013game.pdf) algorithm, but it was fun to work with. Also found this of interest: 

>Pyhop represents states of the world using ordinary variable bindings, not logical propositions. A state is just a Python object that contains the variable bindings. For example, you might write s.loc['v'] = 'd' to say that vehicle v is at location d in state s. To write HTN operators and methods for Pyhop, you don't need to learn a specialized planning language. Instead, you write them as ordinary Python functions. The current state (e.g., s in the above example) is passed to them as an argument. 

That's both something interesting -- a substitute for Lisp and Prolog-style programming -- but also something that takes some getting used to. 

# Notes

As high-minded as this may sound, the most fun I got out of it was imagining a scenario in which Ah-nuld is out to get P.W. Singer to sign a personal copy of *Wired for War*. It provided an opportunity to implement some simple methods for decomposing Ah-nuld's decision-making into sequences that accomplished his goal. I've implemented some basic command line input and a hefty intro screen that documents the scenario and its various inputs. 

All output will be returned as a sequence of plan operators. For ex, Nau's original example has the sequence `result = [('call_taxi', 'me', 'home'), ('ride_taxi', 'me', 'home', 'park'), ('pay_driver', 'me')]`. Run the file `htn_test.py` to begin the process, but make sure that the original `pyhop` file is in the same directory. 





