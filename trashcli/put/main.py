import os
import sys
from datetime import datetime

from trashcli.fstab import volumes
from trashcli.put.access import Access
from trashcli.put.file_trasher import FileTrasher
from trashcli.put.parent_path import parent_path
from trashcli.put.real_fs import RealFs
from trashcli.put.trash_directories_finder import TrashDirectoriesFinder
from trashcli.put.trasher import Trasher
from trashcli.put.user import User
from trashcli.trash import my_input
from trashcli.put.trash_put_cmd import TrashPutCmd


def main():
    file_trasher = FileTrasher(RealFs(),
                               volumes,
                               os.path.realpath,
                               datetime.now,
                               TrashDirectoriesFinder(volumes),
                               parent_path)
    access = Access()
    user = User(my_input)
    trasher = Trasher(file_trasher, user, access)
    cmd = TrashPutCmd(sys.stderr, trasher)
    return cmd.run(sys.argv, os.environ, os.getuid())
