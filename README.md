# Formal Languages & Automata Exercises

This repository contains solutions for three practical automata theory problems:

1. **Convert NFA (with ε-transitions) to DFA**
2. **Check CFG Ambiguity**
3. **Simulate a Turing Machine that adds two unary numbers**

---

## Task 1: NFA to DFA Conversion

### File:
```
nfa_to_dfa.py
```

### Description:
Converts a nondeterministic finite automaton (NFA) with epsilon transitions into a deterministic finite automaton (DFA) using the subset construction algorithm.

### How to Run:
```bash
python nfa_to_dfa.py
```

### Expected Output:
- List of DFA states
- Start and final states
- Transition table in readable format

---

##  Task 2: CFG Ambiguity Checker

### File:
```
cfg_ambiguity_checker.py
```

### Description:
Checks whether a context-free grammar is ambiguous for a given input string by generating all possible parse trees.

### How to Run:
```bash
python cfg_ambiguity_checker.py
```

### Expected Output:
- Number of parse trees generated
- Whether the grammar is ambiguous for that string

---

##  Task 3: Unary Addition Turing Machine

### File:
```
unary_turing_machine.py
```

### Description:
Simulates a Turing Machine that computes the sum of two unary numbers (represented by `1`s) separated by a `+`.

### How to Run:
```bash
python unary_turing_machine.py
```

### Expected Output:
- Input: `111+11`
- Output: `11111`

---

## Requirements
No external libraries required. All scripts are written in **pure Python**.


