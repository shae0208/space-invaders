import pygame
import random
import os
from pygame import mixer
from os.path import join

pygame.init()

WIDTH, HEIGHT = 1280, 720
FPS = 60
PLAYER_VEL = 10
MISSILE_VEL = 10
ENEMY_MISSILE_VEL = 5
ENEMY_VEL = .5
ENEMY_DIR = -1
ENEMY_DROP = 25
ENEMY_SPEED_MULTIPLIER = 2

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(join("assets", "ufo.png"))
pygame.display.set_icon(icon)


def start_menu(window):
    clock = pygame.time.Clock()
    title_font = pygame.font.SysFont("Zen Dots Regular", 64)
    instr_font = pygame.font.SysFont(None, 32)
    
    background = pygame.transform.scale(pygame.image.load(join("assets", "background.png")), (WIDTH, HEIGHT))

    showing = True
    
    while showing:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    showing = False

        window.blit(background, (0, 0))
        
        title_surf = title_font.render("Space Invaders", True, (255, 255, 255))
        start_instr_surf = instr_font.render("Press SPACE to start", True, (255, 255, 255))
        quit_instr_surf = instr_font.render("Press ESC to quit", True, (255, 255, 255))

        title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        start_instr_rect = start_instr_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        quit_instr_rect = quit_instr_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))

        padding = 32
        box_left = min(title_rect.left, start_instr_rect.left) - padding
        box_top = title_rect.top - padding
        box_right = max(title_rect.right, start_instr_rect.right) + padding
        box_bottom = quit_instr_rect.bottom + padding
        box_w = box_right - box_left
        box_h = box_bottom - box_top

        overlay = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        window.blit(overlay, (box_left, box_top))

        window.blit(title_surf, title_rect)
        window.blit(start_instr_surf, start_instr_rect)
        window.blit(quit_instr_surf, quit_instr_rect)

        pygame.display.update()


def pause_menu(window):
    clock = pygame.time.Clock()
    title_font = pygame.font.SysFont("Zen Dots Regular", 64)
    instr_font = pygame.font.SysFont(None, 32)

    showing = True
    
    while showing:
        clock.tick(FPS)
        mixer.music.pause()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    showing = False
                    mixer.music.unpause()

        title_surf = title_font.render("Game Paused", True, (255, 255, 255))
        start_instr_surf = instr_font.render("Press SPACE to resume", True, (255, 255, 255))
        quit_instr_surf = instr_font.render("Press ESC to quit", True, (255, 255, 255))

        title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        start_instr_rect = start_instr_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        quit_instr_rect = quit_instr_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))

        padding = 24
        box_left = min(title_rect.left, start_instr_rect.left) - padding
        box_top = title_rect.top - padding
        box_right = max(title_rect.right, start_instr_rect.right) + padding
        box_bottom = quit_instr_rect.bottom + padding
        box_w = box_right - box_left
        box_h = box_bottom - box_top

        overlay = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        window.blit(overlay, (box_left, box_top))

        window.blit(title_surf, title_rect)
        window.blit(start_instr_surf, start_instr_rect)
        window.blit(quit_instr_surf, quit_instr_rect)

        pygame.display.update()


def game_over_menu(window, score, won=False):
    clock = pygame.time.Clock()
    title_font = pygame.font.SysFont("Zen Dots Regular", 64)
    instr_font = pygame.font.SysFont(None, 32)

    showing = True
    
    while showing:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False
        
        title_text = "You Win!" if won else "Game Over"
        title_surf = title_font.render(title_text, True, (255, 255, 255))
        score_surf = instr_font.render(f"Score: {score}", True, (255, 255, 255))
        instr_surf = instr_font.render("Press R to restart or ESC to quit", True, (255, 255, 255))

        title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        score_rect = score_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))
        instr_rect = instr_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        padding = 24
        box_left = min(title_rect.left, score_rect.left, instr_rect.left) - padding
        box_top = title_rect.top - padding
        box_right = max(title_rect.right, score_rect.right, instr_rect.right) + padding
        box_bottom = instr_rect.bottom + padding
        box_w = box_right - box_left
        box_h = box_bottom - box_top

        overlay = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        window.blit(overlay, (box_left, box_top))

        window.blit(title_surf, title_rect)
        window.blit(score_surf, score_rect)
        window.blit(instr_surf, instr_rect)

        pygame.display.update()

