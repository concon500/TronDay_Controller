def on_forever():
    makerController.player1.set_analog(ArcadeAnalogButton.LEFT_RIGHT,
        input.acceleration(Dimension.X))
    makerController.player1.set_analog(ArcadeAnalogButton.DOWN_UP, input.acceleration(Dimension.Y))
forever(on_forever)

def on_forever2():
    while input.button_a.is_pressed():
        makerController.player1.press(ArcadeButton.B)
forever(on_forever2)

def on_forever3():
    while input.button_b.is_pressed():
        makerController.player1.press(ArcadeButton.A)
forever(on_forever3)
