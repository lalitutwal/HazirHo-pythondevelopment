import face_recognition


def verify_images(image_path_1, image_path_2):
    print("verify images function initiated...")

    # Load the image files
    try:
        img1 = face_recognition.load_image_file(image_path_1)
        img2 = face_recognition.load_image_file(image_path_2)
    except FileNotFoundError:
        return {"error": "files could not be found. please check file paths."}

    # Encoding the image
    try:
        encoding_1 = face_recognition.face_encodings(img1)[0]
    except IndexError:
        return {"error": f" image not found {image_path_1}."}

    try:
        encoding_2 = face_recognition.face_encodings(img2)[
            0
        ]  # [0] it is an array and should start from 0th index
    except IndexError:
        return {"error": f" image not found {image_path_2}."}

    # Compare the two faces
    TOLERANCE = 0.6  # it is default
    matches = face_recognition.compare_faces(
        [encoding_1], encoding_2, tolerance=TOLERANCE
    )

    # 4. Optional: Calculate the raw mathematical distance (lower distance = closer match)
    # distance = face_recognition.face_distance([encoding_1], encoding_2)[0]

    return {
        "same_person": bool(matches[0]),
        # "distance_score": round(float(distance), 4),
        "tolerance_threshold": TOLERANCE,
    }


# end: verify images func


if __name__ == "__main__":
    file_a = "person1.jpg"
    file_b = "person2.jpg"

    output = verify_images(file_a, file_b)

    print("\n--- RESULTS ---")
    print(output)
