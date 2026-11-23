"""make.fun entry: The One-Line Laugh. Writes one funny line to /output/entry.txt."""
import os

LINE = "I built the flat-pack wardrobe perfectly, and the six leftover screws now sit in a jar on the shelf like they know something I don't."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
