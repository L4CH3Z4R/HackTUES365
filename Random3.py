import arcade
import random
import time
SCREEN_TITLE = "Random numbers"
SCREEN_WIDTH = 1380
SCREEN_HEIGHT = 750
SPRITE_SCALING = 1

class MyGame(arcade.Window):
	def __init__(self, width, height, title):
		super().__init__(width, height, title)
		arcade.set_background_color(arcade.color.AMAZON)
	def setup(self):
        # Sprite lists
		self.player_list = arcade.SpriteList()
		self.number_list = arcade.SpriteList()
        # Set up the player
		self.player_sprite = arcade.Sprite("nigga_wat.png", SPRITE_SCALING)
		self.player_sprite.center_x = 50
		self.player_sprite.center_y = 50
		self.number0_sprite = arcade.Sprite("Number0.png", SPRITE_SCALING)
		self.number0_sprite.center_x = random.randint(20,1300)
		self.number0_sprite.center_y = random.randint(20,730)
		self.number_list.append(self.number0_sprite)
		self.number1_sprite = arcade.Sprite("Number1.png", SPRITE_SCALING)
		self.number1_sprite.center_x = random.randint(20,1300)
		self.number1_sprite.center_y = random.randint(20,730)
		self.number_list.append(self.number1_sprite)
		self.number2_sprite = arcade.Sprite("Number2.png", SPRITE_SCALING)
		self.number2_sprite.center_x = random.randint(20,1300)
		self.number2_sprite.center_y = random.randint(20,730)
		self.number_list.append(self.number2_sprite)
		self.number3_sprite = arcade.Sprite("Number3.png", SPRITE_SCALING)
		self.number3_sprite.center_x = random.randint(20,1300)
		self.number3_sprite.center_y = random.randint(20,730)
		self.number_list.append(self.number3_sprite)
		self.number4_sprite = arcade.Sprite("Number4.png", SPRITE_SCALING)
		self.number4_sprite.center_x = random.randint(20,1300)
		self.number4_sprite.center_y = random.randint(20,730)
		self.number_list.append(self.number4_sprite)
		self.number5_sprite = arcade.Sprite("Number5.png", SPRITE_SCALING)
		self.number5_sprite.center_x = random.randint(20,1300)
		self.number5_sprite.center_y = random.randint(20,730)
		self.number_list.append(self.number5_sprite)
		self.number6_sprite = arcade.Sprite("Number6.png", SPRITE_SCALING)
		self.number6_sprite.center_x = random.randint(20,1300)
		self.number6_sprite.center_y = random.randint(20,730)
		self.number_list.append(self.number6_sprite)
		self.number7_sprite = arcade.Sprite("Number7.png", SPRITE_SCALING)
		self.number7_sprite.center_x = random.randint(20,1300)
		self.number7_sprite.center_y = random.randint(20,730)
		self.number_list.append(self.number7_sprite)
		self.number8_sprite = arcade.Sprite("Number8.png", SPRITE_SCALING)
		self.number8_sprite.center_x = random.randint(20,1300)
		self.number8_sprite.center_y = random.randint(20,730)
		self.number_list.append(self.number8_sprite)
		self.number9_sprite = arcade.Sprite("Number9.png", SPRITE_SCALING)
		self.number9_sprite.center_x = random.randint(20,1300)
		self.number9_sprite.center_y = random.randint(20,730)
		self.number_list.append(self.number9_sprite)
	def on_draw(self):
		#Render the screen.
		arcade.start_render()
		# Draw all the sprites
		arcade.draw_text("What were the numbers you saw? Press the numbers on your kb", 400, 730, arcade.color.WHITE, 15)
		self.player_sprite.draw()
		rng=random.randint(0,9)
		self.number_list[rng].draw()
		time.sleep(0.2)
			
				
	def update(self, delta_time):
		pass
	def on_key_press(self, key, key_modifiers):
		pass
	def on_key_release(self, key, key_modifiers):
		pass
	def on_mouse_motion(self, x, y, delta_x, delta_y):
		pass
	def on_mouse_press(self, x, y, button, key_modifiers):
		pass
	def on_mouse_release(self, x, y, button, key_modifiers):
		pass
def main():
	game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
	game.setup()
	arcade.run()
if __name__ == "__main__":
	main()