import webdataset as wds
from tqdm.auto import tqdm

from webdataset_utils import Watcher


def f(l):
    for b in l:
        yield b+1


def foo(b):
    return b+1


ds = wds.Processor([1, 2, 3, 4], f)
ds = Watcher(ds)
