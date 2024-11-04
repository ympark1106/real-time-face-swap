import cv2

def check_cameras():
    for i in range(5):  # 여러 인덱스를 시도 (0, 1, 2, ...)
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera is accessible at index {i}")
            cap.release()
            return i  # 접근 가능한 카메라 인덱스를 반환
        cap.release()
    print("No accessible cameras found.")
    return None

index = check_cameras()
if index is not None:
    print(f"Camera accessible at index {index}")
else:
    print("No camera found.")