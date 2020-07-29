import glob
from pathlib import Path
from queue import Queue
from threading import Thread


def count_words_file(file_path: Path) -> int:
    with open(file_path) as input_file:
        file_data = input_file.read()
        return len(file_data.split())


def count_words_sequential(glob_string: str) -> int:
    return sum(count_words_file(Path(file_path)) for file_path in glob.glob(glob_string) if Path(file_path).is_file())


def count_words_threading(glob_string: str) -> int:
    results_queue = Queue()
    threads = list()

    for file_name in glob.glob(glob_string):
        file_path = Path(file_name)
        if file_path.is_file():
            thread = Thread(target=count_words_to_queue, args=(file_path, results_queue))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

    total_lines = 0
    while not results_queue.empty():
        total_lines += results_queue.get()

    return total_lines


def count_words_to_queue(file_path: Path, queue: Queue):
    queue.put(count_words_file(file_path))
