import pygame
from custom_types import Display, Position, Colour, Grid_Size
from particle import Particle

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


        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]

        self.empty_colour = empty_colour
        self.sand_colour = sand_colour

    def draw(self, screen : Display) :
        for row in range(self.rows) :
            for column in range(self.columns) :
                colour = self.empty_colour
                particle = self.cells[row][column]
                if particle is not None :
                    colour = particle.get_colour()
                
                pygame.draw.rect(screen, colour, (column * (self.cell_size+self.cell_padding) + self.top_padding,
                                                  row * (self.cell_size+self.cell_padding) + self.left_padding,
                                                  self.cell_size,
                                                  self.cell_size))
                
    def get_size(self) -> Grid_Size :
        return (self.rows, self.columns)

    def get_cell(self, position : Position) -> Particle :
        if 0 <= position[0] < self.columns and 0 <= position[1] < self.rows :
            return self.cells[position[1]][position[0]]
        return None
    
    def set_cell(self, position : Position, particle : Particle) :
        if not(0 <= position[0] < self.columns and 0 <= position[1] < self.rows) :
            return
        self.cells[position[1]][position[0]] = particle

    def is_cell_empty(self, position : Position) -> bool :
        return self.cells[position[1]][position[0]] is None