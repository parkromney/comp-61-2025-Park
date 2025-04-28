import pygame
import random
from pygame import mixer


pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Asteroid Dodger")


background = pygame.image.load("AsteroidDodgerAssets/space_bg.jpg")
background = pygame.transform.scale(background, (900, 600))


mixer.music.load("AsteroidDodgerAssets/space_ambience.mp3")
mixer.music.play(-1)
catch_sound = mixer.Sound("AsteroidDodgerAssets/catch.mp3")
hit_sound = mixer.Sound("AsteroidDodgerAssets/hit.mp3")


font = pygame.font.SysFont('Comic Sans MS', 24)
title_font = pygame.font.SysFont('Comic Sans MS', 42)


player_img = pygame.image.load("AsteroidDodgerAssets/catcher_ship.png")
player_img = pygame.transform.scale(player_img, (64, 64))
player_x = 370
player_y = 500


object_img = []
object_x = []
object_y = []
object_y_change = []
object_type = []
num_objects = 10

gas_can_img = pygame.image.load("AsteroidDodgerAssets/gas_can.png")
gas_can_img = pygame.transform.scale(gas_can_img, (75, 75))
debris_img = pygame.image.load("AsteroidDodgerAssets/debris.png")
debris_img = pygame.transform.scale(debris_img, (75, 75))


score_value = 0
debris_hits = 0
max_debris_hits = 10
meter_value = 100
new_meter_decrease_rate = 0.1 / 2
meter_fill_rate = 10


def splash_screen():
    splash_img = pygame.image.load("AsteroidDodgerAssets/splash_bg.png")
    splash_img = pygame.transform.scale(splash_img, (900, 600))
    
    fade_surface = pygame.Surface((900, 600))
    fade_surface.fill((0, 0, 0))

    title_text = title_font.render("ASTEROID DODGER", True, (255, 255, 255))
    name_text = font.render("Created by Park Romney", True, (200, 200, 200))

    for alpha in range(255, -1, -5):
        screen.blit(splash_img, (0, 0))
        screen.blit(title_text, (250, 200))
        screen.blit(name_text, (340, 270))
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)

    pygame.time.delay(1000)

    for alpha in range(0, 256, 5):
        screen.blit(splash_img, (0, 0))
        screen.blit(title_text, (250, 200))
        screen.blit(name_text, (340, 270))
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)


def draw_button(text, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surf, text_rect)

def title_screen():
    menu_running = True
    while menu_running:
        screen.fill((0, 0, 0))
        title = title_font.render("ASTEROID DODGER", True, (255, 255, 255))
        screen.blit(title, (250, 100))

        draw_button("Start Game", 350, 250, 200, 50, (100, 100, 255), (50, 50, 200), start_game)
        draw_button("Instructions", 350, 320, 200, 50, (100, 100, 255), (50, 50, 200), show_instructions)
        draw_button("Quit Game", 350, 390, 200, 50, (100, 100, 255), (50, 50, 200), quit_game)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

