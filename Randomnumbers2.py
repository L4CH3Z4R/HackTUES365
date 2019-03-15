import arcade
from random import seed
from random import randint
import time
SCREEN_WIDTH=1380
SCREEN_HEIGHT=750
arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,"")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for i in range(5):
	a="8"
	b=randint(10,1360)
	c=randint(10,730)
	arcade.draw_text(a,b,c,arcade.color.BLACK,12)
	time.sleep(0.5)
arcade.draw_text("Press the numbers you have just seen in order from first to last",450,730,arcade.color.BLACK,12)	
def on_key_press(self,key,modifiers):
		if a==0:
			if key==arcade.key.NUM_0:
				arcade.draw_text("Correct",20,730,arcade.color.WHITE,12)
			elif a==1:
				if key==arcade.key.NUM_1:
					arcade.draw_text("Correct",20,730,arcade.color.WHITE,12)
			elif a==2:
				if key==arcade.key.NUM_2:
					arcade.draw_text("Correct",20,730,arcade.color.WHITE,12)
			elif a==3:
				if key==arcade.key.NUM_3:
					arcade.draw_text("Correct",20,730,arcade.color.WHITE,12)	
			elif a==4:
				if key==arcade.key.NUM_4:
					arcade.draw_text("Correct",20,730,arcade.color.WHITE,12)	
			elif a==5:
				if key==arcade.key.NUM_5:
					arcade.draw_text("Correct",20,730,arcade.color.WHITE,12)
			elif a==6:
				if key==arcade.key.NUM_6:
					arcade.draw_text("Correct",20,730,arcade.color.WHITE,12)	
			elif a==7:
				if key==arcade.key.NUM_7:
					arcade.draw_text("Correct",20,730,arcade.color.WHITE,12)	
			elif a==8:
				if key==arcade.key.NUM_8:
					arcade.draw_text("Correct",20,730,arcade.color.WHITE,12)	
			elif a==9:
				if key==arcade.key.NUM_9:
					arcade.draw_text("Correct",20,730,arcade.color.WHITE,12)		
				
					
					
			
arcade.finish_render()
arcade.run()