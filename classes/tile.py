from dataclasses import dataclass, field

@dataclass
class Tile:
    description: str = ''
    items: list = field(default_factory=list)
