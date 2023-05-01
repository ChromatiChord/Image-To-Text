from grab_image import grab_image
import config

if __name__ == "__main__":
    image_directory = config.IMAGE_DIRECTORY
    print("Press Ctrl + Shift + PrintScreen to capture a snapshot. Then press Enter to save the snapshot and read the text.")
    
    while True:
        grab_image(image_directory)
