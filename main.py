import time
from datetime import datetime
import glob
import os


def get_lastest_file(path):
    # * means all if need specific format then *.csv
    list_of_files = glob.glob(path+'/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def follow(path):
    path.seek(0, 2)
    while True:
        line = path.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def main(path):
    latest_file = get_lastest_file(path)
    print(latest_file)
    logfile = open(latest_file, "r")
    loglines = follow(logfile)
    for line in loglines:
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%Y-%b-%d (%H:%M:%S.%f)")
        print(f'{timestampStr}: {line.rstrip()}')


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="This script print last line")
    parser.add_argument("-p", "--path", help="FiveM log path")
    args = parser.parse_args()
    path = args.path
    if not path:
        username = os.getlogin()
        print(f'username {username}')
        path = f'C:\\Users\\{username}\\AppData\\Local\\FiveM\\FiveM.app\\logs'
    main(path)
