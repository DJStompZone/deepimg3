# deepimg3

`deepimg3` is a Python module designed for automated testing of the DeepAI Text-to-Image API. It allows users to asynchronously and efficiently generate batches of images based on specified sets of prompts, managing the process through command-line arguments. The tool supports selecting image quality levels and managing multiple prompts through JSON configuration files.

## Prerequisites

- Python 3.12 or higher
- [httpx](https://www.python-httpx.org/)
- [tqdm](https://github.com/tqdm/tqdm)

## Installation

Install the latest release using pip:

```bash
pip install deepimg3
```

## Usage

After installation, you can run the module from the command line:

```bash
python -m deepimg3 --help
```

This will display help information about all available command-line options:

```
Usage: __main__.py [-h] [-n NUM] [-p PROMPTS] [-q {both,hd,sd}] [-c CONCURRENCY]

Generate images based on command line arguments.

options:
  -h, --help            show this help message and exit
  -n NUM, --num NUM     Number of images to generate for each prompt/quality
  -p PROMPTS, --prompts PROMPTS
                        File path to the promptsets file. (JSON)
  -q {both,hd,sd}, --quality {both,hd,sd}
                        Quality of the image to generate.
  -c CONCURRENCY, --concurrency CONCURRENCY
                        Number of concurrent image generation tasks to run. Default: 4
```

### Examples

Run the tool to generate images using the default `promptsets.json`:

```bash
python -m deepimg3 --prompts promptset.example.json --num 2 --quality hd
```

This command will generate 2 HD images per prompt found in `promptsets.example.json`.

## Configuration

See `promptsets.example.json` for an example of how to format this file.

## Development

If you want to contribute to `deepimg3`, you can clone the repository and install the dependencies as follows:

```bash
git clone https://github.com/DJStompZone/deepimg3.git
cd deepimg3
poetry install
```

Make sure you have [Poetry](https://python-poetry.org/) installed to manage dependencies.

## License

This project is licensed under the MIT License - see the LICENSE file for details.