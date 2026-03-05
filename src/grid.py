import pygame
from custom_types import Display, Position, Colour, Grid_Size
from particle import get_particle_colour

class Grid :
    def __init__(self, grid_size : int,
                 cell_size : int, cell_padding : int,
                 top_padding : int, left_padding : int,
                 empty_colour : Colour, sand_colour : Colour) :
        self.rows = grid_size[1]
        self.columns = grid_size[0]
        self.cell_size = cell_size
        self.cell_padding = cell_padding
        self.top_padding = top_padding
        self.left_padding = left_padding

        self.cells = [0 for _ in range(self.rows*self.columns)]

        self.empty_colour = empty_colour
        self.sand_colour = sand_colour

    def draw(self, screen : Display) :
        for y in range(self.rows) :
            for x in range(self.columns) :
                colour = self.empty_colour
                particle_id = self.cells[x + (y * self.columns)]
                if particle_id != 0 :
                    colour = get_particle_colour(particle_id, (x,y))
                
                pygame.draw.rect(screen, colour, (x * (self.cell_size+self.cell_padding) + self.top_padding,
                                                  y * (self.cell_size+self.cell_padding) + self.left_padding,
                                                  self.cell_size,
                                                  self.cell_size))
                
    def get_size(self) -> Grid_Size :
        return (self.rows, self.columns)

    def get_cell(self, position : Position) -> int :
        if 0 <= position[0] < self.columns and 0 <= position[1] < self.rows :
            return self.cells[position[0] + (position[1] * self.columns)]
        return None
    
    def set_cell(self, position : Position, particle_id : int) :
        if not(0 <= position[0] < self.columns and 0 <= position[1] < self.rows) :
            return
        self.cells[position[0] + (position[1] * self.columns)] = particle_id

    def is_cell_empty(self, position : Position) -> bool :
        return self.cells[position[0] + (position[1] * self.columns)] is None
    
    def contains_cell(self, position : Position) -> bool :
        if 0 <= position[0] < self.columns and 0 <= position[1] < self.rows :
            return True