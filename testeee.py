from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Create a preview image of the ICRPG sheet styled like D&D (mockup visual)
width, height = 1240, 1754  # A4 at 150 DPI
bg_color = (245, 235, 215)  # 'papel' background color

# Create base image
img = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Load fonts (using default PIL font for demonstration)
title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 64)
header_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 28)
text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 20)

# Add title
draw.text((width // 2 - 250, 60), "ICRPG CHARACTER SHEET", fill=(30, 50, 90), font=title_font)

# Draw stat boxes
x_left = 100
y_start = 180
box_gap = 90
stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
for i, stat in enumerate(stats):
    draw.rectangle([x_left, y_start + i * box_gap, x_left + 300, y_start + 60 + i * box_gap], outline="black", fill=(220,220,220))
    draw.text((x_left + 10, y_start + 10 + i * box_gap), stat + ":", font=header_font, fill=(0, 0, 0))

# Draw HP / DEFENSE / HERO COIN row
draw.rectangle([x_left, 750, x_left + 900, 820], outline="black", fill=(220,220,220))
draw.text((x_left + 20, 765), "HP:", font=header_font, fill=(0,0,0))
draw.text((x_left + 200, 765), "DEFENSE:", font=header_font, fill=(0,0,0))
draw.text((x_left + 520, 765), "HERO COIN:", font=header_font, fill=(0,0,0))

# Draw sections for Loot, Abilities
draw.rectangle([x_left, 860, x_left + 500, 1060], outline="black")
draw.text((x_left + 10, 865), "LOOT", font=header_font, fill=(0,0,0))
draw.rectangle([x_left + 520, 860, x_left + 1020, 1060], outline="black")
draw.text((x_left + 530, 865), "ABILITIES", font=header_font, fill=(0,0,0))

# Draw final sections: Powers, Augments
draw.rectangle([x_left, 1100, x_left + 500, 1350], outline="black")
draw.text((x_left + 10, 1110), "POWERS", font=header_font, fill=(0,0,0))
draw.rectangle([x_left + 520, 1100, x_left + 1020, 1350], outline="black")
draw.text((x_left + 530, 1110), "AUGMENTS", font=header_font, fill=(0,0,0))

# Draw History box
draw.rectangle([x_left, 1400, x_left + 1020, 1700], outline="black")
draw.text((x_left + 10, 1405), "HISTORY", font=header_font, fill=(0,0,0))

# Show image
plt.figure(figsize=(8, 11))
plt.imshow(img)
plt.axis('off')
plt.tight_layout()
plt.show()