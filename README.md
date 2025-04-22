# ByteBomber

ByteBomber is a tool for createing a ZIP bombs. A ZIP bomb is a highly compressed ZIP file that massively expands in size when extracted. ByteBomber is designed to demonstrate how compression algorithms (specifically ZIP's DEFLATE) can be used to exhaust system resources (disk space, RAM, or CPU), potentially crashing systems or causing instability.

## Installation

To install ByteBomber, run the following command: `pip install bytebomber` (Alternatively, use `pip3` if necessary.)

Once installed, you can integrate ByteBomber into your own project by importing the `build_zip_bomb` function: `from ByteBomber import build_zip_bomb`

You can then call `build_zip_bomb()` in your code to generate ZIP bombs.

## What ByteBomber Does

1. Takes input for how big the uncompressed bomb should be.
2. Takes input for how large each individual payload file should be.
3. Generates a file filled with null bytes (`\x00`) of that size.
4. Creates a ZIP archive containing that file duplicated many times.
5. Applies DEFLATE compression to exploit redundancy.

Since every payload file is identical and filled with zeroes, compression is extremely effective—producing a small ZIP file that expands drastically when extracted.

## CLI

When you run the script, you'll be prompted for the following:

`Bomb decompressed size:`

- This is the total uncompressed size you want the final ZIP bomb to expand to.
- Default is 500 GB.

`Payload file size:`

- Size of the individual file inside the ZIP archive.
- The smaller this is, the more files the ZIP bomb will contain.
- Default is 1 MB.

`Output zip name:`

- Name of the final ZIP file to be created.
- Default is `bomb.zip`.

`Bomb directory name:`

- Directory where files are extracted when the bomb is decompressed.
- Default is `bomb-dir`.

Use the format `<number> <unit>` when entering values (e.g., `500 GB`, `1 TB`).

| Supported Unit | Size     | Size In Bytes                     |
| -------------- | -------- | --------------------------------- |
| B (byte)       | 1 B      | 1                                 |
| KB (Kilobyte)  | 1,024 B  | 1,024                             |
| MB (Megabyte)  | 1,024 KB | 1,048,576                         |
| GB (Gigabyte)  | 1,024 MB | 1,073,741,824                     |
| TB (Terabyte)  | 1,024 GB | 1,099,511,627,776                 |
| PB (Petabyte)  | 1,024 TB | 1,125,899,906,842,624             |
| EB (Exabyte)   | 1,024 PB | 1,152,921,504,606,846,976         |
| ZB (Zettabyte) | 1,024 EB | 1,180,591,620,717,411,303,424     |
| YB (Yottabyte) | 1,024 ZB | 1,208,925,819,614,629,174,706,176 |

> [!NOTE]
> For most purposes, GB or TB ranges are more than sufficient to stress a system. PB, EB, ZB, and YB represent astronomical data sizes far beyond what typical systems can handle.

Once input is provided, a summary of the configuration is shown:

```
Creating ZIP bomb:

    Payload size:         1048576 bytes
    Total uncompressed:   536870912000 bytes
    File count:           512000
    Output:               bomb.zip
```

- Payload size: Size of the file being copied inside the ZIP.
- Total uncompressed: Target final size when the ZIP is extracted.
- File count: How many copies of the payload file are added.
- Output: Filename of the ZIP bomb.

It will then show live progress as files are added to the ZIP.

## What's in the ZIP

Inside the ZIP there are tens of thousands to millions of identical files like:

- 0.txt
- 1.txt
- 2.txt
- ...

All filled with null bytes. The compression algorithm detects repetition and compresses it heavily.

> [!WARNING] > **ByteBomber is for educational purposes only. Do not deploy ZIP bombs on systems you do not own or have permission to test. Misuse can result in data loss or system damage.**
