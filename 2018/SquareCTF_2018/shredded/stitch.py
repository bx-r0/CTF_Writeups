from PIL import Image
import zbarlight
import itertools
from pyzbar.pyzbar import decode

# TODO - Grab all permutations of a list

order = [
    # BORDER
    "11",

    # Square left
    "5", "6", "2", "25", "16", "15", "26", 
    
    "3", "21", "10", "23", "19", "20", "7", 
    
    # Square Right
    "8", "1", "4", "22", "24", "18", "14", 

    # BORDER
    "11"
]

def merge_images(file1name, file2name):
    image1 = Image.open(file1name)
    image2 = Image.open(file2name)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    total_width = width1 + width2
    total_height = max(height1, height2)

    result = Image.new("RGB", (total_width, total_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result

def append_onto_image(image1, file2name):
    image2 = Image.open(file2name)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    total_width = width1 + width2
    total_height = max(height1, height2)

    result = Image.new("RGB", (total_width, total_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result

def QR_Code_Valid(img):
    
    codes = decode(img)
    if not codes:
        return False
    else:
        return True

def generate_image(order):
    merge = merge_images(f"{order[0]}.png", f"{order[1]}.png")
    for i in range(2, len(order)):
        merge = append_onto_image(merge, f"{order[i]}.png")
    return merge

def QRCodeSearch(order):
    img = generate_image(order)
    valid = QR_Code_Valid(img)
    if valid:
        return img
    else:
        return None




# # # ============ BRUTE FORCING
# RIGHT
borders = ["8", "14"]
inner_border = ["1", "18"] # NOT shuffling
middle_right = ["4", "22", "24"]

borders_perm = list(itertools.permutations(borders))
middle_right_perm = list(itertools.permutations(middle_right))

right_side_combinations = []

for mid in middle_right_perm:
    for bord in borders_perm:
        new_list = []

        new_list.append(bord[0])
        new_list.append(inner_border[0])
        new_list += list(mid)
        new_list.append(inner_border[1])
        new_list.append(bord[1])

        right_side_combinations.append(new_list)

# Right side checksum
if len(right_side_combinations) != 12:
    print("Right side incorrect!")
    exit(0)

# MIDDLE
middle_border = ["3", "7"] #Not shuffling
black_sections = ["21", "23", "20"]
white_sections = ["10", "19"]

black_sections_perm = list(itertools.permutations(black_sections))
white_sections_perm = list(itertools.permutations(white_sections))

middle_combinations = []
for b in black_sections_perm:
    for w in white_sections_perm:
        new_list = []

        new_list.append(middle_border[0])
        new_list.append(b[0]) #B
        new_list.append(w[0]) #W
        new_list.append(b[1]) #B
        new_list.append(w[1]) #W
        new_list.append((b[2])) #B
        new_list.append(middle_border[1])

        middle_combinations.append(new_list)

# Middle check!
if len(middle_combinations) != 12:
    print("Middle incorrect!")
    exit(0)


# LEFT
l_left_border = ["5", "6"] #No shuffle
l_middle = ["2", "25", "16"]
l_right_border = ["15", "26"] #No Shuffle

l_middle_perm = list(itertools.permutations(l_middle))

left_side_combinations = []
for m in l_middle_perm:
    new_list = []

    new_list += l_left_border
    new_list += list(m)
    new_list += l_right_border

    print(new_list)

    left_side_combinations.append(new_list)

# Left check!
if len(left_side_combinations) != 6:
    print("Left incorrect!")
    exit(0)

total_combinations = len(right_side_combinations) * len(middle_combinations) * len(left_side_combinations)
checked = 0

print("Pre computation complete!")


for left in left_side_combinations:
    for mid in middle_combinations:
        for right in right_side_combinations:
            test_list = []

            test_list += list(left)
            test_list += list(mid)
            test_list += list(right)

            # # Saving files!
            # r = generate_image(test_list)
            # r.save(f"./poss/{checked}.png")

            # Checking files!
            r = QRCodeSearch(test_list)
            if r is not None:
                r.save("FLAG.png")
                print("QR Found!")
                exit(0)
            
            checked += 1
            print(f"{checked}/{total_combinations}", end='\r')