# ZBomber

This script creates a ZIP bomb, a highly compressed ZIP file that massively expands in size when extracted. It's designed to demonstrate how compression algorithms (specifically ZIP's DEFLATE) can be misused to exhaust system resources (disk space, RAM, or CPU), potentially crashing systems or causing instability.

## What ZBomber Does

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
- Units supported: B, KB, MB, GB, TB, PB.
- Example: 500 GB

`Payload file size:`

- Size of the individual file inside the ZIP archive.
- Default is 1 MB.
- The smaller this is, the more files the ZIP bomb will contain.
- Example: 1 MB

`Output zip name:`

- Name of the final ZIP file to be created.
- Default is `bomb.zip`.

### After input

It prints out a summary:

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

- bomb_0.txt
- bomb_1.txt
- bomb_2.txt
- ...

All filled with null bytes. The compression algorithm detects repetition and compresses it heavily.

## Disclaimer

This tool is for educational purposes only. Do not deploy ZIP bombs on systems you do not own or have permission to test. Misuse can result in data loss or system damage.

Do not use this for pranks, attacks, or anything unethical or unauthorized.
