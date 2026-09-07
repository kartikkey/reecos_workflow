# Reecos

> A tiny local workflow for turning PDF and DOCX books into MP3 audiobooks.

This started as a very simple question: **if I have a book and want to listen to it, can I just convert the book into audio without building an app or paying for an API?**

The answer was yes.

Reecos is currently not an application. It is a deliberately minimal proof-of-concept workflow that runs locally on Windows:

```text
PDF / DOCX
    ↓
Extract text
    ↓
Local text-to-speech
    ↓
WAV
    ↓
FFmpeg
    ↓
ONE MP3 audiobook
```

## What it does

- Accepts `.pdf` and `.docx` books
- Extracts readable text locally
- Uses `pyttsx3` / Windows text-to-speech for narration
- Uses FFmpeg to convert the generated audio to MP3
- Processes every PDF/DOCX placed in `input/`
- Skips books whose MP3 already exists
- Requires no API key or cloud service

## Requirements

- Windows
- Python 3.10+ (tested during the initial prototype with Python 3.14)
- FFmpeg available on PATH

## Setup

Install the Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

Make sure FFmpeg works:

```powershell
ffmpeg -version
```

## Use it

1. Put your PDF or DOCX books inside `input/`.
2. Run:

```powershell
python .\convert.py
```

3. The resulting MP3 files appear in `output/`.

Example:

```text
reecos_workflow/
├── convert.py
├── requirements.txt
├── README.md
├── input/
│   └── my-book.docx
└── output/
    └── my-book.mp3
```

## Initial result

The first real test converted a **13h 24m book** into a single MP3 audiobook. The working prototype was assembled in roughly **15–20 minutes**, while the actual conversion/encoding took around **4 minutes** on the test machine.

The output was intentionally kept simple: one MP3 file for the whole book rather than a chapter-splitting pipeline.

## Why this exists

The interesting part of Reecos is not the complexity. There isn't much.

It is an experiment in solving a real problem with the smallest useful workflow before turning it into a full product.

The thought process was basically:

> I was working with a book and wanted to listen to it. I wondered if I could just turn it into an audiobook. I built the simplest version. It worked. Then I thought: maybe this should become an app that anyone can use.

So I gave the idea a name: **Reecos**.

Maybe it becomes a product. Maybe it stays a tiny useful tool. For now, the important thing is that the core idea works.

## Current scope

This is intentionally an early proof of concept.

Not included yet:

- UI
- Web app
- Mobile app
- OCR for scanned books
- Chapter detection
- Cloud processing
- AI narration
- M4B chapter/metadata generation

Those can come later if the idea proves useful.

## License

This project is currently an experimental personal project. A formal open-source license can be added when the project is ready for broader public use.
