import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal):
    """ Serialize a single animal object into HTML format """
    output = '<li class="cards__item">'
    output += f'<div class="card__title">{animal.get("name", "No Name Provided")}</div>'
    output += '<p class="card__text">'
    output += f"<strong>Location:</strong> {', '.join(animal.get('locations', ['No Location Info']))}<br/>"
    output += f"<strong>Type:</strong> {animal.get('characteristics', {}).get('type', 'No Type Info')}<br/>"
    output += f"<strong>Diet:</strong> {animal.get('characteristics', {}).get('diet', 'No Diet Info')}<br/>"
    output += '</p></li>'
    return output
#generates HTML data 
def html_animal_details(animals_data):
    html_output = ""
    for animal in animals_data:
        html_output += serialize_animal(animal)
    return html_output
#Main function that loads data, updates style 
if __name__ == "__main__":
    animals_data = load_data('animals_data.json')
    animals_html = html_animal_details(animals_data)
    
    with open('animals_template.html', 'r') as file:
        template_content = file.read()
        
    updated_html = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_html)
    
    with open('animals.html', 'w') as file:
        file.write(updated_html)
    
    print("HTML file has been updated.")




