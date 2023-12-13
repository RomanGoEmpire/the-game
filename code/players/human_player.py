from .player import Player
class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def play_card(self, stack) -> (int, int):
        print(f"Your hand: {self.hand}") 
        while True:
            card = int(input("Which card do you want to play? "))
            if card in self.hand:
                break
            else:
                print("Invalid card. Please try again.")
        while True:
            index = int(input("Which index do you want to place it? "))
            if index in [0, 1, 2, 3]:
                break
            else:
                print("Invalid index. Please try again.")
        if stack.is_legal(card, index):
            return card, index
        else:
            print("Illegal move.")
            return self.play_card(stack)
        
    def continue_turn(self) -> bool:
        return bool(int(input("Do you want to continue? 1 for yes, 0 for no: ")))