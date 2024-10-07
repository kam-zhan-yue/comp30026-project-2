from automata.fa.dfa import DFA
from automata.regex.regex import validate, issubset

inputs = {
    '0000100': True,
    '00100100001000111': True,
    '11001111001': True,
    '000': False,
    '1100001': False,
    '00001': False,
    '110000': False,
    '0101010101': False,
}

def q1a() -> DFA:
    return DFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
        input_symbols={'0', '1'},
        transitions={
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q2', '1': 'q0'},
            'q2': {'0': 'q1', '1': 'q3'},
            'q3': {'0': 'q4', '1': 'q3'},
            'q4': {'0': 'q5', '1': 'q3'},
            'q5': {'0': 'q4', '1': 'q6'},
            'q6': {'0': 'q6', '1': 'q6'},
        },
        initial_state='q0',
        final_states={'q5', 'q6'}
    )

# Q1 Testing
dfa = q1a()
dfa.show_diagram().draw('q1a.png')
for test in inputs:
    assert(dfa.accepts_input(test) == inputs[test])

def q1b() -> str:
    return "(1*0*)*(00)+1+(1*0*)*(00)+(1*0*)*"

# Q2 Testing
assert(validate(q1b()) == None)
for test in inputs:
    assert(issubset(test, q1b()) == inputs[test])
