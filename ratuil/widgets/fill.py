
from . import Widget
from ..textstyle import TextStyle
from .. import util
import math

class Fill(Widget):
	
	def __init__(self, char, style=None):
		self.set_filling(char, style)
	
	def set_filling(self, char, style=None):
		assert util.strwidth(char) > 0
		self.char = char
		self.style = style
		self.change()
	
	def draw(self, target):
		target.clear()
		line = (self.char * math.ceil(target.width / util.strwidth(self.char)))[:target.width]
		for y in range(target.height):
			target.write(0, y, line, self.style)
	
	@classmethod
	def from_xml(cls, children, attr, text):
		return cls(text.strip() if text is not None else attr.get("char", "#"), TextStyle.from_str(attr.get("style")))
	
		
			
