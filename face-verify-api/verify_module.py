import os
import face_recognition

# this is a module for comparing and creating face encodings

def image_exists(
	image_path):
    if not os.path.exists(image_path):
        return False
    return True


def create_encoding(
	image_path):
    print(f"[INFO] Creating encoding for {image_path}...")
    img = face_recognition.load_image_file(image_path)
    try:
        encoding = face_recognition.face_encodings(img)[0]
        return encoding
    except IndexError:
        return {"error": f"No face found in {image_path}."}


def compare_encodings(
	encoding_1,
	encoding_2):
    print("[INFO] compare_encodings function initiated...")
    result = face_recognition.compare_faces([encoding_1], encoding_2, tolerance=0.6)
    return result


def verify_images(
	image_path_1,
	image_path_2):
    print("[INFO] verify_images function initiated...")

    # Explicitly check if files exist before trying to load them
    if not image_exists(image_path_1):
        return {"error": f"File missing: {image_path_1}"}
    if not image_exists(image_path_2):
        return {"error": f"File missing: {image_path_2}"}
 

    print("[INFO] Loading and Generating face encodings...")
    encoding_1 = create_encoding(image_path_1)
    encoding_2 = create_encoding(image_path_2)

    matches = compare_encodings(encoding_1, encoding_2)

   # distance = face_recognition.face_distance([encoding_1], encoding_2)[0]

    return {
        "same_person": bool(matches[0]),
        #"distance_score": round(float(distance), 4),
    }
