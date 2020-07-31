import sys
import pygame
import rendering
import logic
import snake
import random
import time
import globalVariables
import random

pygame.init()
clock = pygame.time.Clock()
snake.initalizeGame(pygame)

# Game Loop
while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        # Event-handling for keyboard input when a human plays the game
        logic.handleKeyboardInput(event)
    
    action = random.randint(0, 3)

    # Take a step with the selected action, recieve a reward, new scree-frame 
    # and if a terminal state has been reached (i.e. game over)
    reward, frame, isTerminalState = snake.step(action)

    # If the state is a terminal state then the episode has ended, print score
    if isTerminalState:
        globalVariables.loggedScores.append(globalVariables.score)
        globalVariables.score = 0


    clock.tick(globalVariables.fps) # Use for rendering and showing the game
    #clock.tick() # Don't delay framerate when not rendering


pygame.quit()
