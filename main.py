import argparse
import cv2

def cartoonize (image):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  blurImage = cv2.medianBlur(image, 1)

  edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

  color = cv2.bilateralFilter(image, 9, 200, 200)

  cartoon = cv2.bitwise_and(color, color, mask = edges)

  return cartoon

if __name__ == "__main__":
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--image", required = True, help = "Path to input file")
  args = vars(ap.parse_args())

  image = cv2.imread(args["image"])

  cartoonImage = cartoonize(image)

  cv2.imwrite("output.jpg", cartoonImage)
  cv2.imshow("output", cartoonImage)

  cv2.waitKey(0)
  cv2.destroyAllWindows()
