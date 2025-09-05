from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    def __init__(self, power=0, name=None, description=None):
        self._power = power
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(self,APkm,DPkm):
        pass
