#  Exercise 1: Create a method prints an image of your pokemon
# Display on image in Jupyter notebook
# recreate your class Pokemon
from IPython.display import Image

display(Image('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/155.png', width = 200))

class Pokemon:
    def __init__ (self, name, type, image_url):
        self.name = name
        self.type = type
        self.image_url = image_url

     def print_image(self):
       return display(Image(url=self.image_url, width=300))       
 
cyndaquil = Pokemon('Cyndaquil', 'Fire', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/155.png')
cyndaquil.print_image(Pokemon)


# Exercise 2: Create a method that evolves your pokemon. 
# If your pokemon can't evolve any further print a message that says "<name of pokemon>" can't evolve."

pokedex = {
    "cyndaquil": {"evolution_stage": 1, "evolves_into": "Quilava"},
    "quilava": {"evolution_stage": 2, "evolves_into": "Typholosion"},
    "Typholosion": {"evolution_stage": 3, "evolves_into": None}
}

def evolve_pokemon(name):
    if name in pokedex:
        evolution_stage = pokedex[name]["evolution_stage"]
        evolves_into = pokedex[name]["evolves_into"]
        if evolves_into is not None:
            print(f"{name} evolved into{evovled_into}!")
            return evolves_into
        elif evolves_into:
            print(f"{name} can't evolve any further.")
            return name
    else:
        print(f"Sorry, {name} is not in the pokedex or can't be found.")
        return None
      
pokemon_name = "Cyndaquil"
evolved_pokemon = evolve_pokemon(pokemon_name)
print(f"{pokemon_name} has evolved into {evolved_pokemon}!")


# Exercise 3: Create a Move_Tutor Class that will allow the POkemon Class to inherit a move list. For an added bonus you can make sure that if 
# a pokemon has 4 moves the user can choose one of them to replace with a new move.

class Move_Tutor:
    def __init__(self):
        self.move_list = []
        
        
    def add_move(self, move):
        self.move_list.append(move)
    
    def remove_move(self, move):
        self.move_list.remove(move)
        
    def teach_move(self):
      if len(self.moves < 4:
             print("Please choose a move to teach:")
              for i in move(remove(self.move_list):
                 print(f"{i+1}. {move}")
             choice = input("> ")
             choice = int(choice)
         try:
             if 1 <= choice <= len(self.move_list):
                new_move = self.move_list[choice-1]
                self.moves[self.moves.index(move_to_replace)] = new_move
                print(f"{self.name} forgot {move_to_replace} and learned {new_move}!")
             else:
                 print("It is invalid choice")
         except ValueError:
                print("Sorry! You been disconnected due to low internet connection. Please try again!")
     def show_moves(self):
         print(f"{self.name}'s moves:")
         for move in self_moves:
             print(move)
                            
cyndaquil = Pokemon("Cyndaquil", "Fire")
cyndaquil.add_move("Ember")
cyndaquil.add_move("Smoke Screen")
cyndaquil.add_move("Flame Wheel")
cyndaquil.add_move("Quick Attack")
cyndaquil.show_moves()                           
