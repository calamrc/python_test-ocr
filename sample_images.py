import os


def extract_filename(filename):
    return os.path.splitext(filename)[0]


def extract_timestamp(filename, splitchar="_"):
    filename = extract_filename(filename)
    sections = filename.split(splitchar)
    timestamp = {}
    timestamp["year"] = int(sections[1][:4])
    timestamp["month"] = int(sections[1][4:6])
    timestamp["day"] = int(sections[1][-2:])
    timestamp["hour"] = int(sections[2])
    timestamp["minute"] = int(sections[3])
    timestamp["second"] = int(sections[4])
    return timestamp


files = os.listdir("images/")
images = [f for f in files if f.endswith(".jpg")]
images = map(extract_timestamp, images)

print(images[0])
