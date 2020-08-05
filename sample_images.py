import os
import datetime

TIMEDELTA = datetime.timedelta(minutes=15)
FIRST = 0
LAST = -1


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


def sample_images(image_timestamps, timedelta=TIMEDELTA, position=FIRST):
    image_timestamps.sort()

    index = 0
    attempts = 1
    timestamp_to_find = image_timestamps[index]
    samples = list()
    while True:
        try:
            print(
                "images remaining: {0}, sampled: {1}, to find: {2}, index: {3}, attempts: {4}".
                format(
                    len(image_timestamps), len(samples), timestamp_to_find,
                    index, attempts))
            matches = [
                item for item in image_timestamps
                if item.replace(second=0) == timestamp_to_find.replace(
                    second=0)
            ]
            samples.append(matches[position])
            # image_timestamps = image_timestamps[index::]
            index = image_timestamps.index(matches[position])
            timestamp_to_find = matches[position] + timedelta

            attempts = 1
        except Exception as e:
            attempts += 1
            if timestamp_to_find < max(image_timestamps):
                timestamp_to_find = timestamp_to_find + timedelta
            else:
                return samples


files = os.listdir("images/")
images = [f for f in files if f.endswith(".jpg")]
image_timestamps = map(extract_timestamp, images)

for item in sample_images(image_timestamps):
    print(item)

# sample = list()
# for item in image_timestamps:
# image_timestamps.index(timestamp_to_find)

# print(len(sample))

# for item in image_timestamps[:50]:
# print(item, item + TIMEDELTA)
