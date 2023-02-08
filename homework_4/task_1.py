snake = input()

def to_capitalized_words(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components[0:])

print(to_capitalized_words(snake))

#по заданию понял что нужно вводить уже в снейк кейсе