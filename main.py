import pyautogui
import time

def main():

	pyautogui.FAIlSAFE = True

	print("Starting in 10 seconds: ", end="")
	for i in range(0, 10):
		print(".", end="")
		time.sleep(1)
	print("Started")

	pyautogui.press("space")
	time.sleep(5)
	pyautogui.press("space")

	print("Done!")

if __name__ == "__main__":
	main()