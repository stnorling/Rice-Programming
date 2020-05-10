# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
window_size = (WIDTH,HEIGHT)
###################     READ ME   ####################
#You can specify any keys you want to control but up_arrow seems to 
#cause key overlapping not working properly when thrust is on. For 
#smooth key overlapping feature, please feel free to uncomment line 20 and use w a d k keys. 
#I think it is a much better control experience with key overlapping
#on! But please don't save the change since other graders
#might take points of due to the fact that the project requires
#arrow keys to be used......

key_thrust,key_left,key_right, key_fire = "up", "left", "right", "space"
#key_thrust,key_left,key_right, key_fire = "w", "a", "d", "k"
score = 0
lives = 3
time = 0

spin_val = 0.05
acc_val = 0.2
friction = 0.02
spin_flag = {key_left:0,key_right:0}

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
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

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
    def __init__(self, pos, vel, angle, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.missile = None
        self.sound = sound
    def thrust_on(self):
        self.thrust = True
        self.image_center[0] += self.image_size[0]
        if self.sound:
            self.sound.play()
    def thrust_off(self):
        self.thrust = False
        self.image_center[0] -= self.image_size[0]
        if self.sound:
            self.sound.rewind()
    def set_angle_v(self,angle_v):
        self.angle_vel = angle_v
    def shoot(self):
        fwd = angle_to_vector(self.angle)
        pos = [0,0]
        vel = [0,0]
        missle_speed = 4
        tip_distance = self.image_size[0]/2
        for i in range(2):
            pos[i] = self.pos[i] + fwd[i]*tip_distance
            vel[i] = self.vel[i] + fwd[i]*missle_speed
        self.missile = Sprite(pos, vel, 0, 0, missile_image, missile_info, missile_sound)
        
    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size,self.pos,self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        acc = angle_to_vector(self.angle) 
        for i in range(2):
            self.pos[i] += self.vel[i]
            self.pos[i] = self.pos[i] % window_size[i]
            self.vel[i] += acc[i]* self.thrust*acc_val - friction*self.vel[i]
    
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
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        for i in range(2):
            self.pos[i] = (self.pos[i] + self.vel[i]) % window_size[i]

           
def draw(canvas):
    global time
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    # draw score:
    canvas.draw_text("Lives: " + str(lives), [10,50], 32,'Red')
    canvas.draw_text("Score: " + str(score), [WIDTH -150,50], 32,'Red')
    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    if my_ship.missile:
        my_ship.missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    if my_ship.missile:
        my_ship.missile.update()
            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    speed_range = (2,8)
    max_angle_v = 0.3
    position = generate_pos(window_size)
    velocity = generate_velocity(speed_range)
    angle_v = random.randrange(-50,51)/50.00*max_angle_v
    a_rock = Sprite(position, velocity, 0, angle_v, asteroid_image, asteroid_info)
def generate_pos(dims):
    pos = [0,0]
    pos[0] = random.randrange(dims[0])
    pos[1] = random.randrange(dims[1])
    return pos
def generate_velocity(v_limits):
    #given the speed range, generate random velocity within the range
    vel = [0,0]
    speed = v_limits[0] + random.randrange(101)/100.0*(v_limits[1] - v_limits[0])
    vel[0] = random.randrange(-50,51)/50.00*speed
    vel[1] = (random.randrange(2)*2 -1)*(speed*speed - vel[0]*vel[0])**0.5
    return vel
# key handlers
def thrust():
    my_ship.thrust_on()
def drift():
    my_ship.thrust_off()
#Here the spin mechanism is a bit more complcated than needed
#by the project, as a gamer I feel it would be nice if key overlapping
#can work. For some reason if arrow keys are used it won't 
#support key overlapping if thrust is on.

def spin(key_name):
    #takes string "left", "right" as input
    if key_name not in (key_left,key_right):
        print "Wrong key to set spin!"
        return
    global spin_flag
    temp_spin = spin_val
    if key_name == key_left:
        temp_spin *= -1
    my_ship.set_angle_v(temp_spin)
    spin_flag[key_name] = 1
    
def spin_off(key_name):
    global spin_flag
    spin_flag[key_name] = 0
    my_ship.set_angle_v(0)
    # print spin_flag[key_left] + spin_flag[key_right]	# debug
    # below returns 1 (True) if either left or right was already held
    # down as the other was released
    if spin_flag[key_left] + spin_flag[key_right]:
        if key_name == key_left:
            spin(key_right)
        else:
            spin(key_left)
            
def fire_missile():
    my_ship.shoot()
    
def key_down(key):
    if key == simplegui.KEY_MAP[key_thrust]:
        thrust()
    for key_name in (key_left, key_right):
        if key == simplegui.KEY_MAP[key_name]:
            spin(key_name)
    if key == simplegui.KEY_MAP[key_fire]:
        fire_missile()
        
def key_up(key):
    if key == simplegui.KEY_MAP[key_thrust]:
        drift()
    for key_name in (key_left, key_right):
        if key == simplegui.KEY_MAP[key_name]:
            spin_off(key_name)  
            
            
            
            
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info, ship_thrust_sound)
#a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.05, asteroid_image, asteroid_info)
rock_spawner()
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()