# MacropadPyDemo

This project is a [CircuitPython](https://github.com/adafruit/circuitpython) rewrite of the [Arduino demo](https://learn.adafruit.com/adafruit-macropad-rp2040/arduino) ([video](https://learn.adafruit.com/assets/103257)) that comes packaged with the [Adafruit Macropad RP2040](https://learn.adafruit.com/adafruit-macropad-rp2040).

<p align="center">
    <img src="demo.gif" alt="Video of the demo running on the Macropad RP2040"/>
</p>

This project is intended for educational purposes. Feel free to make use of this project pursuant to the [license](LICENSE).

## Installation Instructions

If you haven't already, you'll need to follow [these instructions](https://learn.adafruit.com/adafruit-macropad-rp2040/circuitpython) in order to run this project on your Macropad RP2040--this will allow your Macropad RP2040 to run CircuitPython code.

## Required Resources

The following are external resources you will need to download and put on your Macropad RP2040 to get this project to run properly.

### Libraries

Here are the necessary libraries. You can find these on [CircuitPython's website](https://circuitpython.org/libraries). Simply download the bundle for the version of CircuitPython your Macropad RP2040 is running and copy the following directories and files into the `lib/` directory of the device.

* adafruit_bitmap_font/
* adafruit_ble/services/standard/hid.mpy
* adafruit_bus_device/
* adafruit_display_text/
* adafruit_hid/
* adafruit_midi/
* adafruit_debouncer.mpy
* adafruit_macropad.mpy
* adafruit_simple_text_display.mpy
* adafruit_ticks.mpy
* neopixel.mpy

This project was created using CircuitPython 8, but may be compatible with other versions.

### Fonts

The default CircuitPython font is too large for this project. Download [this font file](https://github.com/olikraus/u8g2/blob/master/tools/font/bdf/5x8.bdf) from [this incredible selection of fonts](https://github.com/olikraus/u8g2/tree/master/tools/font) from [olikraus](https://github.com/olikraus) and place it in a new directory you create called "fonts" at the root directory of the device (i.e. `CIRCUITPY/fonts/`).

### Code

Once you have the libraries and font loaded, copy/paste [main.py](main.py) to the root directory of the device. If you've done everything correctly, the device should automatically reload and boot into the program.
