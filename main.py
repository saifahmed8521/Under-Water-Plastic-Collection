import yolov5
model = yolov5.load('runs/detect/train2/weights/best.pt')  # load a custom model
results = model('1.jpg',stream=True)  # predict on an image
results.show()
# results.save(filename='result.jpg')

# Process results generator
# for result in results:
#     boxes = result.boxes  # Boxes object for bounding box outputs
#     masks = result.masks  # Masks object for segmentation masks outputs
#     keypoints = result.keypoints  # Keypoints object for pose outputs
#     probs = result.probs  # Probs object for classification outputs
    # result.show()  # display to screen
    # result.save(filename='result.jpg')  # save to disk