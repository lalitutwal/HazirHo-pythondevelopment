# #!/usr/bin/env python3
import os

import face_recognition


def verify_images(image_path_1, image_path_2):
    print("[INFO] verify_images function initiated...")

    # Explicitly check if files exist before trying to load them
    if not os.path.exists(image_path_1):
        return {"error": f"File missing: {image_path_1}"}
    else:
        print(f"[INFO] {image_path_1} exists.")

    if not os.path.exists(image_path_2):
        return {"error": f"File missing: {image_path_2}"}
    else:
        print(f"[INFO] {image_path_2} exists.")

    print("[INFO] Loading image files...")
    img1 = face_recognition.load_image_file(image_path_1)
    img2 = face_recognition.load_image_file(image_path_2)

    print("[INFO] Generating face encodings...")
    try:
        encoding_1 = face_recognition.face_encodings(img1)[0]
    except IndexError:
        return {"error": f"No face found in {image_path_1}."}

    try:
        encoding_2 = face_recognition.face_encodings(img2)[0]
    except IndexError:
        return {"error": f"No face found in {image_path_2}."}

    TOLERANCE = 0.6
    matches = face_recognition.compare_faces(
        [encoding_1], encoding_2, tolerance=TOLERANCE
    )
    distance = face_recognition.face_distance([encoding_1], encoding_2)[0]

    return {
        "same_person": bool(matches[0]),
        "distance_score": round(float(distance), 4),
        "tolerance_threshold": TOLERANCE,
    }


if __name__ == "__main__":
    file_a = "person1.jpg"
    file_b = "person2.jpg"

    print(f"[START] Testing verification for {file_a} and {file_b}...")
    output = verify_images(file_a, file_b)

    print("\n--- RESULTS ---")
    print(output)
