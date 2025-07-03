import cv2
import os

def extract_frames_to_folders(video_path, db_folder="database", query_folder="query", frame_interval=1):
    """
    Извлекает кадры из видео и поочередно сохраняет их в папки `database` и `query`.

    :param video_path: Путь к видеофайлу.
    :param db_folder: Папка для кадров "database".
    :param query_folder: Папка для кадров "query".
    :param frame_interval: Интервал между сохраняемыми кадрами.
    """
    # Создаем папки, если их нет
    os.makedirs(db_folder, exist_ok=True)
    os.makedirs(query_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Ошибка: Не удалось открыть видео.")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Обработка видео: {video_path}")
    print(f"Всего кадров: {total_frames}")

    db_count = 0
    query_count = 0

    for frame_count in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            # Четные кадры -> database, нечетные -> query
            if frame_count % 2 == 0:
                frame_name = os.path.join(db_folder, f"db_{db_count:06d}.jpg")
                db_count += 1
            else:
                frame_name = os.path.join(query_folder, f"query_{query_count:06d}.jpg")
                query_count += 1

            cv2.imwrite(frame_name, frame)

    cap.release()
    print(f"Сохранено в {db_folder}: {db_count} кадров")
    print(f"Сохранено в {query_folder}: {query_count} кадров")

if __name__ == "__main__":
    video_path = "input_video.mp4"  # Укажите ваш путь к видео
    extract_frames_to_folders(video_path)