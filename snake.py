import pygame

SIZE = 20

class Snake():
    def __init__(self):
        self.direction = [0, 1]
        self.parts = [Part((8,6), self), Part((8,5), self), Part((8,4), self)]
    def draw(self, surface):
       for part in self.parts:
           part.draw(surface, isHead = part.coords == self.getHead().coords)
    def update(self):
        lastPart = self.parts.pop()
        self.parts.insert(0, lastPart)
        self.parts[0].move()

    def getHead(self):
        return self.parts[0]

    def turn(self, newDirection):
        directions = {
            "right": [1,0],
            "left": [-1,0],
            "up": [0,-1],
            "down": [0, 1]
        }
        self.direction = directions[newDirection]

class Part():
    def __init__(self, coords, snake):
        self.coords = list(coords)
        self.snake = snake
        
        headImage = pygame.image.load("head.png")
        self.head = pygame.Surface((20, 20))
        self.head.blit(headImage, (0,0))
    
    def draw(self, surface, isHead = False):
        pygame.draw.rect(surface, pygame.Color("green"), (self.coords[0] * SIZE, self.coords[1] * SIZE, SIZE, SIZE))
        if isHead:
            surface.blit(pygame.transform.rotate(self.head, self.snake.direction[0] * -90 + self.snake.direction[1] * 90 + abs(self.snake.direction[1]) * 90), (self.coords[0] * SIZE, self.coords[1] * SIZE))


    def move(self):
        self.coords[0] = self.snake.parts[1].coords[0] + self.snake.direction[0]
        self.coords[1] = self.snake.parts[1].coords[1] + self.snake.direction[1]
