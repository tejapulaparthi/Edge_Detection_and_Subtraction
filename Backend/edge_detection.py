import cv2
def detect_edges(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    img_blur = cv2.GaussianBlur(img, (5, 5), 0)

    edges = cv2.Canny(img_blur, 100, 200)

    return edges
def subtraction(image1, image2):
    if image1.shape != image2.shape:
        raise ValueError("Images must have the same dimensions for subtraction.")
    result = cv2.subtract(image1, image2)
    return result
    