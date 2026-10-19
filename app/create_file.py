import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    file_name = None
    dir_parts = []

    if "-d" in args:
        d_idx = args.index("-d")
        end_idx = args.index("-f") if ("-f" in args and args.index("-f")
                                       > d_idx) else len(args)
        dir_parts = args[d_idx + 1 : end_idx]

    if "-f" in args:
        f_idx = args.index("-f")
        file_name = args[f_idx + 1]

    target_dir = ""
    if dir_parts:
        target_dir = os.path.join(*dir_parts)
        os.makedirs(target_dir, exist_ok=True)

    if file_name:
        file_path = os.path.join(target_dir, file_name) \
            if target_dir else file_name

        lines = []
        while True:
            line = input("Enter content line:")
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_path, "a") as file:
            file.write(f"{timestamp}\n")
            for index, content in enumerate(lines, start=1):
                file.write(f"{index} {content}\n")


if __name__ == "__main__":
    main()
