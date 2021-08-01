class Npc:
    def __init__(self, name: str, description: str, hp: int=50):
        self.name = name
        self.description = description
        self.hp = hp
        self.pronoun: str=''
        self.is_alive = True