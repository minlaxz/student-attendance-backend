#BETA
import os
import time
from PIL import Image,ImageFont
from luma.core.virtual import terminal
from luma.core.render import canvas
from dev.device import get_device

class Job:
    def __init__(self):
        for fontname, size in [("ProggyTiny.ttf",16)]:
            font=ImageFont.truetype(os.path.abspath(os.path.join(os.path.dirname(__file__),'fonts' , fontname)),size)
            self.term=terminal(get_device(),font)

        def show_text_sm(self,text):
            self.term.println(text)
