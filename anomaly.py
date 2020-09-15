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
    room_name = 'lab1'
    filtered_data = data[room_name]
    filtered_data = filtered_data.dropna()

    mean = filtered_data.mean()
    std_dev = filtered_data.std()

    top_bound = mean + (2 * std_dev)
    bottom_bound = mean - (2 * std_dev)
    
    num_readings = len(filtered_data)
    num_bad_readings = 0
    bad_reading_indices = []
    
    for index, temp_reading in filtered_data.iteritems():
        if temp_reading < bottom_bound or temp_reading > top_bound:
            # print(room_name + '\treading at ' + str(index) + ' is an annomaly. Value = ' + str(temp_reading))
            num_bad_readings += 1
            bad_reading_indices.append(index)

    cleaned_reading_data = filtered_data.drop(index=bad_reading_indices)
    new_median = cleaned_reading_data.median()
    new_var = cleaned_reading_data.var()

    print('\n')
    print('Percentage/Fraction of Bad Readings for ' + room_name + ': ' + str((float(num_bad_readings) / num_readings) * 100) + '% (' + str(num_bad_readings) + '/' + str(num_readings) + ')')
    print('')
    print('With bad readings removed:')
    print('Median: ' + str(new_median))
    print('Variance: ' + str(new_var))
    print('')


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)
    determine_anomalies(data)
