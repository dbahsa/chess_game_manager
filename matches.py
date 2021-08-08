#!/user/bin/env python3
# -*- coding: utf-8 -*-


from dataclasses import dataclass, asdict, field

# Unique match format = (["playerX_reference, playerX_scores"], ["playerY_reference, playerY_scores"])

@dataclass
class Match:
    player_reference: list
    player_score: list
    matchups: tuple = field(init=False)

