from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from automata.regex.regex import issubset

def q2a() -> str:
    return '0'

q2a_regex = "(00)*(11)*(00)*"

# NFA which matches strings beginning with "a", ending with "a", and
# containing no consecutive "b"s
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

def q2b(a: DFA, b: DFA) -> NFA:
    states = set(a.states)
    other_states = set(b.states)
    states.update(other_states)

    inputs = set(a.input_symbols)
    other_inputs = set(b.input_symbols)
    inputs.update(other_inputs)

    print("States", states)
    print("Inputs", inputs)
    
    return NFA(
        states=states,
        input_symbols=inputs,
        transitions={

        }
    )

q2b(dfa1, dfa2)