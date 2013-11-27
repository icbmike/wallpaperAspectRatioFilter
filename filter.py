from PIL import Image
import os

def should_move(filename):
	try:
		image = Image.open(filename)
		aspect_ratio = float(image.size[0]) / image.size[1]
		return aspect_ratio != (float(16) / 9)
	except IOError:
		return False

def main():
	
	wallpaper_dir = "/Users/michaellittle/Desktop/wallpaperdump"
	
	#We only want to move file if they are images that are the incorrect aspect ratio
	files_to_move = [filename for filename in os.listdir(wallpaper_dir) if should_move(wallpaper_dir + "/" + filename)]
	
	if not os.access(wallpaper_dir + "/filtered/", os.F_OK):
		os.mkdir(wallpaper_dir + "/filtered")

	for filename in files_to_move:
		os.rename(wallpaper_dir + "/" + filename, wallpaper_dir + "/filtered/" + filename)


if __name__ == '__main__':
	main()