def show_instructions():
    instructions_running = True
    while instructions_running:
        screen.fill((0, 0, 0))

        title = title_font.render("HOW TO PLAY", True, (255, 255, 255))
        screen.blit(title, (300, 60))

        instructions = [
            "Move your ship with the mouse.",
            "Catch gas cans to score and refill your gas.",
            "Every 10 gas cans collected makes the round go faster.",
            "Avoid debris. Hitting 10 of them ends the game.",
            "If the gas meter runs out, the game is over!",
            "Collect 50 gas cans to win!"
        ]
        for i, line in enumerate(instructions):
            rule = font.render(line, True, (255, 255, 255))
            screen.blit(rule, (100, 150 + i * 40))

        draw_button("Back to Menu", 350, 450, 200, 50, (150, 150, 150), (100, 100, 100), title_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

def quit_game():
    pygame.quit()
    exit()

def story_screen():
    story_running = True
    lines = [
        "In 3057, Earth exploded from human greed.",
        "You escaped — the last survivor — but with little fuel.",
        "Now, drifting among the wreckage,",
        "you must collect gas to reach Planet Park —",
        "the last sustainable planet where humans survive.",
        "Dodge debris, gather gas, and secure humanity's future!"
    ]

    current_line = 0
    fade_surface = pygame.Surface((900, 600))
    fade_surface.fill((0, 0, 0))
    fade_alpha = 255
    clock = pygame.time.Clock()

    while story_running:
        screen.fill((0, 0, 0))

       
        for i in range(current_line):
            text = font.render(lines[i], True, (255, 255, 255))
            screen.blit(text, (50, 100 + i * 40))

        if current_line < len(lines):
            text = font.render(lines[current_line], True, (255, 255, 255))
            screen.blit(text, (50, 100 + current_line * 40))

            fade_surface.set_alpha(fade_alpha)
            screen.blit(fade_surface, (0, 0))
            fade_alpha -= 5 

            if fade_alpha <= 0:
                current_line += 1
                fade_alpha = 255
                pygame.time.delay(500) 

        draw_button("Continue", 350, 500, 200, 50, (100, 100, 255), (50, 50, 200), title_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)

def game_over_screen():
    while True:
        screen.fill((0, 0, 0))
        over_text = title_font.render("GAME OVER", True, (255, 0, 0))
        score_text = font.render(f"Your Score: {score_value}", True, (255, 255, 255))
        screen.blit(over_text, (320, 150))
        screen.blit(score_text, (370, 220))

        draw_button("Retry", 350, 300, 200, 50, (100, 100, 255), (50, 50, 200), start_game)
        draw_button("Main Menu", 350, 370, 200, 50, (100, 100, 255), (50, 50, 200), title_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

def win_screen():
    while True:
        screen.fill((0, 0, 0))
        win_text = title_font.render("YOU MADE IT!", True, (0, 255, 0))
        subtitle_text = font.render("You've reached Planet Park. Humanity has a future!", True, (255, 255, 255))
        score_text = font.render(f"Final Score: {score_value}", True, (255, 255, 255))
        
        screen.blit(win_text, (300, 150))
        screen.blit(subtitle_text, (200, 220))
        screen.blit(score_text, (370, 290))

        draw_button("Play Again", 350, 370, 200, 50, (100, 100, 255), (50, 50, 200), start_game)
        draw_button("Main Menu", 350, 440, 200, 50, (100, 100, 255), (50, 50, 200), title_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()


def show_score():
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (10, 10))

def show_debris_hits():
    debris_count = font.render("Debris Hit : " + str(debris_hits), True, (255, 255, 255))
    screen.blit(debris_count, (10, 40))

def show_meter():
    pygame.draw.rect(screen, (255, 0, 0), (10, 70, 300, 20))
    pygame.draw.rect(screen, (0, 255, 0), (10, 70, meter_value * 3, 20))
    meter_text = font.render(f"Gas Meter: {int(meter_value)}%", True, (255, 255, 255))
    screen.blit(meter_text, (320, 70))

def start_game():
    global score_value, debris_hits, meter_value
    global object_img, object_x, object_y, object_y_change, object_type

    score_value = 0
    debris_hits = 0
    meter_value = 100
    base_speed = 3.0
    object_img = []
    object_x = []
    object_y = []
    object_y_change = []
    object_type = []

    for _ in range(num_objects):
        obj_type = "debris" if random.random() < 0.7 else "asteroid"
        object_type.append(obj_type)
        object_img.append(debris_img if obj_type == "debris" else gas_can_img)
        object_x.append(random.randint(0, 760))
        object_y.append(random.randint(-100, -40))
        object_y_change.append(base_speed)

    running = True
    clock = pygame.time.Clock()
    gas_cans_collected = 0

    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        player_x, _ = pygame.mouse.get_pos()
        player_x -= 32 
        player_x = max(0, min(player_x, 836))
        screen.blit(player_img, (player_x, player_y))

        for i in range(num_objects):
            object_y[i] += object_y_change[i]
            object_y_change[i] += 0.001

            if abs(player_x - object_x[i]) < 40 and abs(player_y - object_y[i]) < 40:
                if object_type[i] == "asteroid":
                    score_value += 1
                    catch_sound.play()
                    meter_value = min(meter_value + meter_fill_rate, 100)
                    gas_cans_collected += 1
                    if gas_cans_collected % 10 == 0:
                        base_speed *= 1.5
                        for j in range(len(object_y_change)):
                            object_y_change[j] = base_speed
                elif object_type[i] == "debris":
                    debris_hits += 1
                    hit_sound.play()

                object_x[i] = random.randint(0, 760)
                object_y[i] = random.randint(-100, -40)
                object_y_change[i] = base_speed

            if object_y[i] > 600:
                object_x[i] = random.randint(0, 760)
                object_y[i] = random.randint(-100, -40)
                object_y_change[i] = base_speed

            screen.blit(object_img[i], (object_x[i], object_y[i]))

        meter_value -= new_meter_decrease_rate

        if meter_value <= 0 or debris_hits >= max_debris_hits:
            game_over_screen()
            return

        if score_value >= 50:
            win_screen()
            return

        show_score()
        show_debris_hits()
        show_meter()

        pygame.display.update()
        clock.tick(60)

splash_screen()
story_screen()