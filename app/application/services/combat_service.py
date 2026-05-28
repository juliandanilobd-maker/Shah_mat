class CombatService:

    def attack(self, attacker, defender):
        if attacker.attack_value <= defender.defense:
            return {"type": "BLOCKED"}

        defender.recieve_attack(attacker.attack_value)
        return {"type": "DAMAGE", "defender": defender}
