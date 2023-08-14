import pygame
from box import Box
from particle import Particle
from collisionHelper import circle_sweep_and_prune
from random import randrange, randint
from pygame.locals import *
 
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
FPS = 60

def draw_text(text, font, text_col,screen, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def main():

    pygame.init()

    #define font
    font = pygame.font.SysFont(None, 20)

    box = Box(0, 0, 20, 20, SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40, 2, (65,105,225))

    num_of_particles = 150
    particle_color = [(0,255,127), (135,206,235), (147,112,219)]
    particles = []
    for i in range(num_of_particles):
        x, y = randrange(30, SCREEN_WIDTH - 50), randrange(21, SCREEN_HEIGHT - 40)
        radius = mass = 8
        color = particle_color[randint(0, 2)]
        particles.append(Particle(x, y, radius, mass, 0, color))

    #animation variables
    pause = False

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Particle Simulation")
    clock = pygame.time.Clock()
    running = 1

    while running:
        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw border
        box.draw(screen)

        for particle in particles:
            # Draw Particle
            particle.draw(screen)

            if not pause:

                particle.update(FPS)

                #check for collision on the borders of the box
                particle.checkBorderCollision(box)

                #check for particle collision
                # for other_particle in particles:
                #     if particle == other_particle:
                #         continue
                        
                #     particle.particleCollision(other_particle)

        possible_collisions = circle_sweep_and_prune(particles)

        for collision in possible_collisions:
            particle1, particle2 = collision

            particle1.particleCollision(particle2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                pygame.quit()
                quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause

        pygame.display.update()

        # Limit the framerate
        clock.tick(FPS)

if __name__ == "__main__":
    main()