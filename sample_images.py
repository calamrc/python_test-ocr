import os
import datetime

TIMEDELTA = datetime.timedelta(minutes=15)


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

    timestamp = datetime.datetime(**timestamp)

    return timestamp


def sample_images(image_timestamps, timedelta=TIMEDELTA):
    index = 0
    sample = list()
    while True:
        try:
            timestamp_to_find = image_timestamps.pop(index) + timedelta
            sample.append(timestamp_to_find)
            image_timestamps = image_timestamps[index::]
            index = image_timestamps.index(timestamp_to_find)
        except:
            return sample


files = os.listdir("images/")
images = [f for f in files if f.endswith(".jpg")]
image_timestamps = map(extract_timestamp, images)
image_timestamps.sort()

print(sample_images(image_timestamps))

# sample = list()
# for item in image_timestamps:
# image_timestamps.index(timestamp_to_find)

# print(len(sample))

# for item in image_timestamps[:50]:
# print(item, item + TIMEDELTA)