def game_overlay(window, score):
    font = pygame.font.SysFont(None, 32)

    score_surf = font.render(f"Score: {score}", True, (255, 255, 255))

    score_rect = score_surf.get_rect(bottomleft=(20, HEIGHT - 20))

    padding = 10
    box_left = score_rect.left - padding
    box_top = score_rect.top - padding
    box_right = score_rect.right + padding
    box_bottom = score_rect.bottom + padding
    box_w = box_right - box_left
    box_h = box_bottom - box_top

    overlay = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))
    
    window.blit(overlay, (box_left, box_top))
    window.blit(score_surf, score_rect)
    
 
class Player():
    def __init__(self, x, y):
        super().__init__()
        self.player_img = pygame.image.load(join("assets", "player.png")).convert_alpha()
        self.rect = self.player_img.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.player_img)
        self.x_vel = 0
        
        
    def move(self, dx):
        self.rect.x += dx
    
    
    def move_left(self, vel):
        self.x_vel = -PLAYER_VEL
        
    
    def move_right(self, vel):
        self.x_vel = PLAYER_VEL
    
    
    def loop(self, FPS):
        self.move(self.x_vel)
        
        
    def draw(self, window):
        window.blit(self.player_img, (self.rect.x, self.rect.y))


class Enemy():
    def __init__(self, x, y, row=None):
        super().__init__()
        self.enemy_img = pygame.image.load(join("assets", "enemy.png")).convert_alpha()
        self.rect = self.enemy_img.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.enemy_img)
        self.x = float(x)
        self.y = float(y)
        self.x_vel = ENEMY_VEL * ENEMY_DIR
        self.y_vel = 0
        self.row = row
        
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
        
    def loop(self, FPS):
        self.move(self.x_vel, self.y_vel)
        
        
    def draw(self, window):
        window.blit(self.enemy_img, (self.rect.x, self.rect.y))


class Missile():
    def __init__(self, x, y):
        super().__init__()
        self.missile_img = pygame.transform.scale(pygame.image.load(join("assets", "missile.png")), (64, 64)).convert_alpha()
        self.rect = self.missile_img.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.missile_img)
        self.y_vel = -MISSILE_VEL
            
            
    def move(self, dy):
        self.rect.y += dy


    def loop(self, FPS):
        self.move(self.y_vel)   
            
            
    def draw(self, window):
        window.blit(self.missile_img, (self.rect.x, self.rect.y))


class EnemyMissile():
    def __init__(self, x, y):
        super().__init__()
        self.missile_img = pygame.transform.scale(pygame.image.load(join("assets", "missile.png")), (48, 48)).convert_alpha()
        self.rect = self.missile_img.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.missile_img)
        self.y_vel = ENEMY_MISSILE_VEL

    def move(self, dy):
        self.rect.y += dy

    def loop(self, FPS):
        self.move(self.y_vel)

    def draw(self, window):
        window.blit(self.missile_img, (self.rect.x, self.rect.y))


def draw(window, background, player, enemies, missile=None, enemy_missiles=None):
    window.blit(background, (0, 0))
    
    for enemy in enemies:
        enemy.draw(window)

    if missile:
        missile.draw(window)
    
    if enemy_missiles:
        for em in enemy_missiles:
            em.draw(window)
    
    player.draw(window)

def handle_player_movement(player):
    keys = pygame.key.get_pressed()
    
    player.x_vel = 0
    
    if keys[pygame.K_LEFT] and player.rect.x - PLAYER_VEL > 0:
        player.move_left(PLAYER_VEL)
    
    if keys[pygame.K_RIGHT] and player.rect.x + PLAYER_VEL + player.rect.width < WIDTH - 25:
        player.move_right(PLAYER_VEL)


def handle_missile_movement(missile):
    if missile:
        missile.move(missile.y_vel)
        
        if missile.rect.y < 0:
            return None
        
        return missile
    
    return None


def handle_enemy_movement(enemies):
    global ENEMY_DIR
    
    if not enemies:
        return
    
    leftmost = min(enemy.rect.x for enemy in enemies)
    rightmost = max(enemy.rect.x + enemy.rect.width for enemy in enemies)
    
    if leftmost + ENEMY_DIR * ENEMY_VEL < 0 or rightmost + ENEMY_DIR * ENEMY_VEL > WIDTH:
        ENEMY_DIR *= -1
        for enemy in enemies:
            enemy.move(0, ENEMY_DROP)
            
    for enemy in enemies:
        enemy.x_vel = ENEMY_DIR * ENEMY_VEL
        enemy.y_vel = 0


def update_speed_on_row_clear(enemies, remaining_rows):
    global ENEMY_VEL
    
    if not remaining_rows:
        return
    
    current_rows = set(enemy.row for enemy in enemies if enemy.row is not None)
    cleared = set(remaining_rows) - current_rows

    if not cleared:
        return

    for _ in list(cleared):
        ENEMY_VEL *= ENEMY_SPEED_MULTIPLIER
        remaining_rows.remove(_)


