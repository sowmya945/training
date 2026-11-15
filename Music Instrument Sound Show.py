from abc import ABC, abstractmethod


class Instrument(ABC):
    """Abstract base class representing a musical instrument."""

    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    @abstractmethod
    def play_sound(self) -> str:
        """Produce the sound unique to this instrument."""
        pass

    def describe(self) -> str:
        """Return a standard description shared by all instruments."""
        return f"{self.name} ({self.category} family)"


class Guitar(Instrument):
    def __init__(self, name: str, strings: int = 6):
        super().__init__(name, category="String")
        self.strings = strings

    def play_sound(self) -> str:
        return f"Strumming the {self.strings}-string {self.name}: Strum, twang, ring!"


class Drum(Instrument):
    def __init__(self, name: str, drum_type: str = "Acoustic"):
        super().__init__(name, category="Percussion")
        self.drum_type = drum_type

    def play_sound(self) -> str:
        return f"Beating the {self.drum_type} {self.name}: Boom, tap, crash!"


class Flute(Instrument):
    def __init__(self, name: str, material: str = "Silver"):
        super().__init__(name, category="Woodwind")
        self.material = material

    def play_sound(self) -> str:
        return f"Blowing into the {self.material} {self.name}: Toot, whistle, trill!"


def run_sound_show(instruments: list[Instrument]) -> None:
    """Demonstrate polymorphism by playing every instrument in the show."""
    print("=== Welcome to the Music Instrument Sound Show ===\n")
    for instrument in instruments:
        print(f"Instrument: {instrument.describe()}")
        print(f"Sound:      {instrument.play_sound()}\n")


if __name__ == "__main__":
    orchestra = [
        Guitar("Fender Stratocaster", strings=6),
        Drum("Snare Drum", drum_type="Marching"),
        Flute("Concert Flute", material="Silver"),
    ]
    run_sound_show(orchestra)
