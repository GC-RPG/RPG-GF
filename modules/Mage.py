from modules import Player, Dado

class Mage(Player):
    def __init__(self, name: str):
        super().__init__(name)
        self.intelligence = 25

    def attack(self, target: Player) -> None:
        dado = Dado(0)
        dado.jogar_dado()

        dano = dado.valor + self.intelligence
        target.take_damage(dano)

        print(f"{self.name} lançou uma magia em {target.name} causando {dano} de dano!")
        print(dado)