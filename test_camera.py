#from picamera2 import Picamera2
#picam = Picamera2()
#picam.start()
#picam.capture_file("image.jpg")

from picamera2 import Picamera2, Preview
from PIL import Image
import io
import time

# Picamera2 객체 생성
picam2 = Picamera2()

# 카메라 구성
picam2.configure(picam2.create_still_configuration())

# 카메라 시작
picam2.start()

# 이미지 크기 설정
width, height = 640, 480

try:
    while True:
        # 이미지 캡처
        image = picam2.capture_array()

        # 이미지를 PIL로 변환
        pil_image = Image.fromarray(image)

        # 이미지를 화면에 표시
        pil_image.show()

        # 잠시 대기 (디스플레이 갱신을 위한)
        time.sleep(0.1)  # 100ms 대기

except KeyboardInterrupt:
    pass

finally:
    # 카메라 정지
    picam2.stop()
