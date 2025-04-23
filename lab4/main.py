#wzorzec projektowy: polecenie - wlaczanie/wylaczanie swiatla pilotem

from abc import ABC, abstractmethod

class Polecenie(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Swiatlo:
    def wlacz(self):
        print("Swiatlo wlaczone")

    def wylacz(self):
        print("Swiatlo wylaczone")


class WlaczSwiatloPolecenie(Polecenie):
    def __init__(self, swiatlo: Swiatlo):
        self.swiatlo = swiatlo

    def execute(self):
        self.swiatlo.wlacz()

    def undo(self):
        self.swiatlo.wylacz()

class WylaczSwiatloPolecenie(Polecenie):
    def __init__(self, swiatlo: Swiatlo):
        self.swiatlo = swiatlo

    def execute(self):
        self.swiatlo.wylacz()

    def undo(self):
           self.swiatlo.wlacz()


class Pilot:
    def __init__(self):
        self._polecenie = None
        self._history = []

    def ustaw_polecenie(self, polecenie: Polecenie):
        self._polecenie = polecenie

    def wcisnij_przycisk(self):
        if self._polecenie:
            self._polecenie.execute()
            self._history.append(self._polecenie)

    def wcisnij_cofnij(self):
        if self._history:
            polecenie = self._history.pop()
            polecenie.undo()


if __name__ == "__main__":
    swiatlo = Swiatlo()
    wlacz_swiatlo = WlaczSwiatloPolecenie(swiatlo)
    wylacz_swiatlo = WylaczSwiatloPolecenie(swiatlo)
    pilot = Pilot()

    pilot.ustaw_polecenie(wlacz_swiatlo)
    pilot.wcisnij_przycisk()    #swiatlo wlaczone

    pilot.ustaw_polecenie(wylacz_swiatlo)
    pilot.wcisnij_przycisk()    #swiatlo wylaczone

    pilot.wcisnij_cofnij()      #cofnij - swiatlo znowu wlaczone
    pilot.wcisnij_cofnij()      #cofnij - swiatlo wylaczone
