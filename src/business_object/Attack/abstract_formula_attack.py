from abc import ABC, abstractmethod
from random import uniform

from business_object.Attack.abstract_attack import AbstractAttack


class AbstractFormulaAttack(AbstractAttack, ABC):
    def __init__(self, power=0, name=None, description=None):
        super().__init__(
            power=power,
            description=description,
            name=name,
        )

    def compute_damage(self, APkm, DPkm):
        return (
            (
                (((2 * APkm.level) / 5 + 2) * self.power * self.get_attack_stat(self, APkm))
                / self.get_defense_stat(self, DPkm)
                * 50
            )
            + 2
        ) * uniform(0.85, 1)

    @abstractmethod
    def get_defense_stat(self, DPkm):
        pass

    @abstractmethod
    def get_attack_stat(self, APkm):
        pass
