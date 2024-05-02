import json

#Fun to load JSON data
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def html_animal_details(animals_data):
    html_output = ""
    for animal in animals_data:
        html_output += f"""
        <li class="animal-detail">
            <h2>{animal.get('name', 'No Name Provided')}</h2>
            <p>Diet: {animal.get('characteristics', {}).get('diet', 'No Diet Info')}</p>
            <p>Location: {animal.get('locations', ['No Location Info'])[0]}</p>
            <p>Type: {animal.get('characteristics', {}).get('type', 'No Type Info')}</p>
        </li>
        """
    return html_output

#load the animal data from JSON file
animals_data = load_data('animals_data.json')

#generates HTML content for animals
animals_html = html_animal_details(animals_data)

with open('animals_template.html', 'r') as file:  
    template_content = file.read()

    
updated_html = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_html)

with open('animals.html', 'w') as file:
    file.write(updated_html)

print("HTML file has been updated with animal details.")



