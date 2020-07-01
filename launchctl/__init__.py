__all__ = ["Job", "job", "jobs", "remove", "start", "stop", "unload", "load"]


import subprocess
import values

"""
https://ss64.com/osx/launchctl.html
"""


def remove(label):
    """`launchctl remove label`"""
    subprocess.check_call(["/bin/launchctl", "remove", str(label)])


def start(label):
    """`launchctl start label`"""
    subprocess.check_call(["/bin/launchctl", "start", str(label)])


def stop(label):
    """`launchctl stop label`"""
    subprocess.check_call(["/bin/launchctl", "stop", str(label)])


class Job:
    """launchctl Job class. attrs: `pid`, `status`, `label`"""
    string = None
    pid = None
    status = None
    label = None

    def __init__(self, string):
        self.parse(string)

    def parse(self, string):
        self.string = string
        values = list(filter(None, string.split(" ")))
        if "\t" in string:
            values = list(filter(None, string.split("\t")))
        self.pid = (int(values[0]) if values[0] != "-" else None)
        self.status = (int(values[1]) if values[1] != "-" else None)
        self.label = values[2]

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.__str__()


def jobs():
    """return a list of launchctl jobs"""
    result = []
    out = subprocess.check_output(["/bin/launchctl", "list"]).decode()
    for row in out.splitlines()[1:]:
        result.append(Job(row))
    return result


def _parse_value(string):
    return string.split(" = ")[1].replace(";", "").replace('"', "")


def _py_value(string):
    if string in ["true", "false"]:
        return string == "true"
    try:
        return int(string)
    except Exception:
        return string


def job(label):
    """return launchctl Job by label"""
    args = ["/bin/launchctl", "list", label]
    try:
        out = subprocess.check_output(args, stderr=subprocess.PIPE).decode()
    except subprocess.CalledProcessError:
        return {}
    result = dict()
    for l in out.splitlines():
        if '" =' in l:
            key = l.split('"')[1]
            if ";" in l:  # "key" = "value";
                result[key] = _py_value(_parse_value(l))
        if '=' not in l and '";' in l:  # "value";
            result[key] = result.get(key, []) + [l.split('"')[1]]
    return result


def load(args):
    """`launchctl load args ...`"""
    subprocess.check_call(["/bin/launchctl", "load"] + values.get(args))


def unload(args):
    """`launchctl unload args ...`"""
    subprocess.check_call(["/bin/launchctl", "unload"] + values.get(args))
