from rpg_combat.character import Character


def test_character_starts_with_1000_health():
    wizard = Character()
    assert wizard.health == 1000

def test_character_level_starts_at_1():
    wizard = Character()
    assert wizard.level == 1
