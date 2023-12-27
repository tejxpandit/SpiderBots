# Project : SpiderBots
# File : Test : Input from Controllers
# Author : Tej Pandit
# Date : Dec 2023

import pygame

# Initialize Pygame
pygame.init()

# Create a joystick object
joystick = pygame.joystick.Joystick(0)

# Get the number of buttons on the controller
num_buttons = joystick.get_numbuttons()

# Get the name of the controller
controller_name = joystick.get_name()

# Print some information about the controller
print("Controller name:", controller_name)
print("Number of buttons:", num_buttons)

# Start the main game loop
start = True
while start:

    # Check for events
    for event in pygame.event.get():

        # If the event is a joystick button press
        if event.type == pygame.JOYHATMOTION:

            # Get the button that was pressed
            hat = event.hat
            hat_direction = joystick.get_hat(hat)

            # print(hat_direction)

            if (hat_direction[0] == 1):
                print("right")
            elif (hat_direction[0] == -1):
                print("left")
            elif (hat_direction[1] == 1):
                print("up")
            elif (hat_direction[1] == -1):
                print("down")
            else:
                print("centered")

    # Update the display
    # pygame.display.update()

pygame.quit()