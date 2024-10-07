from automata.fa.dfa import DFA

def q1a() -> DFA:
    return DFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
        input_symbols={'0', '1'},
        transitions={
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q2', '1': 'q0'},
            'q2': {'0': 'q1', '1': 'q3'},
            'q3': {'0': 'q4', '1': 'q3'},
            'q4': {'0': 'q5', '1': 'q3'},
            'q5': {'0': 'q4', '1': 'q5'},
        },
        initial_state='q0',
        final_states={'q5'}
    )

q1a = q1a()
q1a.show_diagram().draw('q1a.png')
print(q1a.accepts_input('0000100'))
print(q1a.accepts_input('000'))
print(q1a.accepts_input('00100100001000111'))