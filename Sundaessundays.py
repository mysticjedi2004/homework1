import pygame, random
#Initialize pygame
pygame.init()
#Set display surface
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sundaes Sunday")
#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()
#Set game values
PLAYER_STARTING_ICK = 5
STARTING_VELOCITY = 1
ACCERLATION = 1
#Class with my image properties
class Myimage:
    def __init__(self, img, name):
        self.imageName = name
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()
        random.seed(None)
        self.rect.x = random.randint(0,WINDOW_WIDTH - 100)
        self.rect.y = random.randint(0,WINDOW_HEIGHT - 100)
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
    velocity = STARTING_VELOCITY
    #image movement
    def move(self):
        self.rect.x += self.dx*self.velocity
        self.rect.y += self.dy*self.velocity
        #Bounce the images off the edges of the display
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx = -1*self.dx
        if self.rect.top <=  0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.dy = -1*self.dy
#scores
yum = 0
ick = PLAYER_STARTING_ICK
#Set colors
TEAL = (0, 128, 128)
SAGE = (152, 168, 105)
RED = (255, 0, 0)
BLACK = (255, 255, 255)
#Ice cream cone image
cone = Myimage("WaffleCone.png", "Cone")
ice_cream = Myimage("IceCream.png", "Ice Cream")
cherry = Myimage("Cherry.png", "Cherry")
chocolate = Myimage("ChocolateSyrup.png", "Chocolate")
whipped = Myimage("WhippedCream.png", "Whipped Cream")
spaghetti = Myimage("Spaghetti.png", "Spaghetti")
hot_dog = Myimage("HotDog.png", "Hot Dog")
objective_list = [cone, ice_cream, cherry, chocolate, whipped]
object = random.choice(objective_list)
items_list = [cone, ice_cream, cherry, chocolate, whipped, spaghetti, hot_dog]
#Set fonts
font = pygame.font.Font("Icecream.ttf", 32)
#Set text
title_text = font.render("Sundaes Sunday", True, TEAL)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)
score_text = font.render("Yum: " + str(yum), True, SAGE)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)
objective_text = font.render("Objective: " + object.imageName, True, SAGE)
objective_rect = objective_text.get_rect()
objective_rect.center = (462.5, 50)
lives_text = font.render("Icks: " + str(ick), True, SAGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)
game_over_text = font.render("GAMEOVER", True, RED, BLACK)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2 -5, WINDOW_HEIGHT//2)
continue_text = font.render("Click anywhere to play again", True, BLACK, RED)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)
#Set sound and music
click_sound = pygame.mixer.Sound("correct.wav")
miss_sound = pygame.mixer.Sound("wrong.wav")
pygame.mixer.music.load("Truck1.wav")
pygame.mixer.music.load("Truck2.wav")
pygame.mixer.music.load("Truck3.wav")
pygame.mixer.music.load("Truck4.wav")
pygame.mixer.music.load("Truck5.wav")
#Set images
background_image = pygame.transform.scale(pygame.image.load("background.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)
#The main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #A click is made
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            #When the objective is clicked
            if object.rect.collidepoint(mouse_x, mouse_y):
                click_sound.play()
                yum += 1
                #Loop through list to increase velocity
                for i in items_list:
                    i.velocity += ACCERLATION
                
                #The object is moved
                previous_dx = object.dx
                previous_dy = object.dy
                while(previous_dx == object.dx and previous_dy == object.dy):
                    object.dx = random.choice([-1, 1])
                    object.dy = random.choice([-1, 1])
                #changing the onjective
                object = random.choice(objective_list)
                objective_text = font.render("Objective: " + object.imageName, True, SAGE)
            
            #If you click incorrectly
            else:
                miss_sound.play()
                ick -= 1
    #Ensuring that all of the images are moving
    for i in items_list:
        i.move()
        
    #Updating the game HUB
    score_text = font.render("Yum: " + str(yum), True, SAGE)
    lives_text = font.render("Icks: " + str(ick), True, SAGE)
    #The code for a Game Over
    if ick == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        #Pause the game until the player resumes
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #The player wants to play again.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    yum = 0
                    ick = PLAYER_STARTING_ICK
                    cone = Myimage("WaffleCone.png")
                    ice_cream = Myimage("IceCream.png")
                    cherry = Myimage("Cherry.png")
                    chocolate = Myimage("ChocolateSyrup.png")
                    whipped = Myimage("WhippedCream.png")
                    spaghetti = Myimage("Spaghetti,png")
                    hot_dog = Myimage("HotDog.png")
                    objective_list = [cone, ice_cream, cherry, chocolate, whipped]
                    object = random.choice(objective_list)
                    objective_text = font.render("Objective: " + object.imageName, True, SAGE)
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                #The player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
             
    #Blit the background
    display_surface.blit(background_image, background_rect)
    #Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(objective_text, objective_rect)
    #Blit assets
    for i in items_list:
        display_surface.blit(i.image, i.rect)
    
    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)
#End the game
pygame.quit()
