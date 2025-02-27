# import cv2
#from pyzbar import pyzbar
import zxingcpp
from PIL import Image
from win10toast_click import ToastNotifier
import pyperclip
import sys
import cv2

input_path = sys.argv[1]
#input_path = "non.png"
#print(sys.argv[1])

data = ""

def callback_copy():
    pyperclip.copy(data)

def callback_open():
    image = Image.open(input_path)
    image.show()

def scanQRcode():
    global data
    toaster = ToastNotifier()
    try:
        # image = cv2.imread(input_path)

        # qrCodeDetector = cv2.QRCodeDetector()
        # decodedText, points, _ = qrCodeDetector.detectAndDecode(image)

        #decodedText = pyzbar.decode(Image.open(input_path))
        #image = Image.open(input_path)
        image = cv2.imread(input_path)
        print(image)
        barcodes = zxingcpp.read_barcodes(image)
        for barcode in barcodes:
            # print('Found barcode:'
            # f'\n Text:    "{barcode.text}"'
            # f'\n Format:   {barcode.format}'
            # f'\n Content:  {barcode.content_type}'
            # f'\n Position: {barcode.position}')
            data = barcode.text
        if len(barcodes) == 0:
            #print("Could not find any barcode.")
            raise Exception("QR code not detected")

        # data = str(decodedText[0].data).strip("b'")
        # print(data) 
        pyperclip.copy(data) # always copy to clipboard
        # toaster.show_toast(
        #     "QR code", # title
        #     f'>> {data} \n🖱️ click to copy', # message 
        #     icon_path=None, # 'icon_path' 
        #     duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
        #     threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
        #     callback_on_click=callback_copy # click notification to run function 
        # ) 
        
    except Exception as e:
        print(e)
        # print("QR code not detected")
        toaster.show_toast(
            "QR code", # title
            f'QR Code not detected \n🖱️ Click to open screenshot', # message 
            icon_path=None, # 'icon_path' 
            duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
            threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
            callback_on_click=callback_open # click notification to run function 
        ) 

if __name__ == '__main__':
    scanQRcode()




