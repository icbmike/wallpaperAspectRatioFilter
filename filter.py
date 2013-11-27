from PIL import Image
import os


def should_move(filename):
	try:
		image = Image.open(filename)
		return (float(image.size[0]) / image.size[1]) != (float(16) / 9)
	except IOError:
		return False

def main():
	#We only want to move file if they are images that are the incorrect aspect ratio
	files_to_move = [filename for filename in os.listdir(".") if should_move(filename)]
	
	if not os.access("filtered/", os.F_OK):
		os.mkdir("filtered")

	for filename in files_to_move:
		os.rename(filename, "filtered/" + filename)


if __name__ == '__main__':
	main()