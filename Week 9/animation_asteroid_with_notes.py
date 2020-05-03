# demo of animation using asteroid sprite sheet

import simplegui

# load 64 frame sprite sheet for asteroid - image source is opengameart, artist is warspawn 
ROCK_CENTER = [64, 64]
ROCK_SIZE = [128, 128]

# below represents the frames of the image (e.g. DIM - dimensions, are [64, 1])
ROCK_DIM = 64

rock_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid1.opengameart.warspawn.png")

# global time for animation
time = 0
secs = 0	# debug

# draw handler    
def draw(canvas):
    global time, secs
    
    # By dividing below by 1 using integer division, we ensure that the index
    # is always an integer, not a float. as time ticks up, index changes every time
    # time ticks to a new scalar number. the maximum ticks at a given frame given 
    # time incrementing by 0.4 is 3 ticks. e.g. time = 14.0, 14.4, 14.8 -> 
    # current_rock_index = 14 14 14. 
    
    # modular arithmetic % ROCK_DIM is in place to ensure that each time the time
    # variable surpases a number divisible by ROCK_DIM (64), e.g. 64, 128, etc, the
    # returned time is reset to 0. This ensures our indexes stay in the range of 64,
    # which is how many tiles we have in our tiled image.
    
    current_rock_index = (time % ROCK_DIM) // 1
    # print time, time % ROCK_DIM, current_rock_index, secs		# debug
    
    # in the below we can see how our current_rock_center increments, depending on the current_rock_index.
    # this in turn determines which tile of the tiled image will be displayed at a given time.
    
    current_rock_center = [ROCK_CENTER[0] +  current_rock_index * ROCK_SIZE[0], ROCK_CENTER[1]]
    canvas.draw_image(rock_image, current_rock_center, ROCK_SIZE, ROCK_CENTER, ROCK_SIZE) 
    
    # below increments 60 times a second. 
    # i.e. time incremenets by: 60 x 0.4 = 24, per second. Based on our current_rock_index variable above,
    # we can see that this results in 24 different frames being displayed per second. 
    
    time += 0.4
    secs += (1.0/60.0)
    
    
# create frame and size frame based on 128x128 pixel sprite
frame = simplegui.create_frame("Asteroid sprite", ROCK_SIZE[0], ROCK_SIZE[1])

# set draw handler and canvas background using custom HTML color
frame.set_draw_handler(draw)
frame.set_canvas_background("Black")

# start animation
frame.start()