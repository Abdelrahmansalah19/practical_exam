
nfa = {
    'states': {'q0', 'q1', 'q2'}, 
    'symbols': {'a', 'b'},         
    'transitions': {              
        'q0': {'ε': {'q1', 'q2'}},  
        'q1': {'a': {'q1'}},
        'q2': {'b': {'q2'}}
    },
    'start': 'q0',                
    'finals': {'q1'}              
}

def epsilon_closure(state, transitions):
    stack = [state]
    closure = {state}
    while stack:
        s = stack.pop()
        for t in transitions.get(s, {}).get('ε', set()):
            if t not in closure:
                closure.add(t)
                stack.append(t)
    return closure

def epsilon_closure_set(states, transitions):
    result = set()
    for state in states:
        result |= epsilon_closure(state, transitions)
    return result

def move(states, symbol, transitions):
    result = set()
    for state in states:
        result |= transitions.get(state, {}).get(symbol, set())
    return result

def nfa_to_dfa(nfa):
    dfa_states = []            
    dfa_transitions = {}       
    state_map = {}             

    start_closure = frozenset(epsilon_closure(nfa['start'], nfa['transitions']))
    state_map[start_closure] = 'A'
    dfa_states.append(start_closure)
    queue = [start_closure]    
    next_label = ord('B')      

    while queue:
        current = queue.pop(0)
        label = state_map[current]
        dfa_transitions[label] = {}

        for symbol in nfa['symbols']:
            move_result = move(current, symbol, nfa['transitions'])
            closure = epsilon_closure_set(move_result, nfa['transitions'])
            if not closure:
                continue
            closure_frozen = frozenset(closure)
            if closure_frozen not in state_map:
                state_map[closure_frozen] = chr(next_label)
                next_label += 1
                queue.append(closure_frozen)
            dfa_transitions[label][symbol] = state_map[closure_frozen]

    final_states = {state_map[s] for s in state_map if nfa['finals'] & s}

    return {
        'states': list(state_map.values()),
        'start': 'A',
        'finals': list(final_states),
        'transitions': dfa_transitions
    }

dfa = nfa_to_dfa(nfa)
print("\n--- DFA Result ---")
print("States:", dfa['states'])
print("Start State:", dfa['start'])
print("Final States:", dfa['finals'])
print("Transitions:")
for state in dfa['transitions']:
    print(f"  {state}: {dfa['transitions'][state]}")
