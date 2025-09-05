from business_object.Attack.abstract_attack import AbstractAttack

class FixedDamageAttack(AbstractAttack):
    def __init__(self, power=0, name=None, description=None):
        super().__init__(
            power=power,
            description=description,
            name=name,
        )

    def compute_damage(self,APkm,DPkm):
        return self._power
