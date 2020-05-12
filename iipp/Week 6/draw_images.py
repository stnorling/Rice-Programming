# Demonstration of a magnifier on a map

import simplegui

# 1521x1818 pixel map of native American language
# source - Gutenberg project

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

# Image dimensions
MAP_WIDTH = 1521
MAP_HEIGHT = 1818

# Scaling factor
SCALE = 3

# Canvas size
CAN_WIDTH = MAP_WIDTH // SCALE
CAN_HEIGHT = MAP_HEIGHT // SCALE

# Size of magnifier pane and initial center
MAG_SIZE = 120
# Below sets the initial magnification center point to the middle of the canvas.
mag_pos = [CAN_WIDTH // 2, CAN_HEIGHT // 2]

# setting the initial magnifier center position so that the full magnification cannot be displayed
# on the canvas ensures that to begin with there is no magnification.
mag_pos = [0, 0]


# Event handlers
# Move magnifier to clicked position
def click(pos):
    global mag_pos
    mag_pos = list(pos)
    
def reset():
    global mag_pos
    mag_pos = [0, 0]

# Draw map and magnified region
def draw(canvas):
    # Draw map
    # The draw_image() method automatically scales the source image to the canvas destination and height.
    canvas.draw_image(image, 
            [MAP_WIDTH // 2, MAP_HEIGHT // 2], [MAP_WIDTH, MAP_HEIGHT], 
            [CAN_WIDTH // 2, CAN_HEIGHT // 2], [CAN_WIDTH, CAN_HEIGHT])

    # Draw magnifier    
    # The scale acts to magnify the dimensions of where you clicked on the canvas to the full resolution
    # coordinates on the original image.
    map_center = [SCALE * mag_pos[0], SCALE * mag_pos[1]]
    map_rectangle = [MAG_SIZE, MAG_SIZE]
    # mag_center is the centre where the magnification is to be drawn on the canvas
    mag_center = mag_pos
    mag_rectangle = [MAG_SIZE, MAG_SIZE]
    # The magnified image is simply drawn on top of the initial image. They both take different
    # centre points from the source, and display different sizes on the canvas, hence the overlay.
    canvas.draw_image(image, map_center, map_rectangle, mag_center, mag_rectangle)
    
# Create frame for scaled map
frame = simplegui.create_frame("Map magnifier", CAN_WIDTH, CAN_HEIGHT)

# register even handlers
frame.set_mouseclick_handler(click)    
frame.set_draw_handler(draw)
frame.add_button('Magnify Off', reset)

# Start frame
frame.start()
