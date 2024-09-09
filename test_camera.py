#from picamera2 import Picamera2
#picam = Picamera2()
#picam.start()
#picam.capture_file("image.jpg")

import time
from picamera import PiCamera
from picamera.array import PiRGBArray
from PIL import Image
import io

# 카메라 초기화
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

# PiRGBArray 객체 생성
rawCapture = PiRGBArray(camera, size=(640, 480))

# 카메라 초기화에 시간 지연 추가
time.sleep(2)

try:
    # 카메라에서 프레임을 가져와서 실시간으로 보여줍니다.
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        
        # 이미지를 PIL로 변환
        pil_image = Image.fromarray(image)
        
        # 이미지를 화면에 표시
        pil_image.show()
        
        # rawCapture 배열을 초기화하여 다음 프레임 준비
        rawCapture.truncate(0)
        
        # 이미지가 표시되기 전에 잠시 대기
        time.sleep(0.03)  # 30ms 대기

except KeyboardInterrupt:
    pass

finally:
    # 모든 윈도우 닫기
    pil_image.close()