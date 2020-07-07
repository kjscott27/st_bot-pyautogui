import pyautogui
from time import sleep

def main():

	initialization()
	countdown()
	openUIElement('space', 1)
	reportMousePosition()


def initialization():
	pyautogui.FAIlSAFE = True


def countdown():
	print("Starting in 10 seconds: ", end="")
	for i in range(0, 10):
		print(".", end="")
		sleep(1)
	print("Started")


def openUIElement(key, seconds=1.00):
	# this isn't useful in my case but cool to have for now
	pyautogui.press(key)
	sleep(seconds)
	pyautogui.press(key)


def reportMousePosition(seconds=10):
	for i in range(0, seconds):
		print(pyautogui.position())
		time.sleep(1)

if __name__ == "__main__":
	main()