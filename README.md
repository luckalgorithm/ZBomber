ByteBomber is a Python tool for creating ZIP bombs. It demonstrates how compression algorithms (specifically ZIP's DEFLATE) can exploit redundancy to create highly compressed files that expand drastically when extracted. It’s primarily for educational purposes to understand the impact of such files.

## Installation

Install ByteBomber via pip: `pip install bytebomber`

You can then use it in your project: `from bytebomber import build_zip_bomb`

## Usage

You can use ByteBomber as a Python module or directly from your command line.

### As a Python Module

Call `build_zip_bomb()` to create a ZIP bomb. You can pass several arguments to customize the behavior:

```
build_zip_bomb(
    target_input="500 GB",
    payload_input="1 MB",
    zip_name="bomb.zip",
    folder_name="bomb-dir",
    verbose=True,
    show_progress=True
)
```

| **Parameter** | Description |
|----------------| ----------------------------------------------------------------------------------|
| `target_input` | Total uncompressed size of the ZIP bomb. Default: prompts user or uses `"500 GB"`. |
| `payload_input` | Size of each file inside the ZIP. Smaller values = more files. Default: prompts user or uses `"1 MB"`. |
| `zip_name` | Output ZIP file name. Default: prompts user or uses `"bomb.zip"`. |
| `folder_name` | Internal folder name for the payload files. Default: prompts user or uses `"bomb_dir"`. |
| `verbose` | If `True`, shows config + summary output. Default: `True`. |
| `show_progress` | If `True`, shows a live progress bar. Default: `True`. |

### Command-Line Usage

When you run ByteBomber from your terminal, you can optionally use flags to customize its behavior:

```
bytebomber --target-size "100 GB" --payload-size "500 KB" --output "my_bomb.zip"
```

| **Flag** | **Long Flag** | Description |
|----------|---------------|--------------------------------------------------------------------|
| `-t`     | `--target-size` | Total uncompressed size of the ZIP bomb (e.g., `"500 GB"`). Default: `"500 GB"`. |
| `-p`     | `--payload-size` | Size of each file inside the ZIP (e.g., `"1 MB"`). Default: `"1 MB"`. |
| `-o`     | `--output`    | Output ZIP file name. Default: `"bomb.zip"`.                         |
| `-f`     | `--folder`    | Internal folder name for the payload files. Default: `"bomb-dir"`.   |
| `-n`     | `--no-progress` | Disable the live progress bar.                                     |
| `-q`     | `--quiet`     | Silence all output messages. |

---

Use the format `<number> <unit>` when entering values (e.g., `500 GB`, `1 TB`). ByteBomber supports B, KB, MB, GB, TB, PB, EB, ZB, and YB. Valuse in the GB-TB range are usually more than enough to stress a system. Values above TB are astronomical data zizes far more than most systems can handle.

> [!NOTE]
> The program accepts values using standard units (e.g., MB, GB), but internally it treats them as binary units (e.g., MiB, GiB).

**ByteBomber is for educational purposes only. Do not deploy ZIP bombs on systems you do not own or have permission to test. Misuse can result in data loss or system damage.**
