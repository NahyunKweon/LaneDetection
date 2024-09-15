from picamera2 import Picamera2, Preview
import threading
import time
import os

# 현재 작업 디렉토리 경로 가져오기
SAVE_FOLDER = os.getcwd()
#j6otYR0esZHr4gckrY4UE4C2JofQPi1aalwc
# 카메라 설정
picam2 = Picamera2()

# 미리보기 활성화
picam2.start_preview(Preview.DRM, x=100, y=100, width=640, height=480)  # 미리보기 활성화, 적절한 옵션으로 설정
preview_config = picam2.create_preview_configuration({"size": (640, 360)})
capture_config = picam2.create_still_configuration()
picam2.configure(preview_config)
def capture_photos():
    count = 0
    while True:
        count += 1
        photo_path = os.path.join(SAVE_FOLDER, f'image_{count}.jpg')
        try:
            picam2.switch_mode_and_capture_file(capture_config, photo_path)
            
            #picam2.capture_file(photo_path)
            print(f'Saved {photo_path}')
        except Exception as e:
            print(f'Error capturing image: {e}')
        time.sleep(5)  # 5초 대기

if __name__ == '__main__':
    # 스레드 시작
    photo_thread = threading.Thread(target=capture_photos)
    photo_thread.daemon = True
    photo_thread.start()

    try:
        while True:
            time.sleep(1)  # 메인 스레드가 종료되지 않도록 유지
    except KeyboardInterrupt:
        print("프로그램 종료")
