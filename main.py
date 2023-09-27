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

        "PLASTURE IMPOTRIVA DIABETULUI":"Soluția pentru Restaurarea Plasticului RAYHONG",
        "list_it1":"Siguranță Garantată:",
        "list_it2":"Economie de Timp și Bani",
        "list_it3":"Ușor de Utilizat",
        "list_desc1":"Fabricată din materiale prietenoase cu mediul înconjurător și utilizând o formulă fără ulei, această soluție este inofensivă și fără miros, nu provoacă daune pielii sau plasticului din mașina dumneavoastră. Curăță cu ușurință impuritățile fără a afecta pielea sau plasticul. Puteți obține cu ușurință aspectul unei mașini \"noi\"!",
        "list_desc2":"Această soluție vă economisește cu siguranță timp și bani. Poate preveni vizitele lunare sau frecvente la service-urile auto pentru repararea, refacerea sau înlocuirea articolelor din plastic.",
        "list_desc3":"Soluția de restaurare plastic auto este extrem de ușor de utilizat. Pur și simplu ștergeți-o cu o burete pe zona dorită până când obțineți culoarea neagră dorită pentru suprafața mașinii dumneavoastră.",
        "noua perie pentru pisici":"noua Soluția pentru Restaurarea Plasticului RAYHONG",
        "plasturecap":"solutieplastic",
        "Plasterul Importiva diabetului va":"soulita RAYHONG pentru restaurarea plasticului va oferi masinii dvs un aspect nou!",
        "perie pisici":"solutie plastic"
        # Add more key-value pairs as needed
    }
uploader = gui.PygameFileUploader(replacements)
uploader.run()
# while True:
#     print(uploader.submitted)
    
