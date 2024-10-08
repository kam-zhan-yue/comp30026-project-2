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

# dfa1.show_diagram().draw('q2a_dfa1.png')
# dfa1.show_diagram().draw('q2a_dfa2.png')

class NFAWrapper:
    def __init__(self, initial_state: str, final_states: set[str]):
        self.states = set()
        self.input_symbols = set()
        self.transitions = {}
        self.initial_state = initial_state
        self.final_states = final_states
    
    def add_transition(self, state_1, i, state_2):
        # ensure that it is an initialised dictionary
        if state_1 not in self.transitions:
            self.transitions[state_1] = {}
        # add the new transition into the nfa transition dictionary
        if i in self.transitions[state_1]:
            self.transitions[state_1][i].add(state_2)
        else:
            self.transitions[state_1][i] = {state_2}

    def add_transitions(self, dfa_transitions):
        for state, transition in dfa_transitions.items():
            for i, t in transition.items():
                # add the new transition into the nfa transition dictionary
                self.add_transition(state, i, t)

    def update_dfa(self, dfa: DFA):
        self.states.update(dfa.states)
        self.input_symbols.update(dfa.input_symbols)
        self.add_transitions(dfa.transitions)
    
    def get_nfa(self) -> NFA:
        return NFA(
            states=self.states,
            input_symbols=self.input_symbols,
            transitions=self.transitions,
            initial_state=self.initial_state,
            final_states=self.final_states,
        )

def suffix_item(thing, suffix):
    return f'{thing}_{suffix}'

def suffix_list(original, suffix):
    return [suffix_item(thing, suffix) for thing in original]

def suffix_set(original, suffix):
    return set(suffix_list(original, suffix))

def suffix_transitions(original, suffix):
    new_transitions = {}
    for state, transitions in original.items():
        suffixed = suffix_item(state, suffix)
        new_transitions[suffixed] = {}
        for i, t in transitions.items():
            new_transitions[suffixed][i] = suffix_item(t, suffix)
    return new_transitions

def clone(dfa: DFA, suffix: str) -> DFA:
    return DFA(
        states=suffix_set(dfa.states, suffix),
        input_symbols=dfa.input_symbols,
        transitions=suffix_transitions(dfa.transitions, suffix),
        initial_state=suffix_item(dfa.initial_state, suffix),
        final_states=suffix_set(dfa.final_states, suffix),
    )

def q2b(a: DFA, b: DFA) -> NFA:
    # Create a secondary a and a new base for b
    a_2 = clone(a, '2')
    b_base = clone(b, 'base')

    # Initialse the NFA's parameters
    nfa_wrapper = NFAWrapper(a.initial_state, a_2.final_states)
    nfa_wrapper.update_dfa(a)
    nfa_wrapper.update_dfa(a_2)

    suffix = 0
    for state in a.states:
        # Create a clone of b_base
        b_branch = clone(b_base, suffix)

        nfa_wrapper.update_dfa(b_branch)

        # Create an epsilon transition from the current state to the start state of the branch
        nfa_wrapper.add_transition(state, '', b_branch.initial_state)

        # Create an epsilon transition from the final state of the branch to the corresponding state of a2
        for final_state in b_branch.final_states:
            nfa_wrapper.add_transition(final_state, '', suffix_item(state, '2'))
        suffix += 1
    
    return nfa_wrapper.get_nfa()

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

inputs = {
    '001100': True,
    '0011110000': True,
    '0': False,
    '01': False,
    '0001100': False,
}

nfa = q2b(dfa1, dfa2)

# Testing for sanity
nfa.show_diagram().draw('q2b.png')

for test in inputs:
    assert(nfa.accepts_input(test) == inputs[test])