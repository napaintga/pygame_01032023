from pygame import *
init()
back = (200, 255, 255)
win_width = 1024
win_height = 512
window = display.set_mode((win_width, win_height))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.images = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)

    def update(self):
        keys = key.get_pressed()
        
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.x -= self.speed
            self.left=True
            self.right= False
        
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.x += self.speed
            self.left=False
            self.right= True
        else:
            self.count=0
            self.left=False
            self.right= False
            
    def animation(self):
        if self.count +1 >=45:
            self.count=0
        elif self.left == True:
            window.blit(player_l[self.count//5],(self.rect.x,self.rect.y))
            self.count+=1
        elif self.right == True:
            window.blit(player_r[self.count//5],(self.rect.x,self.rect.y))
            self.count+=1
        else: 
            window.blit(self.image,(self.rect.x,self.rect.y))
            
            
player_l = [image.load('img/L1.png'), image.load('img/L2.png'), image.load('img/L3.png'), image.load('img/L4.png'), image.load('img/L5.png')]

player_r = [image.load('img/R1.png'), image.load('img/R2.png'), image.load('img/R3.png'), image.load('img/R4.png'), image.load('img/R5.png'), image.load('img/R6.png')]

enemys_l=['img/L1E.png','img/L2E.png','img/L3E.png','img/L4E.png','img/L5E.png']
enemys_r=['img/R1E.png','img/R2E.png','img/R3E.png','img/R4E.png','img/R5E.png','img/R6E.png']