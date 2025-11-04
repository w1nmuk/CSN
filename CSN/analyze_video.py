# analyze_video.py
from ultralytics import YOLO
import cv2

# 1. 모델 로드 (다운로드한 경로)
model = YOLO("models/yolov8s-face-lindevs.pt")

# 2. 테스트 이미지/영상 프레임
frame = cv2.imread("test_smile.jpg")  # 또는 영상에서 프레임 추출

# 3. 얼굴 검출
results = model(frame, conf=0.5)  # 신뢰도 50% 이상만

# 4. 결과 확인
for box in results[0].boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 5. 결과 저장 (GUI 없이!)
cv2.imwrite("output_with_faces.jpg", frame)
print("얼굴 검출 완료! 결과: output_with_faces.jpg")