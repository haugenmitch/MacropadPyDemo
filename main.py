import board
from adafruit_bitmap_font import bitmap_font
from displayio import Bitmap
from adafruit_macropad import MacroPad
from time import sleep, monotonic


# calculates a key's color given its index
def get_color(index) -> tuple:
    time_scale = 5
    time_offset = int(monotonic() / time_scale % 1 * 256)
    index_offset = int(index / len(macropad.pixels) * 256)
    offset = (time_offset + index_offset) % 256
    if offset < 85:
        return (255 - offset * 3, 0, offset * 3)
    elif offset < 170:
        offset -= 85
        return (0, offset * 3, 255 - offset * 3)
    else:
        offset -= 170
        return (offset * 3, 255 - offset * 3, 0)


# generates the string to be displayed for pressed keys
def get_keypress_string(key_states, row) -> str:
    spaces = "  " if row < 3 else " "
    key_num = row * 3 + 1
    state_string = ""
    for i, state in enumerate(key_states):
        state_string += f"KEY{key_num+i}{spaces}" if state else " " * 6
    return state_string


# create macropad object
macropad = MacroPad()

# initialize text display
small_font = bitmap_font.load_font("fonts/5x8.bdf", Bitmap)
state_text = macropad.display_text(font=small_font)
state_text.show()

# initialize I2C system
i2c = board.I2C()
i2c_last_update = 0
i2c_addrs = []
while not i2c.try_lock():
    pass

# initialize state vars
encoder_pos = 0
keys_pressed = [False] * macropad.keys.key_count
state_text[0].text = "* Adafruit Macropad *"
state_text[1].text = "Rotary encoder: 0"

# initialize key colors
macropad.pixels.brightness = 0.3
for i in range(0, len(macropad.pixels)):
    macropad.pixels[i] = get_color(i)

print("Adafruit Macropad with RP2040")

# startup tones
macropad.play_tone(988, 0.1)
sleep(0.1)
macropad.play_tone(1319, 0.2)
sleep(0.2)

while True:
    # handle encoder position changes
    if macropad.encoder != encoder_pos:
        direction = macropad.encoder - encoder_pos
        print(f"Encoder:{macropad.encoder} Direction:{direction}")
        state_text[1].text = "Rotary encoder: {}".format(macropad.encoder)
        encoder_pos = macropad.encoder

    # search for connected I2C devices
    # this check reoccurs at 1 Hz
    if (curr := int(monotonic())) != i2c_last_update:
        i2c_last_update = curr

        # find I2C devices
        print("Scanning I2C:")
        print("Found I2C address ", end="")
        i2c_addrs = []
        for addr in i2c.scan():
            i2c_addrs.append(addr)
            print(f"0x{hex(addr)}, ", end="")
        print()

        # udpate display with found I2C devices
        i2c_text = "I2C Scan: "
        for addr in i2c_addrs:
            i2c_text += f"0x{hex(addr)} "
        if state_text[2].text != i2c_text:
            state_text[2].text = i2c_text

    # handle encoder presses
    macropad.encoder_switch_debounced.update()
    if macropad.encoder_switch_debounced.pressed:
        print("Encoder button")
        state_text[3].text = "Encoder pressed"
        macropad.pixels.brightness = 1.0
    elif macropad.encoder_switch_debounced.released:
        state_text[3].text = ""
        macropad.pixels.brightness = 0.3

    # update the color of all of the keys
    for i in range(0, len(macropad.pixels)):
        macropad.pixels[i] = get_color(i)

    # handle key presses
    rows = set()
    while (key_event := macropad.keys.events.get()):
        key_num = key_event.key_number
        keys_pressed[key_num] = key_event.pressed
        rows.add(key_num // 3)
        print(f"Switch {key_num}")

    # update text to correspond with key presses
    for row in rows:
        state_text[row + 4].text = get_keypress_string(keys_pressed[row*3:row*3+3], row)
