# animation of explosion using 2D sprite sheet

import simplegui

# load 81 frame sprite sheer for explosion - image generated by phaedy explosion generator, source is hasgraphics.com
EXPLOSION_CENTER = [50, 50]
EXPLOSION_SIZE = [100, 100]

# Below represents the dimensions of the tiled image - 9x9
EXPLOSION_DIM = [9, 9]
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/explosion.hasgraphics.png")

# create timer that iterates current_sprite_center through sprite
time = 0

# define draw handler
def draw(canvas):
    global time
    # explosion_index creates an x, y index for the tiles in our tiled image.
    
    # x increases with time and resets to 0 each time it ticks to 9 due to the
    # modular arithmetic
    
    # y increases by 1 each time time passes by a number divisible by 9. this occurs through the
    # use of integer division. modular arithmetic is also used here, ensuring that each time
    # y reaches a number divisible of 9 (EXPLOSION_DIM[1]), it ticks back to 0. 
    
    explosion_index = [time % EXPLOSION_DIM[0], (time // EXPLOSION_DIM[0]) % EXPLOSION_DIM[1]]
    
#print time, time % EXPLOSION_DIM[0], (time // EXPLOSION_DIM[0]) % EXPLOSION_DIM[1], explosion_index		# debug
    
    # below we put our created variable explosion_index to use. the x and y coordinates for the
    # center of the explosion tile displayed are determined based on this index. 
    
    canvas.draw_image(explosion_image, 
                    [EXPLOSION_CENTER[0] + explosion_index[0] * EXPLOSION_SIZE[0], 
                     EXPLOSION_CENTER[1] + explosion_index[1] * EXPLOSION_SIZE[1]], 
                     EXPLOSION_SIZE, EXPLOSION_CENTER, EXPLOSION_SIZE)
    
    # time increments 60 times per second (e.g. 60 frames per second) 
    time += 1

        
# create frame and size frame based on 100x100 pixel sprite
f = simplegui.create_frame("Asteroid sprite", EXPLOSION_SIZE[0], EXPLOSION_SIZE[1])

# set draw handler and canvas background using custom HTML color
f.set_draw_handler(draw)
f.set_canvas_background("Black")

# start animation
f.start()