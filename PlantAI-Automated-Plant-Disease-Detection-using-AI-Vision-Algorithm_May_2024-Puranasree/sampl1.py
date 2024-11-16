import cv2

# Read the image
img = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges in the image
edges = cv2.Canny(gray, 100, 200)

# Display the image
cv2.imshow('Image', img)
cv2.imshow('Edges', edges)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
