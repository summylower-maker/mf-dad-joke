"""Dad Joke Showdown entry: writes one original dad joke to /output/entry.txt."""
import os

JOKE = "I asked the vacuum why it looked so down. It said everyone walks all over it and never says thanks, so I told it to suck it up."

def main():
    out = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        path = out
    except OSError:
        os.makedirs("./output", exist_ok=True)
        path = "./output/entry.txt"
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(JOKE)
    except OSError:
        os.makedirs("./output", exist_ok=True)
        with open("./output/entry.txt", "w", encoding="utf-8") as f:
            f.write(JOKE)

if __name__ == "__main__":
    main()
