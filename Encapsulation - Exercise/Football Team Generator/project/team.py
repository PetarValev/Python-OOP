class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"

        return f"Player {player.name} has already joined"

    def remove_player(self, player_name):
        wanted_player = [p.name for p in self.__players if p.name == player_name][0]
        try:
            self.__players.remove(wanted_player)
        except ValueError:
            return f"Player {player_name} not found"
