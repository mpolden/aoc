#!/usr/bin/env python3

from datetime import datetime
from util import read_input


def parse_event(line):
    date = datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
    text = line[19:]
    return dict(date=date, text=text)


assert parse_event("[1518-09-26 23:59] Guard #2851 begins shift") == {
    "date": datetime(1518, 9, 26, 23, 59),
    "text": "Guard #2851 begins shift",
}


def read_events():
    events = []
    with read_input(4) as f:
        for line in f:
            events.append(parse_event(line.strip()))
    events.sort(key=lambda event: event["date"])
    return events


read_events()[:10]
