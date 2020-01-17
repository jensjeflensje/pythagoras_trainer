from PIL import Image, ImageDraw, ImageFont
import string
import random
import math


def _scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest


def create_triangle():
    dimensions = (512, 512)
    padding = 50

    font = ImageFont.truetype("font.otf", 48)

    im = Image.new('RGBA', dimensions)
    draw = ImageDraw.Draw(im)
    p1 = (padding, padding)
    p2 = (dimensions[0] - padding, dimensions[1] - padding)
    p3 = (padding, dimensions[0] - padding)
    draw.polygon([p1, p2, p3], fill=(0, 0, 0, 150))

    rand = random.randint(0, len(string.ascii_uppercase) - 1 - 3)
    print(rand)
    all_chars = list(string.ascii_uppercase)
    print(all_chars)
    chars = all_chars[rand:rand+3]

    points = [p3, p2, p1]

    print(chars)

    # draw chars at points
    i = 0
    for point in points:
        draw.text((point[0], point[1] - 35), chars[i], (200, 0, 50), font=font)
        i += 1

    char_point_pairs = []

    # collect pairs
    i = 0
    for char in chars:
        i2 = 0
        for char2 in chars:
            if char != char2:
                data = {
                    "chars": [char, char2],
                    "points": [points[i], points[i2]],
                    "longest": False,
                    "draw": True,
                }
                char_point_pairs.append(data)
            i2 += 1
        i += 1

    print(char_point_pairs)

    # remove double pairs
    for pair in char_point_pairs:
        char_pair1 = pair["chars"]
        for pair2 in char_point_pairs:
            char_pair2 = pair2["chars"]
            if char_pair1[0] == char_pair2[1] and char_pair1[1] == char_pair2[0]:
                char_point_pairs.remove(pair2)

    print(char_point_pairs)

    char_point_pairs[-1]["longest"] = True
    lengths = [random.randint(25, 200) for x in range(0, 2)]
    longest = math.sqrt((lengths[0] ** 2) + (lengths[1] ** 2))
    lengths.sort()
    lengths = _scrambled(lengths)
    print(lengths)

    char_point_pairs[0]["length"] = lengths[0]
    char_point_pairs[1]["length"] = lengths[1]
    char_point_pairs[2]["length"] = round(longest)

    char_point_pairs[random.randint(0, len(char_point_pairs) - 1)]["draw"] = False

    print(char_point_pairs)

    answer = None

    i = 0
    for pair in char_point_pairs:

        if i == 0:
            x = round(dimensions[0] / 2)
            y = dimensions[1] - padding
        elif i == 1:
            x = round(padding / 2)
            y = round(dimensions[1] / 2)
        elif i == 2:
            x = round(dimensions[0] / 2)
            y = round(dimensions[1] / 2)
        if pair["draw"]:
            draw.text((x, y), str(pair["length"]), (50, 0, 200), font=font)
        else:
            answer = pair["length"]
            draw.text((x, y), "?", (50, 0, 200), font=font)
        i += 1

    return im, char_point_pairs, answer


create_triangle()[0].save("result.png")
