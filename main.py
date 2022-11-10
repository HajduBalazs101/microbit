timer = 0

def on_forever():
    global timer
    basic.show_number(timer)
    basic.pause(1000)
    timer += 1
basic.forever(on_forever)
