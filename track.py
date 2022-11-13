class Track:
    def __init__(self, length):
        self.length = length

    def track_compiler(self):
        output = list(self.length * "_" + "|")
        return output
race_track = Track(20)