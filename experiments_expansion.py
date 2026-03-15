from modules.expansion import FooocusExpansion  # type: ignore

expansion = FooocusExpansion()

text = 'a handsome man'

for i in range(64):
    print(expansion(text, seed=i))
