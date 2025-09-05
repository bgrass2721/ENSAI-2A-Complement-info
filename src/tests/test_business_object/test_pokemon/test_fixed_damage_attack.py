from business_object.Attack.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic


class TestDefenderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        Calinerie = FixedDamageAttack(name="calinerie", power=1000)
        Mimiqui = AllRounderPokemon(stat_current=Statistic(sp_atk=100, sp_def=100))
        MonsieurMime = AllRounderPokemon(stat_current=Statistic(sp_atk=100, sp_def=100))
        # WHEN
        damage = Calinerie.compute_damage(Mimiqui, MonsieurMime)

        # THEN
        assert damage == 1000


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
