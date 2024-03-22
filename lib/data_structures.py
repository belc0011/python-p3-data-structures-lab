spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for dict in spicy_foods:
        names.append(dict.get('name'))
    return names

def get_spiciest_foods(spicy_foods):
    list_of_dicts = []
    for dict in spicy_foods:
        if dict.get('heat_level') > 5:
            list_of_dicts.append(dict)
    return list_of_dicts

def print_spicy_foods(spicy_foods):
    spicy_level = ""
    for dict in spicy_foods:
        if dict.get('heat_level') == 1:
            spiciness = '🌶'
        elif dict.get('heat_level') == 2:
            spiciness = "🌶🌶"
        elif dict.get('heat_level') == 3:
            spiciness = "🌶🌶🌶"
        elif dict.get('heat_level') == 4:
            spiciness = "🌶🌶🌶🌶"
        elif dict.get('heat_level') == 5:
            spiciness = "🌶🌶🌶🌶🌶"
        elif dict.get('heat_level') == 6:
            spiciness = "🌶🌶🌶🌶🌶🌶"
        elif dict.get('heat_level') == 7:
            spiciness = "🌶🌶🌶🌶🌶🌶🌶"
        elif dict.get('heat_level') == 8:
            spiciness = "🌶🌶🌶🌶🌶🌶🌶🌶"
        else:
            spiciness = "🌶🌶🌶🌶🌶🌶🌶🌶🌶"
        print(f"{dict.get('name')}" + f" ({dict.get('cuisine')})" + f" | Heat Level: {spiciness}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    found_match = {}
    for dict in spicy_foods:
        if dict['cuisine'] == cuisine:
            found_match = dict
    return found_match

def print_spiciest_foods(spicy_foods):
    new_list = []
    for dict in spicy_foods:
        if dict['heat_level'] > 5:
            new_list.append(dict)
    print_spicy_foods(new_list)

def get_average_heat_level(spicy_foods):
    running_total = 0
    num_foods = 0
    for dict in spicy_foods:
        running_total += dict['heat_level']
        num_foods += 1
    return running_total / num_foods

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
