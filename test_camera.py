from picamera2 import Picamera2, Preview
import threading
import time
import os

# 현재 작업 디렉토리 경로 가져오기
SAVE_FOLDER = os.getcwd()

# 카메라 설정
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())

# 미리보기 활성화
picam2.start_preview(Preview.QTGL)  # 미리보기 활성화, 적절한 옵션으로 설정

def capture_photos():
    count = 0
    while True:
        count += 1
        photo_path = os.path.join(SAVE_FOLDER, f'image_{count}.jpg')
        try:
            picam2.capture_file(photo_path)
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
