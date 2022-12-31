import os
import time

from colorama import Fore

os.system('cls')

filename = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt", ]


def animator(filename, delay=1, repeat=10):
    frames = []
    for name in filename:
        with open(name, "r", encoding="utf-8") as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print(Fore.YELLOW)
            print("".join(frame))
            time.sleep(delay)
            os.system('cls')


animator(filename, delay=0.1, repeat=4)

animator(filename, delay=0.3, repeat=4)

animator(filename, delay=0.5, repeat=4)
