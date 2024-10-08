from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from automata.regex.regex import issubset

def q2a() -> str:
    return '0'

# Hardcoded regex of the injection
q2a_regex = "(00)*(11)*(00)*"

# Test out the NFA provided in the assignment
nfa = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q1'}, '1': {'q2'}, '': {'q3'}},
        'q1': {'0': {'q0'}, '1': {'q2'}, '': {'q3'}},
        'q2': {'0': {'q2'}, '1': {'q2'}, '': {'q3'}},
        'q3': {'0': {'q5'}, '1': {'q4'}, '': {'q0', 'q1', 'q2'}},
        'q4': {'0': {'q5'}, '1': {'q3'}},
        'q5': {'0': {'q5'}, '1': {'q5'}},
    },
    initial_state="q0",
    final_states={"q0"},
)

# Testing for sanity
nfa.show_diagram().draw('q2a.png')
assert(nfa.accepts_input(q2a()))
assert(issubset(q2a(), q2a_regex) == False)


dfa1 = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q1', '1': 'q2'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q2'},
    },
    initial_state='q0',
    final_states={'q0'}
)

dfa2 = DFA(
    states={'q3', 'q4', 'q5'},
    input_symbols={'0', '1'},
    transitions={
        'q3': {'0': 'q5', '1': 'q4'},
        'q4': {'0': 'q5', '1': 'q3'},
        'q5': {'0': 'q5', '1': 'q5'},
    },
    initial_state='q3',
    final_states={'q3'}
)

# dfa1.show_diagram().draw('q2a_dfa1.png')
# dfa1.show_diagram().draw('q2a_dfa2.png')

inputs = {
    '001100': True,
    '0011110000': True,
    '0': False,
    '01': False,
}

def suffix_item(thing, suffix):
    return f'{thing}_{suffix}'

def suffix_list(original, suffix):
    return [suffix_item(thing, suffix) for thing in original]

def suffix_transitions(original, suffix):
    new_transitions = {}
    for state, transitions in original.items():
        suffixed = suffix_item(state, suffix)
        new_transitions[suffixed] = {}
        for i, t in transitions.items():
            new_transitions[suffixed][i] = suffix_item(t, suffix)
    return new_transitions

def add_transitions(nfa_transitions, dfa_transitions):
    for state, transition in dfa_transitions.items():
        for i, t in transition.items():
            # check if the nfa transition dictionary is empty
            if state not in nfa_transitions:
                nfa_transitions[state] = {}
            
            # add the new transition into the nfa transition dictionary
            if i in nfa_transitions[state]:
                nfa_transitions[state][i].add(t)
            else:
                nfa_transitions[state][i] = {t}

def q2b(a: DFA, b: DFA) -> NFA:
    states = set(a.states)
    other_states = set(b.states)
    states.update(other_states)

    # for every state in 
    # first clone a into a2
    # need to combine the input symbols, make sure they are updated
    a2_states = suffix_list(a.states, 2)
    a2_transitions = suffix_transitions(a.transitions, 2)

    suffix = 0
    nfa_transitions = {}
    add_transitions(nfa_transitions, a.transitions)
    add_transitions(nfa_transitions, a2_transitions)



    for state, transitions in a.transitions.items():
        branch = suffix_transitions(b.transitions, suffix)

        print(state)

    print(nfa_transitions)
    return None

q2b(dfa1, dfa2)