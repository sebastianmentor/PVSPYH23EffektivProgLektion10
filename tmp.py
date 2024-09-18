from typing import Protocol
from enum import Enum, auto
import random

class KritiseraEnum(Enum):
    SMAK = "smak"
    KONSISTENS = "konsistens"
    LUKT = "lukt"
    FÄRG = "färg"
    TEMPERATUR = "temperatur"


class TestPoängEnum(Enum):
    EN_POÄNG = auto()
    TVÅ_POÄNG = auto()
    TRE_POÄNG = auto()
    FYRA_POÄNG = auto()
    FEM_POÄNG = auto()


class KritikerError(Exception):
    """Raised when a critic already has critict a specific thing"""
    ...


class Kritiker(Protocol):
    def klaga(self) -> str:
        ...


class Maträtt:
    def __init__(self, namn:str) -> None:
        self._namn = namn

    @property
    def namn(self) -> str:
        return self._namn
    
    def __hash__(self) -> int:
        return hash(self._namn)
    
    def __str__(self) -> str:
        return self._namn
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value,Maträtt):
            raise ValueError(f"Kan inte jämföra {value} med en Maträtt!")
        
        return value.namn == self._namn


class Matkritiker:
    def __init__(self, namn:str, erfarenhet:int) -> None:
        self.namn = namn
        self.erfarenhet = erfarenhet
        self._kritiserade_maträtter = {}
        self._test_poäng = list(TestPoängEnum)

    def kritisera_maträtt(self, test:KritiseraEnum, maträtt:Maträtt) -> None:
        if maträtt in self._kritiserade_maträtter:
            gjorda_tester = self._kritiserade_maträtter[maträtt]

            if test in gjorda_tester:
                raise KritikerError(f"Maträtten {maträtt} har redan testats för {test.value}")
            
            gjorda_tester[test] = random.choice(self._test_poäng)

        else:
            self._kritiserade_maträtter[maträtt] = {test:random.choice(self._test_poäng)}


    def klaga(self) -> str:
        return "Jag älskar att klaga på allt!!"




def lyssna_på_en_kritiker_klaga(kritiker:Kritiker) -> None:
    print(kritiker.klaga())

if __name__ == "__main__":
    # Bara lite snyggare namn
    kritisera:KritiseraEnum = KritiseraEnum
    # Skapar några shyssta kritiker
    sebastian = Matkritiker(namn="Sebastian", erfarenhet=0)
    kalle = Matkritiker(namn="Kalle", erfarenhet=3)

    # Smaskiga maträtter
    pylandia_pudding = Maträtt("Pylandia Pudding")
    bananbröd = Maträtt("Bananbröd")

    # Låt kritiken börja
    sebastian.kritisera_maträtt(kritisera('smak'), pylandia_pudding)
    sebastian.kritisera_maträtt(kritisera('smak'), bananbröd)

    kalle.kritisera_maträtt(KritiseraEnum.SMAK, pylandia_pudding)
    kalle.kritisera_maträtt(KritiseraEnum.SMAK, bananbröd)