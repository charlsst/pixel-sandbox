import random
from custom_types import Position, Colour
from settings import Settings

settings = Settings()

EMPTY = 0
SAND = 1

def get_particle_colour(particle_id : int, position : Position) -> Colour :
    if particle_id == 0 :
        return settings.EMPTY_COLOUR
    if particle_id == 1 :
        return randomise_colour(settings.SAND_COLOUR, position)

def randomise_colour(base_colour_rgb : Colour, position : Position) -> Colour :
        rng = random.Random(position[0] * 73856093 ^ position[1] * 19349663)

        v = rng.randint(-10, 10)
        r = max(0, min(255, base_colour_rgb[0] + v))
        g = max(0, min(255, base_colour_rgb[1] + v))
        b = max(0, min(255, base_colour_rgb[2] + v))
        return r, g, b

def update_1(particle_position: Position, grid: list[int]) -> Position:
    x, y = particle_position
    width = settings.GRID_SIZE[0]
    height = settings.GRID_SIZE[1]

    new_y = y + 1

    if new_y >= height:
        return (x, y)

    below = x + new_y * width

    if grid[below] == 0:
        return (x, new_y)
    
    if random.random() < 0.5:
        offsets = (-1, 1)
    else:
        offsets = (1, -1)

    for dx in offsets:
        nx = x + dx

        if 0 <= nx < width:
            idx = nx + new_y * width

            if grid[idx] == 0:
                return (nx, new_y)

    return (x, y)