from rpg_combat.character import Character

def test_character_health_starts_at_1000():
  character = Character()
  assert character.health == 1000
