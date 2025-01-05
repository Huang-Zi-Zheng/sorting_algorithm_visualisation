#This is bubble sort

import pygame, random

pygame.init()

# WINDOW
WINDOW_SIZE = 600
WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Sorting Algorithm Visualization')

#Variables
Rect_width = 10
clock = pygame.time.Clock()
FPS = 100

# Colors
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
GREY = (154, 166, 178)
LIGHT_BLUE = (64, 224, 208)
WHITE = (248, 250, 252)
SKY_BLUE = (217, 234, 253)

class Rectangle:
    def __init__ (self, color, x, height):
        self.color = color
        self.x = x
        self.width = Rect_width
        self.height = height

    def select(self):
         self.color = BLACK

    def unselect(self):
        self.color = WHITE

    def set_smallest(self):
        self.color = WHITE

    def set_sorted(self):
        self.color = BLACK

#Functions
def create_rectangles():
    num_rectangles = WINDOW_SIZE // Rect_width - 5
    rectangles = []
    heights = []

    for i in range(5, num_rectangles ):
            height = random. randint( 20, 500)

            while height in heights:
                height = random.randint(20, 500)

            heights.append(height)
            rect =  Rectangle(BLACK, i * Rect_width, height)
            rectangles.append(rect)

    return rectangles

def draw_rects(rectangles):
    WINDOW.fill(GREY)
#what this do is to separate the rectangles and make it more distinctive. This also ensures the rectangles start from the bottom of the windows
    for rect in rectangles:
        pygame.draw.rect(WINDOW, rect.color, (rect.x, WINDOW_SIZE - rect.height, rect.width, rect.height))
        pygame.draw.line(WINDOW, LIGHT_BLUE, (rect.x, WINDOW_SIZE), (rect.x, WINDOW_SIZE - rect.height))
        pygame.draw.line(WINDOW, LIGHT_BLUE, (rect.x + rect.width, WINDOW_SIZE), (rect.x + rect.width, WINDOW_SIZE - rect.height))
        pygame.draw.line(WINDOW, LIGHT_BLUE, (rect.x, WINDOW_SIZE - rect.height), (rect.x + rect.width, WINDOW_SIZE - rect.height))


#Sorting Functions:
def bubble_sort(rectangles):
    num_rectangles = len(rectangles)

    for i in range(num_rectangles):
        swapped = False  # Track if any swaps occur
        for j in range(0, num_rectangles - i - 1):  # Compare adjacent elements
            rectangles[j].select()
            rectangles[j + 1].select()
            draw_rects(rectangles)

            if rectangles[j].height > rectangles[j + 1].height:
                # Swap the rectangles
                rectangles[j].x, rectangles[j + 1].x = rectangles[j + 1].x, rectangles[j].x
                rectangles[j], rectangles[j + 1] = rectangles[j + 1], rectangles[j]
                draw_rects(rectangles)
                swapped = True

            # Unselect the compared rectangles
            rectangles[j].unselect()
            rectangles[j + 1].unselect()
            rectangles[i].unselect()
            draw_rects(rectangles)
            yield  # Pause for visualization

        # Mark the last rectangle as sorted, MADE CHANGES HERE
        for k in range(len(rectangles) - i, len(rectangles)):
            rectangles[k].set_sorted()

        if not swapped:  # Break early if no swaps occur, MADE CHANGES HERE
            for k in range(len(rectangles)):
                rectangles[k].set_sorted()  # Mark all remaining rectangles as sorted
            break

def display_text(txt, y, size):
    FONT = pygame.font.SysFont('Futura', size)

    text = FONT.render(txt, True, BLACK)
    text_rect = text.get_rect(center=(WINDOW_SIZE/2, y))
    WINDOW.blit(text, text_rect)

def main():
    rectangles = create_rectangles()
    draw_rects(rectangles)
    sorting_generator = bubble_sort(rectangles)

    run =  True
    sorting = False
    while run:
        clock.tick(FPS)
        draw_rects(rectangles)

        if sorting:
            try:
                next(sorting_generator)
            except StopIteration:
                sorting = False
        else:
            draw_rects(rectangles)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sorting = not sorting
                if event.key == pygame.K_q:
                    run = False

        pygame.display.update()

    pygame.quit()
main()