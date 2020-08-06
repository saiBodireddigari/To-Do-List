iris = {}


def add_iris(id_n, species, petal_length, petal_width, **other_features):
    iris[id_n] = {
        'species': species,
        'petal_length': petal_length,
        'petal_width': petal_width}
    for feature, value in other_features.items():
        iris[id_n][feature] = value
    return iris
