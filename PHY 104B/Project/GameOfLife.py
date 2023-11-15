import pygame
import sys
import random


class game_of_life:

    def __init__(self, screen_width=800, screen_height=800, cell_size=10, color_alive=(0, 128, 255), color_dead=(0,0,0)):

        #Initialize window 1000x1000 (screen_width x screen_height) with grid, cell_size is the size of a cell in the grid, color_alive and color_dead represents the state of the cells
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.color_alive = color_alive
        self.color_dead = color_dead


        #Create a screen_width x screen_height window
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        self.clear_screen()

        pygame.display.flip()

        self.active_grid = 0
        #Counting number of columns in grid
        self.cols = int((self.screen_width)/self.cell_size)
        #Counting number of rows in grid 
        self.rows = int((self.screen_height)/self.cell_size)

        self.grids = [] #Empty grid array
        self.init_grids()
        self.set_grid()

        #Initialize the status of the program
        self.paused = False
        self.game_over = False

    def init_grids(self):
        #Create grid with number of columns and rows
        def create_grid():
            rows = [] #empty array of rows
            for num_row in range(self.rows):
                num_of_cols = [0] * self.cols
                rows.append(num_of_cols)
            return rows

        self.grids.append(create_grid())
        self.grids.append(create_grid())

    def set_grid(self, value=None, grid=0):
        #Randomize the grid with cells value ranging from 0 to 1 (0 = dead, 1 = alive)
        for r in range(self.rows):
            for c in range(self.cols):
                if value is None:
                    cell_value = random.randint(0,1)
                else:
                    cell_value = value
                self.grids[grid][r][c] = cell_value
    
    def clear_screen(self):
        #Empty screen
        
        self.screen.fill(self.color_dead)
        

    def draw_grid(self):
        #Draw the states of the cells obtained in the previous function on the screen
        self.clear_screen()

        for c in range(self.cols):
            for r in range(self.rows):
                if self.grids[self.active_grid][r][c] == 1:
                    color = self.color_alive
                else: 
                    color = self.color_dead
                pygame.draw.circle(self.screen, color, (int(c * self.cell_size + (self.cell_size / 2)), int(r * self.cell_size + (self.cell_size / 2))), int(self.cell_size / 2), 0)

        

        pygame.display.flip()
    

    def get_cell(self, row_num, col_num):
        try:
             cell_value = self.grids[self.active_grid][row_num][col_num]
        except:
            cell_value = 0
        return cell_value

    
    def neighbors(self, row_index, col_index):
        #Calculate total dead and alive cells from the neighbors

        num_alive_neighbors = 0
        num_alive_neighbors += self.get_cell(row_index - 1, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index - 1, col_index)
        num_alive_neighbors += self.get_cell(row_index - 1, col_index + 1)
        num_alive_neighbors += self.get_cell(row_index, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index, col_index + 1)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index + 1)

        #Life and Death rules
        if self.grids[self.active_grid][row_index][col_index] == 1:  
            if num_alive_neighbors > 3:  
                return 0
            if num_alive_neighbors < 2:  
                return 0
            if num_alive_neighbors == 2 or num_alive_neighbors == 3:
                return 1
        elif self.grids[self.active_grid][row_index][col_index] == 0:  
            if num_alive_neighbors == 3:
                return 1  
        
        return self.grids[self.active_grid][row_index][col_index]
    
    def inactive_grid(self):
        return (self.active_grid + 1) % 2

    def update_generation(self):
        #Goes through the current generation and obtains the next generation to make the new grid
        self.set_grid(0, self.inactive_grid())
        for r in range(self.rows - 1):
            for c in range(self.cols - 1):
                next_state = self.neighbors(r, c)
                self.grids[self.inactive_grid()][r][c] = next_state
        self.active_grid = self.inactive_grid()

    #Input events from the user
    def all_events(self):
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN): #Take in mouse_click as an input, begin radomizing the grid
                if event.button == 1:
                    self.active_grid = 0
                    self.set_grid(None, self.active_grid) #Radomize the state of the cells by clicking mouse button
                    self.set_grid(0, self.inactive_grid())
                    self.draw_grid()
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):
        while True:

            if self.game_over:
                return
            self.all_events()

            if not self.paused:
                self.update_generation()
                self.draw_grid()


if __name__ == '__main__':
    game = game_of_life().run()

    