from automata.pda.npda import NPDA

def q3a() -> NPDA:
    return NPDA(
        states={'q0', 'q1', 'q2', 'q3'},
        input_symbols={'a', 'b'},
        stack_symbols={'$', '#'},
        # transition state: {
        #    input: {
        #       top of stack: {(transition state, (pop from stack, put in stack))}
        #    }
        # }
        transitions={
            'q0': {
                # deterministically find the halfway point
                '': {
                    '$': {('q1', ('$'))},
                    '#': {('q1', ('#'))},
                },
                # if a, just push # into the stack
                'a': {
                    '$': {('q0', ('#', '$'))},
                    '#': {('q0', ('#', '#'))},
                },
                # if b, just push # into the stack
                'b': {
                    '$': {('q0', ('#', '$'))}, 
                    '#': {('q0', ('#', '#'))},
                },
            },
            # consume all the a's until encounter a b
            'q1': {
                # if encountered an a, just pop from stack
                'a': { '#': {('q1', (''))}},
                # if encountered a b, then transition to q2 and pop from stack
                'b': { '#': {('q2', (''))}},
            },
            'q2': {
                # pop a's and b's from the stack
                'a': { '#': {('q2', (''))}},
                'b': { '#': {('q2', (''))}},
                # at the end of the string, try to terminate
                '': { '$': {('q3', ('$'))}},
            },
        },
        initial_state='q0',
        initial_stack_symbol='$',
        final_states={'q3'},
        acceptance_mode='final_state',
    )


def q3b() -> str:
    return [
        ('S', ['ab', 'bb', 'aSa', 'bSa', 'bTb', 'aTb']),
        ('T', ['aa', 'bb', 'ab', 'ba', 'aTa', 'aTb', 'bTb', 'bTa']),
    ]