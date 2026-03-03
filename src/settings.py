from config_loader import load_config

class Settings :

    def __init__(self) :
        config_data = load_config()

        self.BACKGROUND_COLOUR = config_data["background_colour"]
        self.EMPTY_COLOUR = config_data["empty_colour"]
        self.SAND_COLOUR = config_data["sand_colour"]
        self.SCREEN_TITLE = config_data["screen_title"]
        self.GRID_SIZE = config_data["grid_size"]
        self.CELL_SIZE = config_data["cell_size"]
        self.CELL_PADDING = config_data["cell_padding"]
        self.SCREEN_BORDER = config_data["screen_border"]

        self.validate()
    
    def validate(self) :
        # Checks for negative screen borders.
        if self.GRID_SIZE[0] < 0 or self.GRID_SIZE[1] < 0 :
            raise "GRID_SIZE cannot contain a negative!"
        
        # Checks for negative cell size.
        if self.CELL_SIZE < 0 :
            raise "CELL_SIZE cannot be negative!"
    
        # Checks for negative cell padding.
        if self.CELL_PADDING < 0 :
            raise "CELL_SIZE cannot be negative!"
        
        # Checks for negative screen borders.
        for edge in self.SCREEN_BORDER :
            if edge < 0 :
                raise "SCREEN_BORDER cannot contain a negative!"