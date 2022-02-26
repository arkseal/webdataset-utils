import webdataset as wds

from .utils import combine_functions


def wrap_watcher(dataset, length=None):
    return Watcher(dataset, length)


class Watcher:
    def __init__(self, dataset, length=None) -> None:
        self.dataset = dataset
        if not isinstance(dataset, wds.Processor):
            self.dataset = wds.WebDataset(dataset)
        self.length = length

    def reset_length(self):
        self.length = None

    def __iter__(self):
        if self.length is not None:
            for item in self.dataset:
                yield item
        else:
            for length, item in enumerate(self.dataset, 1):
                yield item
            self.length = length

    def __len__(self):
        return self.length

    def __getattr__(self, name: str):
        f = getattr(self.dataset, name)
        if callable(f):
            self.length = None
            return combine_functions(f, wrap_watcher)
        return f
