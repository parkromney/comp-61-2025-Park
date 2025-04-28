import pygame
import random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

pygame.display.set_caption("Asteroid Dodger")

background = pygame.image.load("AsteroidDodgerAssets/space_bg.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

mixer.music.load("AsteroidDodgerAssets/space_ambience.mp3")
mixer.music.play(-1)
catch_sound = mixer.Sound("AsteroidDodgerAssets/catch.mp3")
hit_sound = mixer.Sound("AsteroidDodgerAssets/hit.mp3")

font = pygame.font.SysFont('Comic Sans MS', 24)
title_font = pygame.font.SysFont('Comic Sans MS', 42)

player_img = pygame.image.load("AsteroidDodgerAssets/catcher_ship.png")
player_img = pygame.transform.scale(player_img, (64, 64))
player_x = screen_width // 2 - 32
player_y = screen_height - 100

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
new_meter_decrease_rate = 0.15
meter_fill_rate = 10

# ---------- splash_screen ----------
def splash_screen():
    splash_img = pygame.image.load("AsteroidDodgerAssets/splash_bg.png")
    splash_img = pygame.transform.scale(splash_img, (screen_width, screen_height))
    
    fade_surface = pygame.Surface((screen_width, screen_height))
    fade_surface.fill((0, 0, 0))

    title_text = title_font.render("ASTEROID DODGER", True, (255, 255, 255))
    name_text = font.render("Created by Park Romney", True, (200, 200, 200))

    for alpha in range(255, -1, -5):
        screen.blit(splash_img, (0, 0))
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 3))
        screen.blit(name_text, (screen_width // 2 - name_text.get_width() // 2, screen_height // 2))
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)

    pygame.time.delay(1000)

    for alpha in range(0, 256, 5):
        screen.blit(splash_img, (0, 0))
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 3))
        screen.blit(name_text, (screen_width // 2 - name_text.get_width() // 2, screen_height // 2))
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)

# ---------- draw_button ----------
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

# ---------- title_screen ----------
def title_screen():
    menu_running = True
    while menu_running:
        screen.fill((0, 0, 0))
        title = title_font.render("ASTEROID DODGER", True, (255, 255, 255))
        screen.blit(title, (screen_width // 2 - title.get_width() // 2, 100))

        draw_button("Start Game", screen_width // 2 - 100, 250, 200, 50, (100, 100, 255), (50, 50, 200), start_game)
        draw_button("Instructions", screen_width // 2 - 100, 320, 200, 50, (100, 100, 255), (50, 50, 200), show_instructions)
        draw_button("Quit Game", screen_width // 2 - 100, 390, 200, 50, (100, 100, 255), (50, 50, 200), quit_game)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

# ---------- show_instructions ----------
def show_instructions():
    instructions_running = True
    while instructions_running:
        screen.fill((0, 0, 0))

        title = title_font.render("HOW TO PLAY", True, (255, 255, 255))
        screen.blit(title, (screen_width // 2 - title.get_width() // 2, 60))

        instructions = [
            "Move your ship with the mouse.",
            "Catch gas cans to score and refill your gas.",
            "Every 10 gas cans collected makes the round go faster.",
            "Avoid debris. Hitting 10 of them ends the game.",
            "If the gas meter runs out, the game is over!",
            "Collect 75 gas cans to win!"
        ]
        for i, line in enumerate(instructions):
            rule = font.render(line, True, (255, 255, 255))
            screen.blit(rule, (screen_width // 8, 150 + i * 40))

        draw_button("Back to Menu", screen_width // 2 - 100, 500, 200, 50, (150, 150, 150), (100, 100, 100), title_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

# ---------- quit_game ----------
def quit_game():
    pygame.quit()
    exit()

# ---------- story_screen ----------
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
    fade_surface = pygame.Surface((screen_width, screen_height))
    fade_surface.fill((0, 0, 0))
    fade_alpha = 255
    clock = pygame.time.Clock()

    while story_running:
        screen.fill((0, 0, 0))

        for i in range(current_line):
            text = font.render(lines[i], True, (255, 255, 255))
            screen.blit(text, (screen_width // 8, 100 + i * 40))

        if current_line < len(lines):
            text = font.render(lines[current_line], True, (255, 255, 255))
            screen.blit(text, (screen_width // 8, 100 + current_line * 40))

            fade_surface.set_alpha(fade_alpha)
            screen.blit(fade_surface, (0, 0))
            fade_alpha -= 5

            if fade_alpha <= 0:
                current_line += 1
                fade_alpha = 255
                pygame.time.delay(500)

        draw_button("Continue", screen_width // 2 - 100, screen_height - 100, 200, 50, (100, 100, 255), (50, 50, 200), title_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)

def show_objects(x, y, obj_type):
    if obj_type == "gas":
        screen.blit(gas_can_img, (x, y))
    else:
        screen.blit(debris_img, (x, y))

# ---------- show_player ----------
def show_player(x, y):
    screen.blit(player_img, (x, y))

# ---------- show_score ----------
def show_score(x, y):
    score = font.render("Gas Cans: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# ---------- show_gas_meter ----------
def show_gas_meter(x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 200, 25))
    pygame.draw.rect(screen, (0, 255, 0), (x, y, max(0, 2 * meter_value), 25))
    meter_text = font.render("Gas", True, (255, 255, 255))
    screen.blit(meter_text, (x + 75, y - 25))

# ---------- game_over_screen ----------
def game_over_screen():
    over = True
    while over:
        screen.fill((0, 0, 0))
        over_text = title_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (screen_width // 2 - over_text.get_width() // 2, 200))
        draw_button("Play Again", screen_width // 2 - 100, 350, 200, 50, (0, 200, 0), (0, 255, 0), start_game)
        draw_button("Main Menu", screen_width // 2 - 100, 420, 200, 50, (0, 0, 200), (0, 0, 255), title_screen)
        draw_button("Quit", screen_width // 2 - 100, 490, 200, 50, (200, 0, 0), (255, 0, 0), quit_game)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

# ---------- game_win_screen ----------
def game_win_screen():
    won = True
    while won:
        screen.fill((0, 0, 0))
        win_text = title_font.render("YOU WIN!", True, (0, 255, 0))
        screen.blit(win_text, (screen_width // 2 - win_text.get_width() // 2, 200))
        draw_button("Play Again", screen_width // 2 - 100, 350, 200, 50, (0, 200, 0), (0, 255, 0), start_game)
        draw_button("Main Menu", screen_width // 2 - 100, 420, 200, 50, (0, 0, 200), (0, 0, 255), title_screen)
        draw_button("Quit", screen_width // 2 - 100, 490, 200, 50, (200, 0, 0), (255, 0, 0), quit_game)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

# ---------- start_game ----------
def start_game():
    global player_x, player_y, object_x, object_y, object_type, score_value, debris_hits, meter_value

    player_x = screen_width // 2 - 32
    player_y = screen_height - 100

    object_x = []
    object_y = []
    object_type = []
    for _ in range(num_objects):
        object_x.append(random.randint(0, screen_width - 75))
        object_y.append(random.randint(-1500, -100))
        object_type.append("gas" if random.random() < 0.6 else "debris")

    score_value = 0
    debris_hits = 0
    meter_value = 100
    object_speed = 4
    new_meter_decrease_rate = 0.05

    gas_cans_collected = 0  # Track only gas cans collected (not all scores)

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        mouse_x, _ = pygame.mouse.get_pos()
        player_x = mouse_x - 32

        for i in range(num_objects):
            object_y[i] += object_speed
            if object_y[i] > screen_height:
                object_y[i] = random.randint(-1000, -100)
                object_x[i] = random.randint(0, screen_width - 75)
                object_type[i] = "gas" if random.random() < 0.6 else "debris"

            distance = ((player_x - object_x[i]) ** 2 + (player_y - object_y[i]) ** 2) ** 0.5
            if distance < 50:
                if object_type[i] == "gas":
                    gas_cans_collected += 1
                    score_value += 1
                    meter_value = min(100, meter_value + meter_fill_rate)
                    catch_sound.play()

                    if gas_cans_collected % 10 == 0:
                        object_speed *= 1.3  # Increase speed by 30%
                        

                else:
                    debris_hits += 1
                    hit_sound.play()

                object_y[i] = random.randint(-1000, -100)
                object_x[i] = random.randint(0, screen_width - 75)
                object_type[i] = "gas" if random.random() < 0.6 else "debris"

        for i in range(num_objects):
            show_objects(object_x[i], object_y[i], object_type[i])

        show_player(player_x, player_y)
        show_score(10, 10)
        show_gas_meter(10, 50)

        meter_value -= new_meter_decrease_rate
        if debris_hits >= max_debris_hits or meter_value <= 0:
            running = False
            game_over_screen()

        if score_value >= 75:
            running = False
            game_win_screen()

        pygame.display.update()
        clock.tick(60)

# ---------- Start everything ----------
splash_screen()
story_screen()