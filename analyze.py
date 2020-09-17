#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).

It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.

Feel free to save your data in a better format--I was just showing what one might do quickly.
"""
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
    occupancy = {}
    co2 = {}

    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)

    for k in data:
        if k == 'temperature' or k == 'occupancy':
            data_title = 'lab1 ' + k[0].upper() + k[1:] + ' Data'
            print(data_title)
            print('Median: ' + str(data[k]['lab1'].median()))
            print('Variance: ' + str(data[k]['lab1'].var()))
            print('')

        plt.figure()
        data[k]['lab1'].plot.hist()
        plt.title('lab1 ' + k + ' Histogram')

        if k == 'temperature':
            plt.xlabel('Temperature')
        elif k == 'occupancy':
            plt.xlabel('Number of People')
        else:
            plt.xlabel('Units of CO2')
        

    time = data['temperature'].index
    time_deltas = time[1:] - time[:-1]
    time_intervals = [t.total_seconds() for t in time_deltas]
    time_series = pandas.Series(time_intervals)
    print('Time Interval Statistics')
    print('Mean: ' + str(time_series.mean()))
    print('Variance: ' + str(time_series.var()))
    print('')

    plt.figure()
    time_series.plot.hist()
    plt.title('Time Interval Histogram')
    plt.xlabel('Time (seconds)')

    plt.show()
