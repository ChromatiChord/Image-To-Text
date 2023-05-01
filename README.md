# Image-To-Text

### Installation
1. Head [here](https://github.com/UB-Mannheim/tesseract/wiki "Title") and download tesseract OCR. Install it.
2. Install the python dependencies with `pip install -r requirements.txt`
3. Ensure that the path specified in config.py matches your tesseract OCR installation path.
4. Run the program from the command line with `python main.py`

### Usage
1. Once the program is running, press the key combination `Ctrl+Shift+PrintScreen` to take a snapshot (this combination can be changed in config.py).
2. Select your desired area and press enter to save the snapshot.
3. Soon after, a popup will appear containing the analysed text from the image.
