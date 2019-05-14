import ai2thor.controller
import cv2
import keyboard
import yolo

def exportFrame():
	event = controller.step(dict(action='Initialize',continuous=True))
	cv2.imwrite('frame.jpg', event.cv2img)
	yolo.detect()

if __name__ == "__main__":
	controller = ai2thor.controller.Controller()
	controller.start(player_screen_height=480, player_screen_width=480)
	controller.reset('FloorPlan28')
	while True:
		try:
			if keyboard.is_pressed('a'):
				event = controller.step(dict(action = 'MoveLeft'))
				exportFrame()
			elif keyboard.is_pressed('d'):
				event = controller.step(dict(action = 'MoveRight'))
				exportFrame()
			elif keyboard.is_pressed('w'):
				event = controller.step(dict(action = 'MoveAhead'))
				exportFrame()
			elif keyboard.is_pressed('s'):
				event = controller.step(dict(action = 'MoveBack'))
				exportFrame()
			elif keyboard.is_pressed('right arrow'):
				event = controller.step(dict(action = 'RotateRight'))
				exportFrame()
			elif keyboard.is_pressed('left arrow'):
				event = controller.step(dict(action = 'RotateLeft'))
				exportFrame()            
			elif keyboard.is_pressed('up arrow'):
				event = controller.step(dict(action = 'LookUp'))
				exportFrame()
			elif keyboard.is_pressed('down arrow'):
				event = controller.step(dict(action = 'LookDown'))
				exportFrame()
			elif keyboard.is_pressed('esc'):
				exit()
		except Exception as error:
			raise error