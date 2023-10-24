import gui

# Define a function to convert values to the desired format
def convert(value):
    print(value)
    if type(value) == str:
         return value
    elif type(value) == int:
        return f"#{hex(value)[2:]}"
    else:
        return f"#{hex(value)[2:]}"

# Read the HTML template file

replacements = {

    "PLASTURE IMPOTRIVA DIABETULUI":"Rucsac Luminos USB Music",
    "list_it1":"Rucsac cu Design Modern",
    "list_it2":"Rezistent la Apă",
    "list_it3":"Funcțional și Confortabil",
    "list_desc1":"Acest rucsac modern va deveni accesoriul preferat al copilului tău, deoarece strălucește în întuneric, având un design super trendy și un efect impresionant de luminescență.",
    "list_desc2":"Rucsacul este fabricat din material sport rezistent la apă, ușor de curățat, practic și atrăgător. Dispune de două compartimente cu fermoar, unul dintre ele având un spațiu special pentru laptop cu sistem de închidere Velcro.",
    "list_desc3":"Acest rucsac se evidențiază prin portul USB intern, ce permite încărcarea smartphone-ului în timp ce ești în mișcare. De asemenea, poți păstra sursa de alimentare PowerBank în interiorul rucsacului. În plus, rucsacul poate găzdui un laptop cu ecran de 15,6 inch. Vine echipat cu un lucchet cu cod de acces pentru securitate adăugată.",
    "noua perie pentru pisici":"Rucsac Luminos USB Music",
    "plasturecap":"RucsacLuminosUSB",
    "Plasterul Importiva diabetului va":"Un rucsac funcțional și la modă, perfect pentru copii și adolescenți. Cu acest rucsac, copilul tău poate fi în trend și în siguranță în orice moment, datorită luminii fluorescente care se activează în întuneric.",
    "perie pisici":"Rucsac Luminos"

        # Add more key-value pairs as needed
    }
uploader = gui.PygameFileUploader(replacements)
uploader.run()
# while True:
#     print(uploader.submitted)
    
