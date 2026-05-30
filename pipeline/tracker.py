from collections import defaultdict

class VisitorTracker:

    def __init__(self):

        self.visitors = {}

        self.counter = 0

    def assign(self, track_id):

        if track_id not in self.visitors:

            self.counter += 1

            self.visitors[track_id] = (
                f"VIS_{self.counter}"
            )

        return self.visitors[track_id]