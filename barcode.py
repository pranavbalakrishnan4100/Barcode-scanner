from pyzbar import pyzbar
import cv2


def draw_barcode(decoded, image):
 
    image = cv2.rectangle(image,
                          (decoded.rect.left, decoded.rect.top), 
                          (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                           color=(0, 255, 0),
                           thickness=5)
    return image

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        image = draw_barcode(obj, image)
        # print barcode number
        print("Data:", obj.data)
        print()

    return image


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while True:
        # read the frame from the camera
        ret, frame = cap.read()
        # decode detected barcodes & get the image
        frame, decoded_objects = decode(frame)
        # show the image in the window
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            break
