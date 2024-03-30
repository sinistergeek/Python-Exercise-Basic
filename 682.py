class GetLoogLines(object):
    def __init__(self,log_file):
        self.log_file = log_file
        self.line = None
    def __iter__(self):
        return self
    def __next__(self):
        if self.line is None:
            self.line = read_line(log_file)
        while not complex_condition(self.line):
            self.line = read_line(self.log_file)
        return self.line
log_lines = GetLogLines(huge_log_file)
