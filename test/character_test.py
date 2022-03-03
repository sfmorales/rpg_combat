from rpg_combat.character import Character


def test_character_health_starts_at_1000():
    character = Character()
    assert character.health == 1000


def test_character_level_starts_at_1():
    character = Character()
    assert character.level == 1


def test_character_starts_alive():
    character = Character()
    assert character.alive == True


def test_character_can_damage_character():
    alice = Character()
    bob = Character()
    old_bob_health = bob.health
    alice.attack(bob)
    assert bob.health < old_bob_health
