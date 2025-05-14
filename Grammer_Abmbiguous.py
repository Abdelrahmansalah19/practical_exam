# Define a sample grammar
# Grammar: S -> S + S | S * S | a
grammar = {
    'S': [['S', '+', 'S'], ['S', '*', 'S'], ['a']]
}

def generate_trees(string, symbol, grammar):

    if not string:
        return []

    if symbol not in grammar:
        return [[symbol]] if string == symbol else []

    trees = []  

    for productions in grammar[symbol]:
        if len(productions) == 1:
            if string == productions[0]:
                trees.append([symbol, productions[0]])
        elif len(productions) == 3:
            for x in range(1, len(string) - 1):
                left = string[:x]
                middle = string[x]
                right = string[x+1:]

                if middle != productions[1]:
                    continue  

                left_trees = generate_trees(left, productions[0], grammar)
                right_trees = generate_trees(right, productions[2], grammar)

                for lt in left_trees:
                    for rt in right_trees:
                        trees.append([symbol, lt, middle, rt])
    return trees

input_str = "a+a+a"
parse_trees = generate_trees(input_str, 'S', grammar)

print(f"Number of parse trees: {len(parse_trees)}")
print("Grammar is ambiguous" if len(parse_trees) > 1 else "Grammar is unambiguous")
