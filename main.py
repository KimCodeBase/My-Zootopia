import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)
    
animals_data = load_data('animals_data.json')
print(animals_data)

def print_animal_details(animals_data):
    if not animals_data:
        print("No data loaded")
    for animal in animals_data:
        name = animal.get('name')
        diet = animal.get('characteristics', {}).get('diet')
        locations = animal.get('locations')
        type = animal.get('characteristics', {}).get('type')

        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if locations:
            print(f"Locations: {locations[0]}") 
        if type:
            print(f"Type: {type}")
        print()
    
print_animal_details(animals_data)




