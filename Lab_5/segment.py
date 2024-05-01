import cv2
from matplotlib import pyplot as plt

def otsu(img, save_to):
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    
    _, thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    
    
    plt.imshow(thresh, cmap='gray')
    plt.axis('off')
    plt.savefig(save_to)
    plt.show()
    
    return thresh

def image_processing(image, blur_kernel=91, canny_threshold1=100, canny_threshold2=250):
    
    blur = cv2.medianBlur(image, blur_kernel)
    
    
    edged = cv2.Canny(blur, canny_threshold1, canny_threshold2)
    
    
    plt.imshow(edged, cmap='gray')
    plt.axis('off')
    plt.show()
    
    return edged

def image_contours(image_entrance):
    
    contours, _ = cv2.findContours(image_entrance.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return contours


def image_recognition(image_entrance, image_cont, file_name):
    for c in image_cont:
        peri = cv2.arcLength(c, True)
        area = cv2.contourArea(c)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if area > 200:
            cv2.drawContours(image_entrance, [approx], -1, (0, 255, 0), 4)

    cv2.imwrite(file_name, image_entrance)
    plt.imshow(image_entrance)
    plt.show()

    return


if __name__ == "__main__":
    img = cv2.imread('img_lake4.jpg')
    segment =  otsu(img, 'imgOTSU.jpg')

    image_exit = image_processing(segment)
    image_cont = image_contours(image_exit)

    image_recognition(img, image_cont, "image_recognition_1.jpg")
