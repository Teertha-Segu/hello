def go_straight():
    motion.drive(-20, -20)
    basic.pause(750)
    motion.drive(10, -20)
    basic.pause(500)
    motion.drive(-20, -20)
    basic.pause(1500)
    motion.drive(-20, 10)
    basic.pause(500)
    motion.drive(-20, -20)
    basic.pause(1500)
    motion.drive(-20, 10)
    basic.pause(500)
    motion.drive(-20, -20)
    basic.pause(1500)
    motion.drive(10, -20)
    basic.pause(500)
    motion.drive(-20, -20)
    basic.pause(750)
    motion.drive(10, -20)
    basic.pause(500)
    motion.drive(-20, -20)
    basic.pause(1500)
    motion.drive(-20, 10)
    basic.pause(500)
    motion.drive(-20, -20)
    basic.pause(1500)
    motion.drive(-20, 10)
    basic.pause(500)
    motion.drive(-20, -20)
    basic.pause(1500)
    motion.stop()

def on_button_pressed_a():
    go_straight()
input.on_button_pressed(Button.A, on_button_pressed_a)
