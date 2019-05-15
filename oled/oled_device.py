import os
import time
#"This Script is Created by laxz for OLED and Raspberry pi"
from PIL import Image,ImageFont
from luma.core.virtual import terminal
from luma.core.render import canvas
from dev.device import get_device

def make_font(name,size):
    f_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'fonts' , name))
    return ImageFont.truetype(f_path , size)


def get_term(s):
    for fontname, size in [("ProggyTiny.ttf", s)]:
        font = make_font(fontname,size) if fontname else None
        return(terminal(get_device() ,font))

def show_text_lg(txt):
    term = get_term(18)
    term.println(txt)
    time.sleep(0.3)

def show_text_sm(txt):
    term = get_term(16)
    term.println(txt)
    time.sleep(0.3)


def percent_long():
    term = get_term(16)
    term.animate = False
    for mill in range(0, 10001, 25):
        term.puts("\rProcessing: {0:0.1f} %".format(mill / 100.0))
        term.flush()
    term.animate = True

def percent_fast():
    term = get_term(16)
    term.animate = False
    for mill in range(0, 10001, 250):
        term.puts("\rProcessing: {0:0.1f} %".format(mill / 100.0))
        term.flush()
    term.animate = True


def img():
	device = get_device()
	img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
		'images', 'pi_logo.png'))
	logo = Image.open(img_path).convert("RGBA")
	fff = Image.new(logo.mode, logo.size, (255,) * 4)
	background = Image.new("RGBA", device.size, "white")
	posn = ((device.width - logo.width) // 2, 0)

	while True:
		for angle in range(0, 360, 2):
			rot = logo.rotate(angle, resample=Image.BILINEAR)
			img = Image.composite(rot, fff, rot)
			background.paste(img, posn)
			device.display(background.convert(device.mode))
		break



def put_text(txt):
	term = get_term(18)
	term.animate = False
	term.puts(txt)
	term.flush()
	sleep(0.3)
