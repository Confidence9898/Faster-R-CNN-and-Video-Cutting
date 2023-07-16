import cv2
import math

def cutting_data(input_path, output_path):
	cap = cv2.VideoCapture(input_path)
	frame_rate = cap.get(cv2.CAP_PROP_FPS)
	frame_interval = int(frame_rate)

	frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	duration = frame_count/frame_rate
	duration = math.ceil(duration)
	print(frame_interval)
	print(duration)
	frame_number = 0
	while True:
		ret, frame = cap.read()
		
		if not ret:
			continue

		if frame_number % frame_interval == 0:
			output_path = f"ctting_result/output_image_{frame_number}.jpg"
				# cv2.imshow("Video", frame)
			cv2.imwrite(output_path, frame)

		if frame_number >= (duration-1)*frame_interval:
			break
  
		cv2.waitKey(100)
		frame_number += 1

# cutting_data("peeking_3.mp4")
     