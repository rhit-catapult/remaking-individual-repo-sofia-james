import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    # TODO 4: Return the actual distance between point 1 and point 2.
    #  Hint: you will need the math library for the sqrt function.
    #       distance = sqrt(   (delta x) ** 2 + (delta y) ** 2  )
    distance = math.sqrt((point1_x - point2_x)**2 + (point1_y - point2_y)**2)
    return distance


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)
    pink = pygame.Color("Pink")

    # TODO 8: Load the "drums.wav" file into the pygame music mixer
    pygame.mixer.music.load("drums.wav")
    pygame.mixer.Sound("explosion.wav")

    instruction_text = 'Click in a circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    circle1_color = (154, 58, 212)
    circle1_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle1_radius = 50
    circle_border_width = 3
    circle2_color = (pink)
    circle2_center = (325, 64)
    circle2_radius = 25

    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO 2: For a MOUSEBUTTONDOWN event get the click position.
            if event.type == pygame.MOUSEBUTTONDOWN:
                # TODO 3: Determine the distance between the click position and the circle1_center using the distance
                # TODO 3:   function and save the result into a variable called distance_from_circle
                click_position = event.pos
                distance_from_circle = distance(click_position, circle1_center)
                # TODO 5: If distance_from_circle is less than or equal to circle1_radius, set message_text to 'Bullseye!'
                # TODO 5: If distance_from_circle is greater than the circle1_radius, set the message_text to 'You missed!'
                if distance_from_circle < circle1_radius:
                    #message_text = "Bullseye!"
                    pygame.mixer.music.play()
                if distance_from_circle > circle2_radius:
                    pygame.mixer.Sound("explosion.wav").play
                    #message_text = "You missed!"
                    #pygame.mixer.music.stop()
                # TODO 9: Start playing the music mixer looping forever if the click is within the circle
                # TODO 10: Stop playing the music if the click is outside the circle

        screen.fill(pygame.Color("Black"))

        # TODO 1: Draw the circle using the screen, circle1_color, circle1_center, circle1_radius, and circle_border_width
        pygame.draw.circle(screen, circle1_color, circle1_center, circle1_radius, circle_border_width)
        pygame.draw.circle(screen, circle2_color, circle2_center, circle2_radius, circle_border_width)

        # TODO 6: Create a text image (render the text) based on the message_text with the color (122, 237, 201)
        onscreen_message = font.render(message_text, True, (122, 237, 201))

        screen.blit(instructions_image, (25, 25))
        # TODO 7: Draw (blit) the message to the user that says 'Bullseye!' or 'You missed!'
        screen.blit(onscreen_message, (25, 375))

        pygame.display.update()


main()
