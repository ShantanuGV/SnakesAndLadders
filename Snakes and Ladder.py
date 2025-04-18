import pygame
import random

pygame.init()

# Screen setup
screen = pygame.display.set_mode((700, 570))
pygame.display.set_caption("🐍Snakes and 🖇Ladder")

winner = None
game_over = False


# Background and board
bimag = pygame.image.load("101692.jpg")
bordimag = pygame.image.load("100.png")

# Player pins
player_red = pygame.image.load("pin_red.png")
player_red = pygame.transform.scale(player_red, (30, 30))
player_blue = pygame.image.load("pin_blue.png")
player_blue = pygame.transform.scale(player_blue, (30, 30))

# Dice images
dice_1 = pygame.image.load("dice_1.png")
dice_1 = pygame.transform.scale(dice_1, (100, 100))
dice_2 = pygame.image.load("dice_2.png")
dice_2 = pygame.transform.scale(dice_2, (100, 100))
dice_3 = pygame.image.load("dice_3.png")
dice_3 = pygame.transform.scale(dice_3, (100, 100))
dice_4 = pygame.image.load("dice_4.png")
dice_4 = pygame.transform.scale(dice_4, (100, 100))
dice_5 = pygame.image.load("dice_5.png")
dice_5 = pygame.transform.scale(dice_5, (100, 100))
dice_6 = pygame.image.load("dice_6.png")
dice_6 = pygame.transform.scale(dice_6, (100, 100))

dice_imgs = [dice_1, dice_2, dice_3, dice_4, dice_5, dice_6]

# Snakes and ladders mapping
snakes = {99: 46, 91: 76, 65: 52, 50: 10, 45: 9, 37: 20}
ladders = {2: 41, 28: 49, 75: 94, 83: 98}

# Button
button_color = (255, 0, 0)
button_rect = pygame.Rect(570, 200, 110, 40)
font = pygame.font.Font(None, 30)

# Large font for winner announcement
large_font = pygame.font.Font(None, 100)

# Game variables
red_pos = 1
blue_pos = 1
current_dice = 1
turn = "red"
square_size = 55
game_over = False

def get_position_coords(pos):
    """Convert board position (1-100) to screen x, y"""
    row = (pos - 1) // 10
    col = (pos - 1) % 10
    if row % 2 == 1:
        col = 9 - col
    x = 10 + col * square_size + (square_size - 30) // 2
    y = 10 + (9 - row) * square_size + (square_size - 30) // 2
    return x, y

def draw_board():
    screen.blit(bimag, (0, 0))
    screen.blit(bordimag, (10, 10))

def draw_players():
    rx, ry = get_position_coords(red_pos)
    bx, by = get_position_coords(blue_pos)
    screen.blit(player_red, (rx, ry))
    screen.blit(player_blue, (bx, by))

def draw_button():
    pygame.draw.rect(screen, button_color, button_rect)
    text = font.render("Roll Dice", True, (255, 255, 255))
    screen.blit(text, (button_rect.x + 10, button_rect.y + 10))

def draw_dice():
    screen.blit(dice_imgs[current_dice - 1], (570, 20))

def draw_turn():
    turn_text = f"Turn: {'🔴 Red' if turn == 'red' else '🔵 Blue'}"
    text = font.render(turn_text, True, (255, 255, 255))
    screen.blit(text, (button_rect.x, button_rect.y - 40))


def draw_winner(winner):
    winner_text = f"{winner} WINSSSSSSSSSS!!!!!!"
    text = large_font.render(winner_text, True, (255, 0, 0))
    screen.blit(text, (50, 250))


def roll_dice():
    global current_dice, red_pos, blue_pos, turn, game_over, winner
    roll = random.randint(1, 6)
    current_dice = roll

    if turn == "red":
        new_pos = red_pos + roll
        if new_pos <= 100:
            if new_pos == blue_pos:
                blue_pos = 1
            red_pos = new_pos

            if red_pos in snakes:
                red_pos = snakes[red_pos]
            elif red_pos in ladders:
                red_pos = ladders[red_pos]

        if red_pos == 100:
            winner = "RED"
            game_over = True
        else:
            turn = "blue"

    else:
        new_pos = blue_pos + roll
        if new_pos <= 100:
            if new_pos == red_pos:
                red_pos = 1
            blue_pos = new_pos

            if blue_pos in snakes:
                blue_pos = snakes[blue_pos]
            elif blue_pos in ladders:
                blue_pos = ladders[blue_pos]

        if blue_pos == 100:
            winner = "BLUE"
            game_over = True
        else:
            turn = "red"

# Main loop
running = True
while running:
    draw_board()
    draw_button()
    draw_dice()
    draw_turn()
    draw_players()

    if game_over and winner:
        draw_winner(winner)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over and button_rect.collidepoint(event.pos):
                roll_dice()

pygame.quit()
