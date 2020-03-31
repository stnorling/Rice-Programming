import simplegui

im = simplegui.load_image("https://stocknessmonster.com/assets/stocky_bored.6ef4f8c0.gif")

# Once we have an image object created, we can use the below methods to retrieve
# the width and height dimensions of the image.
h = im.get_height()
w = im.get_width()

def draw(canvas):
    if h and w > 0:
        # Fifth parameter determines rotation of the image.
        canvas.draw_image(im, [w/2,h/2], [w, h], [w/2.4,h/1.5], [w, h], 69.8)

# .get_height and .get_width will return 0 if they compute the image size before
# the image has loaded. Thus the below w and h may not correctly create the frame
# if the image takes a while to load.
frame = simplegui.create_frame('Stockness', w, h)

frame.set_draw_handler(draw)    
frame.set_canvas_background("White")
                               
frame.start()