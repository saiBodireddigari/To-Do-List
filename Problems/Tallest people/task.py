def tallest_people(**people):
    max_height = max(list(people.values()))
    for key, value in sorted(people.items()):
        if value == max_height:
            print(f'{key} : {max_height}')