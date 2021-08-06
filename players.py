class Players:
    last_name: str
    first_name: str
    birth_date: str
    gender: str
    rating: int
    score: list
    tournament: list

from dataclasses import dataclass, asdict, field

@dataclass
class Player:
    """Class to create player instance."""
    last_name: str
    first_name: str
    single_pl_info: dict = field(init=False, repr=False)

    def __post_init__(self):
        """ Method to help create player full data."""
        self.single_pl_info = {"Last Name": self.last_name,
                                "First Name": self.first_name}
        
# pl_ref: list of all players data, exploited by data.py     
pl_ref = []

def add_players():
    """ function to instantiate players"""
    print("\n🚀 Procédons à l'enregistrement des 8 joueurs:")
    for i in range(1,3):
        print(f"\n🔥 Entrer les informations sur le joueur n°{i}")
        p = Player(input("- Son nom de famille: "), 
                    input("- Son prénom: ")
                    )
        pl_ref.append(p.single_pl_info)
        # print("-------------------------------------")
    print("\n🤓 Merci. Les 8 joueurs ont bien été enregistrés!")
    print("Passons à l'étape suivante dès à présent...\n")
        
add_players()
print(pl_ref)
