import pygame
import sys
from settings import Settings
from simulation import Simulation
from particle import Sand

def main() :
    settings = Settings()

    screen = pygame.display.set_mode(((settings.GRID_SIZE[0] * (settings.CELL_SIZE + settings.CELL_PADDING)) + settings.SCREEN_BORDER[1] + settings.SCREEN_BORDER[3] - settings.CELL_PADDING,
                                      (settings.GRID_SIZE[1] * (settings.CELL_SIZE + settings.CELL_PADDING)) + settings.SCREEN_BORDER[0] + settings.SCREEN_BORDER[2] - settings.CELL_PADDING))
    pygame.display.set_caption(settings.SCREEN_TITLE)

    clock = pygame.time.Clock()
    simulation = Simulation(settings)

    while True: 
        # Read Events #
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        buttons = pygame.mouse.get_pressed()
        if buttons[0] :
            mouse_position = pygame.mouse.get_pos()
            mouse_x = mouse_position[0] // (settings.CELL_SIZE + settings.CELL_PADDING)
            mouse_y = mouse_position[1] // (settings.CELL_SIZE + settings.CELL_PADDING)
            print(mouse_x, mouse_y)
            simulation.add_particle((mouse_x, mouse_y), Sand())
        
        simulation.update()

        # Draw Graphics #
        screen.fill(settings.BACKGROUND_COLOUR)
        simulation.draw(screen)

        # Final Changes #
        pygame.display.flip()
        clock.tick(60)
    
if __name__ == "__main__" :
    main()