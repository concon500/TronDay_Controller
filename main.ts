forever(function () {
    makerController.player1.setAnalog(ArcadeAnalogButton.LeftRight, input.acceleration(Dimension.X))
    makerController.player1.setAnalog(ArcadeAnalogButton.DownUp, 0 - input.acceleration(Dimension.Y))
})
forever(function () {
    while (input.buttonB.isPressed()) {
        makerController.player1.press(ArcadeButton.A)
    }
})
forever(function () {
    while (input.buttonA.isPressed()) {
        makerController.player1.press(ArcadeButton.B)
    }
})
