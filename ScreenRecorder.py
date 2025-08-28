import pyautogui
import cv2
import numpy as np


def screen_record(filename="Recording.avi", fps=30.0):
    screen_size = pyautogui.size()
    resolution = (screen_size.width, screen_size.height)

    codec = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(filename, codec, fps, resolution)

    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 480, 270)

    print("🎥 Recording started. Press 'q' to stop.")

    try:
        while True:
            img = pyautogui.screenshot()

            frame = np.array(img)

            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            out.write(frame)

            cv2.imshow("Live", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("🛑 Recording stopped by user.")
                break
    except KeyboardInterrupt:
        print("🛑 Recording stopped with Ctrl+C.")
    finally:
        out.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    screen_record("Recording.avi", fps=30.0)
