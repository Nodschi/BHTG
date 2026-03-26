
from game.hazards import CircleZone

HAZARD_MAP = {
    "circle_zone": CircleZone,

}

class Level:
    def __init__(self, events):
        self.events = sorted(events, key=lambda e: e["time"])
        self.time = 0
        self.index = 0

    def upadte(self, dt, manager):
        self.time += dt

        while self.index < len(self.events) and self.events[self.index]["time"] <= self.time:
            self.spawn(self.events[self.index], manager)
            self.index += 1

    def spawn(self, event, manager):
        print(event)

    def get_hazard(self, event):
        hazard_type = event["type"]
        

        hazard_class = HAZARD_MAP.get(hazard_type)

        if hazard_class is None:
            raise ValueError("No class with this name found")
        
        data = {k: v for k, v in event.items() if k not in ("type", "time")}

        return hazard_class(**data)


