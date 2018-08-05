from PIL import Image

training_data = []

def process_test_data(fpath):
    return [getAverageDominantColor(Image.open(str(fpath)))]

def average(ls):
    return sum(ls) / len(ls)

def isNotWhite(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    threshold = 10
    if abs(r - g) > threshold:
        if abs(g - b) > threshold:
            if abs(r - b) > threshold:
                return True
    return False

def getAverageDominantColor(img):
    dominant_colors = []
    colors = img.getcolors(maxcolors=99999999)  # used arbitrarily large number to emphasize that I WANT ALL THE DATA!
    for rgba in colors:
        if isNotWhite(rgba[1]):
            dominant_colors.append(rgba[1])
    red = [rgb[0] for rgb in dominant_colors]
    green = [rgb[1] for rgb in dominant_colors]
    blue = [rgb[2] for rgb in dominant_colors]
    final_color = (average(red), average(green), average(blue))
    return final_color

for num in range(1, 21):
    try:
        img = Image.open('pictures/ato' + str(num) + ".jpg")
    except IOError:
        try:
            img = Image.open('pictures/ato' + str(num) + ".jpeg")
        except IOError:
            img = Image.open('pictures/ato' + str(num) + ".png")

    dom_color = getAverageDominantColor(img)
    training_data.append(dom_color)

training_answers = ['a', 'a', 'o', 'a', 'o', 'o', 'a', 'a', 'o', 'a', 'a', 'o', 'a', 'o', 'o', 'o', 'a', 'a', 'o', 'a']