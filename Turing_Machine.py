def unary_addition(tape):
    """
    Simulates a Turing Machine that adds two unary numbers separated by '+'.
    It simply replaces '+' with '1', thus appending the second unary number.
    """

    tape = list(tape)

    head = 0
    while head < len(tape):
        if tape[head] == '+':
            tape[head] = '1'  
            break
        head += 1

    return ''.join(tape)

input_tape = "111+11"
output_tape = unary_addition(input_tape)

print("Input:", input_tape)
print("Output:", output_tape)
