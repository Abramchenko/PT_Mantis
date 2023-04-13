from sys import maxsize
import re


def clear_spaces(s):
    return re.sub(" {2}", " ", s)
class Project:

    def __init__(self, id=None, name=None, status=None, enabled=None, view_state=None, description=None):
        self.id = id
        self.name = name
        self.status = status
        self.enabled = enabled
        self.view_state = view_state
        self.description = description


    def __repr__(self):
        return "%s: %s" % (self.id, self.name)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (clear_spaces(self.name.strip()) == clear_spaces(other.name.strip()))

    def id_or_max(self):
        if self.id:
            return self.id
        else:
            return maxsize