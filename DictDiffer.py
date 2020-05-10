class DictDiffer(object):
    """
    Calculate the difference between two dictionaries as:
    (1) items added
    (2) items removed
    (3) keys same in both but changed values
    (4) keys same in both and unchanged values
    """

    def __init__(self, past, current):
        self.curr_dict, self.past_dict = current.__dict__, past.__dict__
        self.curr_keys, self.past_keys = set(current.__dict__.keys()), set(past.__dict__.keys())
        self.intersect = self.curr_keys.intersection(self.past_keys)

    def added(self):
        return self.curr_keys - self.intersect

    def removed(self):
        return self.past_keys - self.intersect

    def changed(self):
        return set(o for o in self.intersect if self.past_dict[o] != self.curr_dict[o])

    def unchanged(self):
        return set(o for o in self.intersect if self.past_dict[o] == self.curr_dict[o])

    def equal(self):
        return len(self.added() | self.removed() | self.changed()) == 0

    def equal_excl_lists(self):
        past_dict_entries_which_not_lists = dict(sorted(filter(lambda x: type(x[1]) is str, self.past_dict.items())))
        curr_dict_entries_which_not_lists = dict(sorted(filter(lambda x: type(x[1]) is str, self.curr_dict.items())))
        return past_dict_entries_which_not_lists == curr_dict_entries_which_not_lists
