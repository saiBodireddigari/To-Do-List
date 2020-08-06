def select_dates(potential_dates):

    names = [dic.get("name") for dic in potential_dates if dic.get("age") > 30 and dic.get("city") == 'Berlin' and "art" in dic.get("hobbies")]
    return str(", ".join(names))
