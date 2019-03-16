import arcade
import os

SPRITE_SCALING = 0.446
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 24
SCREEN_HEIGHT = SPRITE_SIZE * 14
SCREEN_TITLE = "Brainathon"

MOVEMENT_SPEED = 10


class Room:
	""" This class holds all the information about the different rooms. """
	def __init__(self):
		self.wall_list = None

		# This holds the background images. If you don't want changing background images, you can delete this part.
		self.background = None


def setup_room_0():
	""" Create and return room 0. If your program gets large, you may want to separate this into different files. """
	room = Room()
	room.wall_list = arcade.SpriteList()

	# Bottom and top row of boxes
	# This y loops a list of two, the coordinate 0, and just under the top of window
	for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			# Skip making a block 4 and 5 blocks on the top 
			if (x != SPRITE_SIZE * 11) or y == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)

	# Left and right column of boxes
	for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
		# Loop for each box going across
		for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
			# Skip making a block 4 and 5 blocks up on the right side
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)

	# If you want coins or monsters in a level, then add that code here.

	# Load the background image for this level.
	room.background = arcade.load_texture("floor.png")

	return room


def setup_room_1():
	""" Create and return room 2. """
	room = Room()
	room.wall_list = arcade.SpriteList()

	# Bottom and top row of boxes
	# This y loops a list of two, the coordinate 0, and just under the top of window
	for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			if (x != SPRITE_SIZE * 11) or y != 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)

	# Left and right column of boxes
	for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
		# Loop for each box going across
		for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
			if (y != SPRITE_SIZE * 10) or x == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)

	room.background = arcade.load_texture("floor.png")

	# Maze
	'''wall = arcade.Sprite("wall.png", SPRITE_SCALING)
	wall1 = arcade.Sprite("wall.png", SPRITE_SCALING)
	wall2 = arcade.Sprite("wall.png", SPRITE_SCALING)
	wall3 = arcade.Sprite("wall.png", SPRITE_SCALING)
	wall4 = arcade.Sprite("wall.png", SPRITE_SCALING)
	wall5 = arcade.Sprite("wall.png", SPRITE_SCALING)
	wall6 = arcade.Sprite("wall.png", SPRITE_SCALING)
	wall.left = 10 * SPRITE_SIZE
	wall.bottom = 1 * SPRITE_SIZE
	wall1.left = 10 * SPRITE_SIZE
	wall1.bottom = 2 * SPRITE_SIZE
	wall2.left = 10 * SPRITE_SIZE
	wall2.bottom = 3 * SPRITE_SIZE
	wall3.left = 10 * SPRITE_SIZE
	wall3.bottom = 4 * SPRITE_SIZE
	wall4.left = 10 * SPRITE_SIZE
	wall4.bottom = 5 * SPRITE_SIZE
	wall5.left = 10 * SPRITE_SIZE
	wall5.bottom = 6 * SPRITE_SIZE
	room.wall_list.append(wall)
	room.wall_list.append(wall1)
	room.wall_list.append(wall2)
	room.wall_list.append(wall3)
	room.wall_list.append(wall4)
	room.wall_list.append(wall5)
	room.wall_list.append(wall6)'''
	for y in (11 * SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			if (x != SPRITE_SIZE * 1 and x != SPRITE_SIZE * 15) or y == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)
	for y in (10 * SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			if (x != SPRITE_SIZE * 1 and x != SPRITE_SIZE * 3 and x != SPRITE_SIZE * 4 and x != SPRITE_SIZE * 5 and x != SPRITE_SIZE * 6 and x != SPRITE_SIZE * 7 and x != SPRITE_SIZE * 8 and x != SPRITE_SIZE * 9 and x != SPRITE_SIZE * 10 and x != SPRITE_SIZE * 11 and x != SPRITE_SIZE * 12 and x != SPRITE_SIZE * 13 and x != SPRITE_SIZE * 15 and x != SPRITE_SIZE * 16 and x != SPRITE_SIZE * 17 and x != SPRITE_SIZE * 18 and x != SPRITE_SIZE * 19 and x != SPRITE_SIZE * 20 and x != SPRITE_SIZE * 21 and x != SPRITE_SIZE * 22 and x != SPRITE_SIZE * 23) or y == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)
	for y in (9 * SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			if (x != SPRITE_SIZE * 1 and x != SPRITE_SIZE * 3 and x != SPRITE_SIZE * 5 and x != SPRITE_SIZE * 7 and x != SPRITE_SIZE * 15 and x != SPRITE_SIZE * 22) or y == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)
	for y in (8 * SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			if (x != SPRITE_SIZE * 1 and x != SPRITE_SIZE * 3 and x != SPRITE_SIZE * 5 and x != SPRITE_SIZE * 7 and x != SPRITE_SIZE * 9 and x != SPRITE_SIZE * 10 and x != SPRITE_SIZE * 11 and x != SPRITE_SIZE * 12 and x != SPRITE_SIZE * 13 and x != SPRITE_SIZE * 15 and x != SPRITE_SIZE * 17 and x != SPRITE_SIZE * 18 and x != SPRITE_SIZE * 19 and x != SPRITE_SIZE * 20 and x != SPRITE_SIZE * 21 and x != SPRITE_SIZE * 22 and x != SPRITE_SIZE * 23) or y == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)
	for y in (7 * SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			if (x != SPRITE_SIZE * 1 and x != SPRITE_SIZE * 3 and x != SPRITE_SIZE * 5 and x != SPRITE_SIZE * 7 and x != SPRITE_SIZE * 8 and x != SPRITE_SIZE * 9 and x != SPRITE_SIZE * 13 and x != SPRITE_SIZE * 17) or y == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)
	for y in (6 * SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			if (x != SPRITE_SIZE * 1 and x != SPRITE_SIZE * 3 and x != SPRITE_SIZE * 5 and x != SPRITE_SIZE * 11 and x != SPRITE_SIZE * 13 and x != SPRITE_SIZE * 14 and x != SPRITE_SIZE * 15 and x != SPRITE_SIZE * 17 and x != SPRITE_SIZE * 19 and x != SPRITE_SIZE * 20 and x != SPRITE_SIZE * 21 and x != SPRITE_SIZE * 22 and x != SPRITE_SIZE * 23) or y == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)
	for y in (5 * SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			if (x != SPRITE_SIZE * 1 and x != SPRITE_SIZE * 3 and x != SPRITE_SIZE * 5 and x != SPRITE_SIZE * 6 and x != SPRITE_SIZE * 7 and x != SPRITE_SIZE * 9 and x != SPRITE_SIZE * 11 and x != SPRITE_SIZE * 13 and x != SPRITE_SIZE * 15 and x != SPRITE_SIZE * 17 and x != SPRITE_SIZE * 19 and x != SPRITE_SIZE * 23 and x != SPRITE_SIZE * 22) or y == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)
	for y in (4 * SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			if (x != SPRITE_SIZE * 1 and x != SPRITE_SIZE * 5 and x != SPRITE_SIZE * 7 and x != SPRITE_SIZE * 9 and x != SPRITE_SIZE * 11 and x != SPRITE_SIZE * 15 and x != SPRITE_SIZE * 17 and x != SPRITE_SIZE * 19 and x != SPRITE_SIZE * 22) or y == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)
	for y in (3 * SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			if (x != SPRITE_SIZE * 1 and x != SPRITE_SIZE * 2 and x != SPRITE_SIZE * 3 and x != SPRITE_SIZE * 4 and x != SPRITE_SIZE * 5 and x != SPRITE_SIZE * 7 and x != SPRITE_SIZE * 9 and x != SPRITE_SIZE * 11 and x != SPRITE_SIZE * 12 and x != SPRITE_SIZE * 13 and x != SPRITE_SIZE * 14 and x != SPRITE_SIZE * 15 and x != SPRITE_SIZE * 17 and x != SPRITE_SIZE * 18 and x != SPRITE_SIZE * 19 and x != SPRITE_SIZE * 20 and x != SPRITE_SIZE * 22) or y == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)
	for y in (2 * SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			if (x != SPRITE_SIZE * 7 and x != SPRITE_SIZE * 9 and x != SPRITE_SIZE * 11 and x != SPRITE_SIZE * 15 and x != SPRITE_SIZE * 22) or y == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)
	for y in (1 * SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			if (x != SPRITE_SIZE * 1 and x != SPRITE_SIZE * 2 and x != SPRITE_SIZE * 3 and x != SPRITE_SIZE * 5 and x != SPRITE_SIZE * 6 and x != SPRITE_SIZE * 7 and x != SPRITE_SIZE * 8 and x != SPRITE_SIZE * 9 and x != SPRITE_SIZE * 11 and x != SPRITE_SIZE * 13 and x != SPRITE_SIZE * 14 and x != SPRITE_SIZE * 15 and x != SPRITE_SIZE * 16 and x != SPRITE_SIZE * 17 and x != SPRITE_SIZE * 18 and x != SPRITE_SIZE * 19 and x != SPRITE_SIZE * 20 and x != SPRITE_SIZE * 22) or y == 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)
	
			
	return room


