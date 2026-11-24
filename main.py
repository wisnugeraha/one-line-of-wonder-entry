import os

line = "a paper boat, folded and wet, now carrying the whole sky"
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line + "\n")