def main(window):
    global ENEMY_VEL, ENEMY_DIR
    clock = pygame.time.Clock()
    running = True
    
    mixer.music.load(join("assets", "background.wav"))
    mixer.music.play(-1)
    
    start_menu(window)
    
    player = Player(600, 675)
    missile = None
    enemy_missiles = []
    
    last_enemy_shot = pygame.time.get_ticks()
    
    enemies_row1 = [Enemy(i * 90, 0, row=0) for i in range(0, WIDTH // 100)]
    enemies_row2 = [Enemy(i * 90, 75, row=1) for i in range(0, WIDTH // 100)]
    enemies_row3 = [Enemy(i * 90, 150, row=2) for i in range(0, WIDTH // 100)]
    enemies_row4 = [Enemy(i * 90, 225, row=3) for i in range(0, WIDTH // 100)]
    
    enemies = [*enemies_row1, *enemies_row2, *enemies_row3, *enemies_row4]
    remaining_rows = set(enemy.row for enemy in enemies if enemy.row is not None)
    
    score = 0
    last_shot = 0

    while running:
        clock.tick(FPS)
        background = pygame.transform.scale(pygame.image.load(join("assets", "background.png")), (WIDTH, HEIGHT))
        now = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if missile is None and now - last_shot >= 500:
                        m_x = player.rect.centerx
                        m_y = player.rect.y
                        missile = Missile(m_x, m_y)
                        mixer.Sound.play(mixer.Sound(join("assets", "laser.wav")))
                        last_shot = now
                
                if event.key == pygame.K_ESCAPE:
                    pause_menu(window)
        
        if enemies and now - last_enemy_shot >= 1000:
            shooter = random.choice(enemies)
            em_x = shooter.rect.centerx
            em_y = shooter.rect.bottom
            
            enemy_missiles.append(EnemyMissile(em_x, em_y))
            last_enemy_shot = now

        draw(window, background, player, enemies, missile, enemy_missiles)
        
        handle_player_movement(player)
        
        missile = handle_missile_movement(missile)
        
        handle_enemy_movement(enemies)
        
        update_speed_on_row_clear(enemies, remaining_rows)
        
        player.loop(FPS)
        if missile:
            missile.loop(FPS)
        
        for enemy in enemies:
            enemy.loop(FPS)
            
        if missile:
            for enemy in enemies[:]:
                offset = (enemy.rect.x - missile.rect.x, enemy.rect.y - missile.rect.y)
                
                if missile.mask.overlap(enemy.mask, offset):
                    enemies.remove(enemy)
                    mixer.Sound.play(mixer.Sound(join("assets", "explosion.wav")))
                    score += 1
                    missile = None
                    break

        player_hit = False
        
        for em in enemy_missiles[:]:
            em.loop(FPS)
            
            if em.rect.y > HEIGHT:
                enemy_missiles.remove(em)
                continue

            if em.mask.overlap(player.mask, (player.rect.x - em.rect.x, player.rect.y - em.rect.y)):
                player_hit = True
                
                try:
                    enemy_missiles.remove(em)
                except ValueError:
                    pass
                break

        if not player_hit:
            for enemy in enemies:
                offset = (enemy.rect.x - player.rect.x, enemy.rect.y - player.rect.y)
                if enemy.mask.overlap(player.mask, offset):
                    player_hit = True
                    break

        if player_hit or enemies == []:
            game_over = game_over_menu(window, score, won=False if player_hit else True)
            
            if game_over:
                ENEMY_VEL = 0.5
                ENEMY_DIR = -1
                
                score = 0
                
                player = Player(600, 675)
                missile = None
                enemies_row1 = [Enemy(i * 85, 0, row=0) for i in range(0, WIDTH // 100)]
                enemies_row2 = [Enemy(i * 85, 75, row=1) for i in range(0, WIDTH // 100)]
                enemies_row3 = [Enemy(i * 85, 150, row=2) for i in range(0, WIDTH // 100)]
                enemies_row4 = [Enemy(i * 85, 225, row=3) for i in range(0, WIDTH // 100)]
                enemies = [*enemies_row1, *enemies_row2, *enemies_row3, *enemies_row4]
                remaining_rows = set(enemy.row for enemy in enemies if enemy.row is not None)

            else:
                running = False
                break

        update_speed_on_row_clear(enemies, remaining_rows)

        game_overlay(window, score)
        
        pygame.display.update()

    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main(window)