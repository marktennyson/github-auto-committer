import os as os
import time as tm
import uuid as uuid
import click as c

from datetime import datetime as dt

BASEDIR = os.path.abspath(os.curdir)
RANGE_COUNT = 2

def change_file_data():
    with open(os.path.join(BASEDIR, 'file.txt'), 'a') as f:
        f.write(str(uuid.uuid4())+"\n")

def add_file_to_track():
    resp = os.popen("git add .")
    data = resp.read()
    c.secho(str(data), fg="blue")

def make_commit():
    resp = os.popen(f'git commit -m "rand commit: {uuid.uuid4()}"')
    data = resp.read()
    c.secho(str(data), fg="green")

def make_push():
    resp = os.popen('git push')
    data = resp.read()
    c.secho(str(data), fg="yellow")

@c.command()
@c.option('-c', '--count', default=RANGE_COUNT, help='Provide the range count for the total commit')
def main(count):
    for i in range(count):
        c.secho(f"Process started at: {dt.now()}")
        c.secho(f"Performing the commit count: {i+1}")
        change_file_data()
        add_file_to_track()
        make_commit()
        make_push()
        c.secho(f"Process completed at: {dt.now()}")

if __name__ == "__main__":
    main()