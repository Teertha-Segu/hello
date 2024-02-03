function go_straight () {
    motion.drive(-20, -20)
    basic.pause(750)
    motion.drive(-20, 10)
    basic.pause(500)
    motion.stop()
}
input.onButtonPressed(Button.A, function () {
    go_straight()
})
