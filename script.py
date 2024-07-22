from podcast_data import themes
from podcast_data import data

def start_recomendation():
    print(("#" * 46))
    print("WELCOME TO THE PODCAST RECOMMENDATION PLATFORM!")
    print("#" * 46)
    
def select_option():
    option_list = [
        "Selecciona 'n' si quieres elegir tu podcast por NOMBRE.",
        "Selecciona 't' si quieres elegir tu podcast por TEMÁTICA.",
        "Selecciona 'v' si quieres elegir tu podcast por VALORACIÓN."
    ] 
      
    options = "\n".join(option_list)
    option = input(options + "\n")
    
    if option == "n":
        select_name()
        
    elif option == "t":
        select_tematica()
          
    elif option == "v":
        select_rating()
    else:
        print("Letra inválida! Por favor, introduce 'n','t' o 'v'")
        select_option()
        
# Select Nombre
def select_name():
    name_prefix = input("Introduce las primeras letras o la primera palabra del nombre del podcast que buscas:\n").lower()
    found = False
    for item in data:
        if item[0].lower().startswith(name_prefix):
            print(f"Podcast encontrado: {item[0].upper()}")
            print(f"- Categoría: {item[3]}")
            print(f"- Temporadas: {item[1]}")
            print(f"- Valoración: {item[2]}/5")
            print(f"- Descripción: {item[4]}\n")
            found = True
    if not found:
        print("Podcast no encontrado. Intenta de nuevo.")
        select_name()


def select_tematica():
    tematica_list = [
        f"Selecciona 'a' para {themes[0]}.",
        f"Selecciona 'c' para {themes[1]}.",
        f"Selecciona 'd' para {themes[2]}.",
        f"Selecciona 'e' para {themes[3]}.",
        f"Selecciona 'f' para {themes[4]}.",
        f"Selecciona 'hi' para {themes[5]}.",
        f"Selecciona 'hu' para {themes[6]}.",
        f"Selecciona 'na' para {themes[7]}.",
        f"Selecciona 'no' para {themes[8]}.",
        f"Selecciona 'p' para {themes[9]}.",
        f"Selecciona 's' para {themes[10]}.",
        f"Selecciona 'te' para {themes[11]}.",
        f"Selecciona 'tv' para {themes[12]}."        
    ]
   
    tematicas = "\n".join(tematica_list)
    tematica = input(tematicas + "\n")
    
    category_map = {
        "a": "Astronomía",
        "c": "Cultura",
        "d": "Documental",
        "e": "Educación",
        "f": "Filosofía",
        "hi": "Historia",
        "hu": "Humor",
        "na": "Naturaleza",
        "no": "Noticias",
        "p": "Política",
        "s": "Superación Personal",
        "te": "Tecnología",
        "tv": "TV & Film"
    }

    if tematica in category_map:
        selected_category = category_map[tematica]
        for item in data:
            if item[3] == selected_category:
                print(f"En la categoría de {selected_category} tienes: {item[0].upper()}")
                print(f"- Temporadas: {item[1]}")
                print(f"- Valoración: {item[2]}/5")
                print(f"- Descripción: {item[4]}")
                
    else:
        print("Letra inválida! Por favor, introduce alguna de las anteriores")
        select_tematica()
        

# Select Valoración
def select_rating():
    rating = input("Selecciona una valoración del 1 al 5:\n")
    if rating in ["1", "2", "3", "4", "5"]:
        found = False
        for item in data:
            if item[2] == rating:
                print(f"Con la valoración {rating} tienes: {item[0].upper()}")
                print(f"- Temporadas: {item[1]}")
                print(f"- Valoración: {item[2]}/5")
                print(f"- Descripción: {item[4]}\n")
                found = True
        if not found:
            print(f"No se encontraron podcasts con la valoración {rating}.")
    else:
        print("Valoración inválida! Por favor, introduce un número del 1 al 5.")
        select_rating()


# Inicia el programa
start_recomendation()
select_option()
