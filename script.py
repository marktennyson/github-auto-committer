import os as os
import time as tm
import uuid as uuid
import click as c
import typing as t

from io import StringIO
from nc_console import Console
from datetime import datetime as dt

if t.TYPE_CHECKING:
    from os import _wrap_close
    from io import BufferedRandom

BASEDIR:str = os.path.abspath(os.curdir)
RANGE_COUNT:int = 2

class GithubCommitter:
    def __init__(self) -> None:
        self.fileObj:"BufferedRandom" = open(os.path.join(BASEDIR, 'file.txt'), 'a')

    def __is_fatal_error(self, data:str) -> bool:
        if "fatal:" in data:
            self.buffer:"StringIO" = StringIO(data)
            return True
        else:
            return False

    def __get_fatal_error(self) -> str:
        lineStr:str = str()
        for line in self.buffer.readlines():
            if "fatal:" in line:
                lineStr = line
        return lineStr
        
    def change_file_data(self) -> t.Literal[True]:
        Console.log.Info("Started updating the file.")
        self.fileObj.write(str(uuid.uuid4())+"\n")
        Console.log.Success("File updating completed.")
        return True

    def add_file_to_track(self) -> bool:
        Console.log.Info("Started adding the file on git commit track.")
        resp:"_wrap_close" = os.popen("git add .")
        data:str = resp.read()
        if self.__is_fatal_error(data) is True:
            Console.log.Error("Some Error occured while adding the file on track.")
            Console.log.Error(self.__get_fatal_error())
            return False
        else:
            Console.log.Success("File successfully added on track.")
            return True

    def make_commit(self) -> bool:
        Console.log.Info("Committing is on the process........")
        resp:"_wrap_close" = os.popen(f'git commit -m "rand commit: {uuid.uuid4()}"')
        data:str = resp.read()
        if self.__is_fatal_error(data) is True: 
            Console.log.Error("Some Error occured while committing the file.")
            Console.log.Error(self.__get_fatal_error())
            return False
        else:
            Console.log.Success("File committed successfully.")
            return True

    def make_push(self) -> bool:
        resp:"_wrap_close" = os.popen('git push')
        data:str = resp.read()
        if self.__is_fatal_error(data) is True: 
            Console.log.Error("Some Error occured while pushing the file.")
            Console.log.Error(self.__get_fatal_error())
            return False
        else:
            Console.log.Success("File pushed successfully.")
            return True

@c.command()
@c.option('-c', '--count', default=RANGE_COUNT, help='Provide the range count for the total commit')
def main(count:int):
    for i in range(count):
        Console.log.Info(f"Process started at: {dt.now()}")
        Console.log.Info(f"Performing the commit count: {i+1}")
        committer:"GithubCommitter" = GithubCommitter()
        committer.change_file_data()
        aftt_resp:bool = committer.add_file_to_track()
        if aftt_resp is not True:
            Console.log.Error("Aborting......")
            os._exit(0)

        mc_resp:bool = committer.make_commit()
        if mc_resp is not True:
            Console.log.Error("Aborting......")
            os._exit(0)

        mp_resp:bool = committer.make_push()
        if mp_resp is not True:
            Console.log.Error("Aborting......")
            os._exit(0)

        Console.log.Success(f"Process completed at: {dt.now()}")

if __name__ == "__main__":
    t1:float = tm.time()
    main()
    t2:float = tm.time()
    Console.log.Info(f"Total time taken: {round((t2-t1), 2)}")