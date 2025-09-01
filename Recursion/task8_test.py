import unittest
from unittest.mock import patch
from task8 import find_files


class FakeEntry:
    def __init__(self, path, name, is_dir=False):
        self.path = path
        self.name = name
        self._is_dir = is_dir
    def is_dir(self):
        return self._is_dir


FS = {
    "/root": [
        FakeEntry("/root/a.txt", "a.txt"),
        FakeEntry("/root/sub",   "sub",   is_dir=True),
    ],
    "/root/sub": [
        FakeEntry("/root/sub/b.log", "b.log"),
    ],
    "/empty": []
}


def fake_scandir(path):
    return list(FS.get(path, []))


class TestTask8(unittest.TestCase):

    def test_find_files(self):
        with patch('task8.os.scandir', side_effect = fake_scandir):
            self.assertCountEqual(find_files("/empty"),[])

        with patch('task8.os.scandir', side_effect = fake_scandir):
            self.assertCountEqual(find_files("/root/sub"),["b.log"])    

        with patch('task8.os.scandir', side_effect = fake_scandir):
            self.assertCountEqual(find_files("/root"),["b.log","a.txt"])                      




        
        
        
if __name__ == '__main__':
    unittest.main()
   
   