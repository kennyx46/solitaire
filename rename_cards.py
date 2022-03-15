import os
import shutil

names = ['diamonds', 'hearts', 'clubs', 'spades']

multiplicator = 1
os.makedirs('renamed', exist_ok=True)
for name in names:
    for i in range(1, 14):
        image_number = i * multiplicator
        if image_number >= 37:
            image_number += 1
        filename = str(image_number).zfill(4)
        # os.rename(f"{filename}.png", f"{name}{i}.png")
        shutil.copy(f"big-cards-rename/{filename}.png", f"renamed/{name}{i}.png")
    multiplicator += 1