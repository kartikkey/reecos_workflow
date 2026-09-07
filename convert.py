import subprocess
from pathlib import Path

import fitz
import pyttsx3
from docx import Document

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)
INPUT_DIR.mkdir(exist_ok=True)


def extract_text(file_path):
    extension = file_path.suffix.lower()

    if extension == ".pdf":
        print("  Reading PDF...")
        document = fitz.open(file_path)
        text = "\n\n".join(page.get_text("text") for page in document)
        document.close()
        return text

    if extension == ".docx":
        print("  Reading DOCX...")
        document = Document(file_path)
        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        )

    return ""


def create_audio(text, output_file):
    temp_wav = output_file.with_suffix(".temp.wav")

    print("  Generating speech...")
    print("  This may take a while for a large book.")

    engine = pyttsx3.init()
    engine.setProperty("rate", 165)
    engine.save_to_file(text, str(temp_wav))
    engine.runAndWait()

    print("  Converting to MP3...")

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(temp_wav),
            "-codec:a",
            "libmp3lame",
            "-b:a",
            "96k",
            "-ac",
            "1",
            str(output_file),
        ],
        check=True,
    )

    temp_wav.unlink(missing_ok=True)


def convert_book(file_path):
    print()
    print("=" * 60)
    print(f"BOOK: {file_path.name}")
    print("=" * 60)

    output_file = OUTPUT_DIR / f"{file_path.stem}.mp3"

    if output_file.exists():
        print("  MP3 already exists - skipping.")
        return

    text = extract_text(file_path).strip()

    if not text:
        print("  ERROR: No readable text found.")
        return

    print(f"  Characters: {len(text):,}")
    create_audio(text, output_file)

    print("\n  ✓ DONE")
    print(f"  → {output_file}")


def main():
    print()
    print("=" * 60)
    print("                    REECOS")
    print("              BOOK → AUDIOBOOK")
    print("=" * 60)

    files = sorted(
        file
        for file in INPUT_DIR.iterdir()
        if file.suffix.lower() in [".pdf", ".docx"]
    )

    if not files:
        print("\nNo PDF or DOCX files found in the input folder.")
        return

    print(f"\nFound {len(files)} book(s).")

    for file in files:
        convert_book(file)

    print("\n" + "=" * 60)
    print("                 ALL DONE")
    print("=" * 60)
    print(f"\nAudiobooks are in:\n{OUTPUT_DIR}\n")


if __name__ == "__main__":
    main()
