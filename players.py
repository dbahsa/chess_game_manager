from dataclasses import dataclass, asdict, field

def player_score():
    """ return a list of player scores after each matchup """
    scores =[]
    return scores

def player_t_in():
    """ to add tournaments in which a player participated in """
    tournaments =[]
    return tournaments

@dataclass
class Player:
    """Class to create player instance."""
    last_name: str
    first_name: str
    gender: str
    rating: int
    scores: list = field(init=False, repr=False, default_factory=player_score)
    tournaments: list = field(init=False, repr=False, default_factory=player_t_in)
    single_pl_info: dict = field(init=False, repr=False)

    def __post_init__(self):
        """ Method to help create player full data"""
        self.single_pl_info = {"Last Name": self.last_name,
                                "First Name": self.first_name,
                                "Genre": self.gender,
                                "Classement Général": self.rating,
                                "Score": self.scores,
                                "Tournois": self.tournaments}
        
# pl_ref: list of all players data, exploited by data.py     
pl_ref = []

def add_players():
    """ function to instantiate players"""
    print("\n🚀 Procédons à l'enregistrement des 8 joueurs:")
    # !!! DO NOT FORGET TO CHANGE THE RANGE BELOW TO REFLECT USER'S REQUIREMENTS OF 8 PLAYERS
    for i in range(1,3):
        print(f"\n🔥 Entrer les informations sur le joueur n°{i}")
        p = Player(input("- Nom de famille: "), 
                    input("- Prénom: "),
                    input("- Genre : "),
                    input("- Nombre de Points au Classement Général: ")
                    )
        pl_ref.append(p.single_pl_info)
        # print("-------------------------------------")
    print("\n🤓 Merci. Les 8 joueurs ont bien été enregistrés!")
    print("Passons à l'étape suivante dès à présent...\n")
        
add_players()
print(pl_ref)
