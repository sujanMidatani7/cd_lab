def shift_reduce_parser(grammar, input_string):
    stack = []
    input_buffer = list(input_string)
    actions = []
    while input_buffer:
        reduced = False
        for nonterminal, production in grammar.items():
            for p in production:
                # print(nonterminal,stack[-len(p):],list(p))
                if stack[-len(p):] == list(p):
                    
                    reduced = True
                    for _ in range(len(p)):
                        stack.pop()
                    stack.append(nonterminal)
                    actions.append((stack[:], input_buffer[:], f'Reduce: {nonterminal} -> {p}'))
                    break
            if reduced:
                break
        if reduced:
            continue
        stack.append(input_buffer.pop(0))
        actions.append((stack[:], input_buffer[:], 'Shift'))
        # print(actions)
    for stack_state, input_buffer_state, action in actions:
        print(f'Stack: {" ".join(stack_state)}, Input Buffer: {" ".join(input_buffer_state)}, Action: {action}')
gram = {
    "E": ["2E2", "3E3", "4"]
}
# gram = {
#     "S": ["aABc"],
#     "A": ["Abc", "b"],
#     "B": ["d"]
# }
# input_str="ab"
# print(gram.items())
input_str = "2324232$"
shift_reduce_parser(gram, input_str)