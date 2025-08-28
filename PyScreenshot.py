import pyscreenshot


def take_screenshot(filename="screenshot.png", bbox=None):
    """
    Capture a screenshot.
    - filename: output file name
    - bbox: tuple (x1, y1, x2, y2). If None, capture full screen
    """
    if bbox:
        print(f"📸 Capturing partial screenshot {bbox}...")
    else:
        print("📸 Capturing full screen...")

    image = pyscreenshot.grab(bbox=bbox)

    image.show()

    image.save(filename)
    print(f"✅ Screenshot saved as {filename}")


if __name__ == "__main__":
    print("Choose option:")
    print("1. Full Screenshot")
    print("2. Partial Screenshot")
    choice = input("> ").strip()

    if choice == "1":
        take_screenshot("full_screenshot.png")
    elif choice == "2":
        print("Enter coordinates for partial screenshot (x1 y1 x2 y2):")
        coords = input("> ").split()
        if len(coords) == 4:
            x1, y1, x2, y2 = map(int, coords)
            take_screenshot("partial_screenshot.png", bbox=(x1, y1, x2, y2))
        else:
            print("❌ Invalid coordinates. Please enter 4 integers.")
    else:
        print("❌ Invalid choice.")
