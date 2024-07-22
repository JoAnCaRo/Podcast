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
        print("Nombre")
        
    elif option == "t":
        select_tematica()
          
    elif option == "v":
        print("Valoración")
    else:
        print("Letra inválida! Por favor, introduce 'n','t' o 'v'")
        select_option()

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

# Inicia el programa
start_recomendation()
select_option()
