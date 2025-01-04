import pygame, random

pygame.init()

# WINDOW
WINDOW_SIZE = 600
WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Sorting Algorithm Visualization')

#Variables
Rect_width = 25
clock = pygame.time.Clock()
FPS = 20

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
        self.color = PURPLE

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

    for rect in rectangles:
        pygame.draw.rect(WINDOW, rect.color, (rect.x, WINDOW_SIZE - rect.height, rect.width, rect.height))
        pygame.draw.line(WINDOW, LIGHT_BLUE, (rect.x, WINDOW_SIZE), (rect.x, WINDOW_SIZE - rect.height))
        pygame.draw.line(WINDOW, LIGHT_BLUE, (rect.x + rect.width, WINDOW_SIZE), (rect.x + rect.width, WINDOW_SIZE - rect.height))
        pygame.draw.line(WINDOW, LIGHT_BLUE, (rect.x, WINDOW_SIZE - rect.height), (rect.x + rect.width, WINDOW_SIZE - rect.height))


#Sorting Functions:
def selection_sort(rectangles):
    num_rectangles = len(rectangles)

    for i in range(num_rectangles):
        min_index = i
        rectangles[i].set_smallest()

        for j in range(i + 1 , num_rectangles):
            rectangles[j].select()
            draw_rects(rectangles)

            if rectangles[j].height < rectangles[min_index].height:
                rectangles[min_index].unselect()
                min_index = j
                rectangles[j].set_smallest()

            rectangles[min_index].set_smallest()
            draw_rects(rectangles)
            rectangles[j].unselect()

            yield

        rectangles[i].x, rectangles[min_index].x = rectangles[min_index].x, rectangles[i].x
        rectangles[i], rectangles[min_index] = rectangles[min_index], rectangles[i]

        rectangles[min_index].unselect()
        rectangles[i].set_sorted()

        draw_rects(rectangles)

def display_text(txt, y, size):
    FONT = pygame.font.SysFont('Futura', size)

    text = FONT.render(txt, True, BLACK)
    text_rect = text.get_rect(center=(WINDOW_SIZE/2, y))
    WINDOW.blit(text, text_rect)

def main():
    rectangles = create_rectangles()
    draw_rects(rectangles)
    sorting_generator = selection_sort(rectangles)

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