def setup_room_2():
	""" Create and return room 3.  """
	room = Room()
	room.wall_list = arcade.SpriteList()

	# Create bottom and top row of boxes
	# This y loops a list of two, the coordinate 0, and just under the top of window
	for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
		# Loop for each box going across
		for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
			wall = arcade.Sprite("wall.png", SPRITE_SCALING)
			wall.left = x
			wall.bottom = y
			room.wall_list.append(wall)

	# Create left and right column of boxes
	for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
		# Loop for each box going across
		for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
			# Skip making a block 4 and 5 blocks up
			if (y != SPRITE_SIZE * 10) or x != 0:
				wall = arcade.Sprite("wall.png", SPRITE_SCALING)
				wall.left = x
				wall.bottom = y
				room.wall_list.append(wall)
	room.background = arcade.load_texture("floor.png")

	return room


class MyGame(arcade.Window):
	""" Main application class. """

	def __init__(self, width, height, title):
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen = True)
		width, height = self.get_size()
		self.set_viewport(0, width, 0, height)

		# Set the working directory (where we expect to find files) to the same
		# directory this .py file is in. You can leave this out of your own
		# code, but it is needed to easily run the examples using "python -m"
		# as mentioned at the top of this program.
		file_path = os.path.dirname(os.path.abspath(__file__))
		os.chdir(file_path)

		# Sprite lists
		self.current_room = 0

		# Set up the player
		self.rooms = None
		self.player_sprite = None
		self.player_list = None
		self.physics_engine = None

	def setup(self):
		# Set up the player
		self.player_sprite = arcade.Sprite("nigga_wat.png", SPRITE_SCALING)
		self.player_sprite.center_x = 500
		self.player_sprite.center_y = 500
		self.player_list = arcade.SpriteList()
		self.player_list.append(self.player_sprite)

		# List of rooms
		self.rooms = []

		# Create the rooms. Extend the pattern for each room.
		room = setup_room_0()
		self.rooms.append(room)

		room = setup_room_1()
		self.rooms.append(room)

		room = setup_room_2()
		self.rooms.append(room)

		# Our starting room number
		self.current_room = 0

		# Create a physics engine for this room
		self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

	def on_draw(self):
		""" Render the screen. """
		arcade.start_render()

		# Draw the background texture
		arcade.draw_texture_rectangle(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH * 2, SCREEN_HEIGHT * 2, self.rooms[self.current_room].background)

		# Draw all the walls in this room
		self.rooms[self.current_room].wall_list.draw()

		# If you have coins or monsters, then copy and modify the line above for each list.

		self.player_list.draw()

	def on_key_press(self, key, modifiers):
		if key == arcade.key.UP:
			self.player_sprite.change_y = MOVEMENT_SPEED
		elif key == arcade.key.DOWN:
			self.player_sprite.change_y = -MOVEMENT_SPEED
		elif key == arcade.key.LEFT:
			self.player_sprite.change_x = -MOVEMENT_SPEED
		elif key == arcade.key.RIGHT:
			self.player_sprite.change_x = MOVEMENT_SPEED
			
		if key == arcade.key.F:
			self.set_fullscreen(not self.fullscreen)

	def on_key_release(self, key, modifiers):
		if key == arcade.key.UP or key == arcade.key.DOWN:
			self.player_sprite.change_y = 0
		elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
			self.player_sprite.change_x = 0

	def update(self, delta_time):
		""" Movement and game logic """

		# Call update on all sprites 
		self.physics_engine.update()

		# Do some logic here to figure out what room we are in, and if we need to go to a different room.
		if self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 0:
			self.current_room = 1
			self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
			self.player_sprite.center_y = 0
		elif self.player_sprite.center_y < 0 and self.current_room == 1:
			self.current_room = 0
			self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
			self.player_sprite.center_y = SCREEN_HEIGHT
		elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 1:
			self.current_room = 2
			self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
			self.player_sprite.center_x = 0
		elif self.player_sprite.center_x < 0 and self.current_room == 2:
			self.current_room = 1
			self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
			self.player_sprite.center_x = SCREEN_WIDTH



def main():
	""" Main method """
	window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
	window.setup()
	arcade.run()


if __name__ == "__main__":
	main()