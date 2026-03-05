from custom_types import Display, Position
from grid import Grid
from settings import Settings
from particle import SAND, update_1

class Simulation :
    def __init__(self, settings : Settings) :
        self.settings = settings
        self.grid = Grid(self.settings.GRID_SIZE,
                         self.settings.CELL_SIZE,
                         self.settings.CELL_PADDING,
                         self.settings.SCREEN_BORDER[0],
                         self.settings.SCREEN_BORDER[1],
                         self.settings.EMPTY_COLOUR,
                         self.settings.SAND_COLOUR)
        self.grid_size = self.grid.get_size()
    
    # Draws the grid to the screen
    def draw(self, screen : Display) :
        self.grid.draw(screen)

    # Updates every tile in the grid
    def update(self) :
        for y in range(self.grid_size[0] -2, -1, -1) :
            for x in range(self.grid_size[1]) :
                particle = self.grid.cells[x + (y * self.grid_size[1])]
                if particle != 0 :
                    new_position = update_1((x, y), self.grid.cells)
                    
                    if new_position != (x, y) :
                        self.grid.set_cell(new_position, SAND)
                        self.grid.set_cell((x, y), 0)

    def get_grid(self) :
        return self.grid

    def get_grid_cell(self, position : Position) :
        return self.grid.get_cell(position)

    def add_particle(self, position : Position, particle_id : int) :
        if 0 <= position[0] < self.settings.GRID_SIZE[0] and 0 <= position[1] < self.settings.GRID_SIZE[1] :
            self.grid.set_cell((position[0], position[1]), particle_id)

    def delete_particle(self, position : Position) :
        if 0 <= position[0] < self.settings.GRID_SIZE[0] and 0 <= position[1] < self.settings.GRID_SIZE[1] :
            self.grid.set_cell((position[0], position[1]), 0)