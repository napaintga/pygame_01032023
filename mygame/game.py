from pygame import *

init()
back = (200, 255, 255)
win_width = 1024
win_height = 512
window = display.set_mode((win_width, win_height))
player_l = [image.load('img/L1.png'), image.load('img/L2.png'), image.load('img/L3.png'),
            image.load('img/L4.png'), image.load('img/L5.png')]

player_r = [image.load('img/R1.png'), image.load('img/R2.png'), image.load('img/R3.png'),
            image.load('img/R4.png'), image.load('img/R5.png')]

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.left=False
        self.right= False
        self.count = 0
        

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()

        if keys[K_LEFT] :
            self.rect.x -= self.speed
            self.left = True
            self.right = False

        elif keys[K_RIGHT] :
            self.left = False
            self.right = True
            self.rect.x += self.speed
        else:
            self.right = self.left = False
            
    def animation(self):
        if self.left:
            self.count = (self.count + 1) % len(player_l)  
            window.blit(player_l[self.count], (self.rect.x, self.rect.y))
        elif self.right:
            self.count = (self.count + 1) % len(player_l)  
            window.blit(player_r[self.count], (self.rect.x, self.rect.y))
        else:
            self.count=0
            window.blit(player_r[self.count], (self.rect.x, self.rect.y))





FPS = 40
bg = transform.scale(image.load("img/fon.png"), (win_width, win_height))
display.set_caption("Гра")

clock = time.Clock()

game= False
menu = True


font.init() 
font3 = font.Font(None, 36)
font2 = font.Font(None, 36) 
font1 = font.Font(None,100)

def game_menu():
    pass

def level_1():
    pass

def level_2():
    pass

running = True
player = Player('img/R1.png', 5, 300, 85, 100, 10)
x_bg = 0
y_bg=0
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif  e.type==KEYDOWN :
            game = True
            menu = False
        elif e.type == K_SPACE:
            game = False
            menu = True
            

    if game:
        window.fill(back)
        window.blit(bg, (x_bg, y_bg))
        window.blit(bg, (x_bg+win_width, y_bg))
        x_bg-=4
        
        player.update()
        player.animation()

        if x_bg == -win_width:
            x_bg=0
    if menu:
        text = font2.render("Рахунок:" , 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render("Пропущено:" , 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        text_friendkill = font3.render("Своїх вбито:" , 1, (255, 255, 255))
        window.blit(text_friendkill, (10, 80))
        
    display.update()

    time.delay(FPS)
