import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np


def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:
    temperature = {}

    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}

    data = pandas.DataFrame.from_dict(temperature, "index").sort_index()

    return data


def determine_anomalies(data):
    means = dict(data.mean())
    std_devs = dict(data.std())

    rooms = []
    top_bounds = {}
    bottom_bounds = {}

    for r in means:
        rooms.append(r)
        top_bounds[r] = means[r] + (2 * std_devs[r])
        bottom_bounds[r] = means[r] - (2 * std_devs[r])

    for index, row in data.iterrows():
        for name in rooms:
            temp_reading = row[name]
            if not pandas.isna(temp_reading) and (row[name] < bottom_bounds[name] or row[name] > top_bounds[name]):
                print(name + '\treading at ' + str(index) + ' is an annomaly. Value = ' + str(row[name]))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)
    determine_anomalies(data)

