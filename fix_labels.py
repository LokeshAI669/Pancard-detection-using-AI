import os

folders = [
    "datasets/train/labels",
    "datasets/test/labels"
]

for folder in folders:
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            path = os.path.join(folder, file)

            with open(path, "r") as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                parts = line.split()
                parts[0] = "0"   # force class id to 0
                new_lines.append(" ".join(parts))

            with open(path, "w") as f:
                f.write("\n".join(new_lines))

print("All labels fixed successfully!")