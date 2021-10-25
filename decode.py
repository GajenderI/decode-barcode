# Importing library
from os import WEXITED
import cv2
import argparse
from pyzbar.pyzbar import decode

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# # load the input image
image = args["image"]

def decodeImage(img):
    try:
        detectedBarcodes = decode(img)
        return detectedBarcodes
    except TypeError:
     	   print ("cannot unpack non-iterable NoneType object")
         
# Make one method to decode the barcode
def BarcodeReader(image):
    
	# read the image in numpy array using cv2
	img = cv2.imread(image)
 
	# Decode the barcode image
	detectedBarcodes = decodeImage(img)

	# If not detected then print the message
	if not detectedBarcodes:
		print("Barcode Not Detected or your barcode is blank/corrupted!")
	else:
	
		# Traverse through all the detected barcodes in image
		for barcode in detectedBarcodes:
		
			# Locate the barcode position in image
			(x, y, w, h) = barcode.rect
			
			# Put the rectangle in image using
			# cv2 to heighlight the barcode
			cv2.rectangle(img, (x-10, y-10),
						(x + w+10, y + h+10),
						(255, 0, 0), 2)
			
			if barcode.data!="":
			
			# Print the barcode data
				print(barcode.data.decode("utf-8"))
				print(barcode.type)

BarcodeReader(image)
