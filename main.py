import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve the API key from environment variables
API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_animal_data(animal_name):
    """Fetch animal data from the API based on the animal name."""
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(BASE_URL + animal_name, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def serialize_animal(animal):
    """Serialize a single animal object into HTML format."""
    output = '<li class="cards__item">'
    output += f'<div class="card__title">{animal.get("name", "No Name Provided")}</div>'
    output += '<p class="card__text">'
    output += f"<strong>Location:</strong> {', '.join(animal.get('locations', ['No Location Info']))}<br/>"
    output += f"<strong>Type:</strong> {animal.get('characteristics', {}).get('type', 'No Type Info')}<br/>"
    output += f"<strong>Diet:</strong> {animal.get('characteristics', {}).get('diet', 'No Diet Info')}<br/>"
    output += '</p></li>'
    return output

def html_animal_details(animals_data, animal_name):
    """Generate HTML content based on animal data or an error message if no data is found."""
    if not animals_data:
        return f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
    
    html_output = ""
    for animal in animals_data:
        html_output += serialize_animal(animal)
    return html_output

if __name__ == "__main__":
    animal_name = input("Enter a name of an animal: ")
    animals_data = fetch_animal_data(animal_name)
    animals_html = html_animal_details(animals_data, animal_name)

    with open("animals_template.html", "r") as file:
        template_content = file.read()

    updated_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w") as file:
        file.write(updated_html)

    print("Website was successfully generated to the file animals.html.")
