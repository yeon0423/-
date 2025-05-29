import os
from tkinter import *
from PIL import Image as Image_k
from PIL import ImageTk
import CallAPI
import random

IMG_DIR = "/Users/hayeon/ㅇ/----teamproject/images"  #이미지 경로 변경 (내 컴퓨터에 맞게)

def show_image():
    try:
        if 'window' in globals() and isinstance(window, Tk):
            pass
        else:
            window = Tk()
            window.title("미세먼지 측정기")
            window.geometry("700x500")

        img_path_good = [os.path.join(IMG_DIR, fname) for fname in [
            "KakaoTalk_20250525_094734829_03.jpg",
            "KakaoTalk_20250525_094734829_06.jpg",
            "KakaoTalk_20250525_094734829_13.jpg",
            "KakaoTalk_20250525_094734829_15.jpg",
            "KakaoTalk_20250525_094734829_17.jpg",
            "KakaoTalk_20250525_094734829_20.jpg",
        ]]

        img_path_soso = [os.path.join(IMG_DIR, fname) for fname in [
            "KakaoTalk_20250525_094734829_02.jpg",
            "KakaoTalk_20250525_094734829_08.jpg",
            "KakaoTalk_20250525_094734829_11.jpg",
            "KakaoTalk_20250525_094734829_18.jpg",
        ]]

        img_path_bad = [os.path.join(IMG_DIR, fname) for fname in [
            "KakaoTalk_20250525_094734829_01.jpg",
            "KakaoTalk_20250525_094734829_04.jpg",
            "KakaoTalk_20250525_094734829_07.jpg",
            "KakaoTalk_20250525_094734829_09.jpg",
            "KakaoTalk_20250525_094734829_16.jpg",
        ]]

        img_path_too_bad = [os.path.join(IMG_DIR, fname) for fname in [
            "KakaoTalk_20250525_094734829_05.jpg",
            "KakaoTalk_20250525_094734829_10.jpg",
            "KakaoTalk_20250525_094734829_12.jpg",
            "KakaoTalk_20250525_094734829_14.jpg",
            "KakaoTalk_20250525_094734829_19.jpg",
        ]]

        selected_img_path1 = random.choice(img_path_good)
        selected_img_path2 = random.choice(img_path_soso)
        selected_img_path3 = random.choice(img_path_bad)
        selected_img_path4 = random.choice(img_path_too_bad)

        desired_width = 500
        desired_height = 300

        if CallAPI.c == 1:
            image_path = selected_img_path1
            label_text = "오늘의 미세먼지는 좋음입니다"
        elif CallAPI.c == 2:
            image_path = selected_img_path2
            label_text = "오늘의 미세먼지는 보통입니다"
        elif CallAPI.c == 3:
            image_path = selected_img_path3
            label_text = "오늘의 미세먼지는 나쁨입니다"
        elif CallAPI.c == 4:
            image_path = selected_img_path4
            label_text = "오늘의 미세먼지는 매우나쁨입니다"
        else:
            label_text = "미세먼지 상태를 알 수 없습니다."
            image_path = None

        if image_path:
            if not os.path.exists(image_path):
                print(f"[Error] 이미지 파일이 없습니다: {image_path}")
                image_path = None

        if image_path:
            image = Image_k.open(image_path)
            try:
                resample_filter = Image_k.Resampling.LANCZOS
            except AttributeError:
                resample_filter = Image_k.LANCZOS

            resized_image = image.resize((desired_width, desired_height), resample_filter)
            photo = ImageTk.PhotoImage(resized_image)

            label_img = Label(window, image=photo)
            label_img.image = photo  # 참조 유지 필수
            label_img.pack(side="bottom", pady=20)

        label_text_label = Label(window, text=label_text)
        label_text_label.pack(side="top", pady=20)

        # mainloop는 중복 호출 막기 위해 전역 변수로 상태 확인 가능
        if not hasattr(show_image, "loop_started"):
            show_image.loop_started = True
            window.mainloop()

    except Exception as e:
        print(f"[show_image 함수 오류]: {e}")

