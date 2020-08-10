def morning(greetings):
    def wrapper(name):
        greetings(name)
        print(f'Good morning, {name}')

    return wrapper
