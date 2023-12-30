# Project : SpiderBots
# File : Test : Manual Robot Control
# Author : Tej Pandit
# Date : Dec 2023

import pygame
import socket
import time

# Initialize Pygame
pygame.init()

# Create a joystick object
joystick = pygame.joystick.Joystick(0)

# Robot Action
action = "stop\n"

# Create a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
clientSocket.connect(("192.168.0.106", 80))


# Start the main loop
start = True
while start:

    # Check for events
    for event in pygame.event.get():

        # Exit Control
        if event.type == pygame.QUIT:
            pygame.quit()
            break

        # If the event is a joystick button press
        if event.type == pygame.JOYHATMOTION:

            # Get the button that was pressed
            hat = event.hat
            hat_direction = joystick.get_hat(hat)

            # print(hat_direction)

            if (hat_direction[0] == 1):
                print("right")
                action = "right\n"
                clientSocket.send(action.encode())
                time.sleep(0.05)

            elif (hat_direction[0] == -1):
                print("left")
                action = "left\n"
                clientSocket.send(action.encode())
                time.sleep(0.05)

            elif (hat_direction[1] == 1):
                print("up")
                action = "up\n"
                clientSocket.send(action.encode())
                time.sleep(0.05)

            elif (hat_direction[1] == -1):
                print("down")
                action = "down\n"
                clientSocket.send(action.encode())
                time.sleep(0.05)

            else:
                print("stop")
                action = "stop\n"
                clientSocket.send(action.encode())
                time.sleep(0.05)

    # Update the display
    # pygame.display.update()

pygame.quit()