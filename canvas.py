from ipywidgets import ColorPicker, link, HBox, VBox, Button
from ipycanvas import Canvas, hold_canvas

canvas_ = Canvas(width=800, height=250, sync_image_data=True, layout={'border': '1px solid black'})

drawing = False
position = None


def on_mouse_down(x, y):
    global drawing
    global position

    drawing = True
    position = (x, y)
    
def on_mouse_move(x, y):
    global drawing
    global position

    if not drawing:
        return
    
    with hold_canvas(canvas_):
        canvas_.stroke_line(position[0], position[1], x, y)

        position = (x, y)

def on_mouse_up(x, y):
    global drawing
    global position

    drawing = False
    
    with hold_canvas(canvas_):
        canvas_.stroke_line(position[0], position[1], x, y)
        
def clear_canvas(btn):
    canvas_.sync_image_data = False
    canvas_.clear()
    canvas_.sync_image_data = True
    
canvas_.on_mouse_down(on_mouse_down)
canvas_.on_mouse_move(on_mouse_move)
canvas_.on_mouse_up(on_mouse_up)
canvas_.line_width = 2

picker = ColorPicker(description='Color:', value='#749cb8')
link((picker, 'value'), (canvas_, 'stroke_style'))

btn_clear = Button(description='Clear')
btn_clear.on_click(clear_canvas)

canvas = VBox((HBox((picker, btn_clear)),
      HBox((canvas_,))))
