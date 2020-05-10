# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
in_play = False


class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# ship explosion
ship_explosion_info = ImageInfo([50, 50], [100, 100], 0, 81, True)
ship_explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/explosion.hasgraphics.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.sound = ship_thrust_sound
        self.forward_vector = [0, 0]
        self.turning = {'right': False,
                        'left':False
                        }
        self.shooting = False
        self.shoot_count = 0
    
    def get_pos(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def draw(self,canvas):
        # rather than do two draw_image() functions, could simply change the self.image_center parameter in the
        # if statement.
        if not self.thrust:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]], 
                              self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        # Rather than using magic numbers below for friction and acceleration (0.97, 0.55), could set local variables
        # within this function to represent these coefficients, and thus change accordingly if needed.
        
        self.angle += self.angle_vel
        
        if self.thrust:
            self.forward_vector = angle_to_vector(self.angle)
            # Rather than using an if statement all together, can multiple the first componenet of the below
            # equation by self.thrust (1 if True, 0 if False). Regardless of self.thrust, the friction multiple
            # would still be applied
            self.vel[0] = (self.vel[0] + 0.55 * self.forward_vector[0])
            self.vel[1] = (self.vel[1] + 0.55 * self.forward_vector[1])
            
        self.vel[0] = 0.97 * (self.vel[0])
        self.vel[1] = 0.97 * (self.vel[1])
                                 
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        
        if self.shooting:
            self.shoot_count += 2
            if self.shoot_count % 12 == 2:
                self.shoot()
        
    def angle_change(self, dir):
        inputs = {'left': -0.08, 
                  'right': 0.08}
        
        for i in inputs:
            if i == dir:
                self.angle_vel = inputs[i]
            
    def angle_vel_reset(self):
        self.angle_vel = 0  
        
    def accelerate(self):
        self.thrust = True
        self.sound.play()
      
    def thrust_off(self):
        self.thrust = False
        self.sound.rewind()
        
    def shooting_on(self):
        self.shooting = True
        
    def shooting_off(self):
        self.shoot_count = 0
        self.shooting = False
        
    def shoot(self):
        global missile_group
        
        # the missile parameters can be set on the old missile, then reassigned to the new missile  in its
        # creation to make the code a bit tidier. A new a_missile needs to be created in order to play the sound.
        # alternatively, the parameters could be set up and then a_missle.sound.play() entered (note this would
        # require creating a new method in the Sprite class allowing sounds to be played).
        
        # rather than updating the forward vector below, can create a new foward vector 'missile_vector'
        # that is seperate from the ship's forward_vector
        
        self.forward_vector = angle_to_vector(self.angle)
        a_missile = Sprite([self.pos[0] + self.forward_vector[0] * self.radius, self.pos[1] + self.forward_vector[1] * 45], 
                          [self.vel[0] + (9 * self.forward_vector[0]),self.vel[1] + (9 * self.forward_vector[1])],
                          0, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
    
    def get_pos(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
   
    def draw(self, canvas):
        
        if self.animated:
            if self.image == ship_explosion_image:
                EXPLOSION_DIM = [9, 9]
                explosion_index = [self.age % EXPLOSION_DIM[0], (self.age // EXPLOSION_DIM[0]) % EXPLOSION_DIM[1]]
                canvas.draw_image(ship_explosion_image, 
                    [self.image_center[0] + explosion_index[0] * self.image_size[0], 
                     self.image_center[1] + explosion_index[1] * self.image_size[1]], 
                     self.image_size, self.pos, self.image_size, self.angle)
            else:
                canvas.draw_image(self.image, [self.image_center[0] + self.age * self.image_size[0], self.image_center[1]],
                                            self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel        
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.age += 1
        if self.age >= self.lifespan:
            return True
                  
    def collision(self, other_object):
        return dist(self.get_pos(), other_object.get_pos()) <= self.get_radius() + other_object.get_radius()
            
    
    
# Both keydown and keyup handlers can be placed in to the my_ship object, and then called to there from 
# the frame.set_key_handler() methods. This would allow calling of self methods inside the key handlers. 
# E.g. updating self.image_center for accelerating vs. not accelerating etc. Probably better, as would make
# it easier to change up the code if the 'my_ship' variable were to change names.

# Would also mean can call self on parameters, rather than having to create so many methods in the Class
# (e.g. accelerate, angle_change, etc).

shooting = False

def keydown_handler(key): 
    global in_play, shooting
    
    #in_play = True
    
    if simplegui.KEY_MAP['left'] == key:
        my_ship.angle_change('left')
        my_ship.turning['left'] = True
        
    elif simplegui.KEY_MAP['right'] == key:
        my_ship.angle_change('right')
        my_ship.turning['right'] = True
        
    elif simplegui.KEY_MAP['up'] == key:
        my_ship.accelerate()
        
    elif simplegui.KEY_MAP['space'] == key:
        my_ship.shooting_on()

        
def keyup_handler(key):
    global shooting
    
    if simplegui.KEY_MAP['left'] == key:
        my_ship.turning['left'] = False
        if my_ship.turning['right'] == False:
            my_ship.angle_vel_reset()
        else:
            my_ship.angle_change('right')
            
    if simplegui.KEY_MAP['right'] == key:
        my_ship.turning['right'] = False
        if my_ship.turning['left'] == False:
            my_ship.angle_vel_reset()
        else:
            my_ship.angle_change('left')
    
    if simplegui.KEY_MAP['up'] == key:
        my_ship.thrust_off()
        
    if simplegui.KEY_MAP['space'] == key:
        my_ship.shooting_off()
    
    
def mouse_handler(pos):
    global in_play, lives, score, timer
    
    if in_play == False:
        in_play = True
        lives = 3
        score = 0
        timer.start()
        soundtrack.rewind()
        soundtrack.play()
        
    
def draw(canvas):
    global time, in_play, lives, score, rock_group, timer
    
    # animate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    # two images of the debris are drawn and moved at the same time in order to 
    # create the effect of continuous flying debris in the background. 
    # their length apart is the width of the canvas at all given times, so they
    # never overlap. the first image starts off the canvas, and the second
    # image starts at the center of the canvas. 
    # as wtime gradually increases, the images both move to the right, until 
    # wtime goes back to 0 (when it exceeds WIDTH -> wtime % WIDTH = 0)
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # call group sprite processer
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)
    
    # call group collision checker for ship. deducts life if ship collides with rock.
    if group_collide(rock_group, my_ship):
        lives -= 1
        if lives == 0:
            in_play = False
            timer.stop()
            soundtrack.rewind()
        
    # call group_group collission checker for missiles and rocks. Add points for successful destroynig of rocks
    if group_group_collide(missile_group, rock_group):
        score += 10
    
    # draw ship and sprites
    my_ship.draw(canvas)
    
    # update ship
    my_ship.update()
    
    # draw splash
    if not in_play:
        splash.draw(canvas)
        rock_group = set([]) 
        soundtrack.play()
        
    # draw score and lives
    canvas.draw_text('Lives: ' + str(lives), [10, 20], 20, 'Yellow')
    canvas.draw_text('Score: ' + str(score), [WIDTH -100, 20], 20, 'Yellow')

    
# function that processes and draws all sprites in a group
def process_sprite_group(group, canvas):
    for sprite in group.copy():
        sprite.draw(canvas)
        if sprite.update():
            group.remove(sprite)
        
# function that checks for collisions in a group
def group_collide(group, other_object):
    global explosion_group
    for sprite in group.copy():
        if sprite.collision(other_object):
            an_explosion = Sprite(sprite.get_pos(), [0, 0], 0, 0, explosion_image, explosion_info, explosion_sound)
            explosion_group.add(an_explosion)
            if other_object == my_ship:
                ship_explosion = Sprite(other_object.get_pos(), [0, 0], 0, 0, ship_explosion_image, 
                                        ship_explosion_info, explosion_sound)
                explosion_group.add(ship_explosion)
            group.remove(sprite)
            return True            
    
# function that checks for collissions between groups (e.g. missiles and rocks)    
def group_group_collide(group, other_group):
    for sprite in group.copy():
        if group_collide(other_group, sprite):
            group.remove(sprite)
            return True

# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    
    rand_pos = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
    # rock vel changes based on score. higher score = higher rock vel. makes more difficult.
    rand_vel = [random.random() * (2 + score * 0.01) * random.choice([1, -1]), 
                random.random() * (2 + score * 0.01) * random.choice([1, -1])]
    rand_angular_vel = random.random() * 0.25 * random.choice([1, -1])
    
    a_rock = Sprite(rand_pos, rand_vel, 0, rand_angular_vel, asteroid_image, asteroid_info)
    
    if len(rock_group) < 12:
        # Below ensures rocks do not spawn on to the ship
        if dist(a_rock.get_pos(), my_ship.get_pos()) > (a_rock.get_radius() + my_ship.get_radius()) * 1.5:
            rock_group.add(a_rock)
    
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], math.pi/2, ship_image, ship_info)
missile_group = set([])
rock_group = set([])
explosion_group = set([])

# initialize splash
splash = Sprite([WIDTH / 2, HEIGHT / 2], [0, 0], 0, 0, splash_image, splash_info)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.set_mouseclick_handler(mouse_handler)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
frame.start()