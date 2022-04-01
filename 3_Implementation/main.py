from random import randint
import time
class Box(object):
    sets = ["", "", "", "", "", "", "", ""]
    vals = [0, 0, 0, 0, 0, 0, 0, 0]
    def __init__(self):
        self.End_pts = 0
    def fill_sets(self):
        su = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(8):
            self.sets[i] = su[i]
    def fill_vals(self):
        for i in range(8):
            self.vals[i] = randint(1, 10)
    def shw_cube(self):
        for i in range(8):
            print(f"[{self.sets[i]}]", end="")
    def shw_val(self, i, Name):
        print(f"{Name} has reveled cube [{self.sets[i]}] with a value of {self.vals[i]}")
        self.sets[i] = str(self.vals[i])
    def update_End_pts(self):
        self.End_pts = self.End_pts + 1
    def check_choosen_already(self, cube):
        choosen = True
        for i in range(8):
            if cube == self.sets[i] and cube != str(self.vals[i]):
                choosen = False
                break
            elif cube == self.sets[i] and cube == str(self.vals[i]):
                choosen = True
                break
            else:
                choosen = True
        return choosen
class Participant(object):
    def __init__(self):
        self.Name = "CPU"
        self.Scoree = 0
    def Updte_Scoree(self, i):
        self.Scoree = self.Scoree + Box.vals[i]
    def Shw_Scoree(self):
        print(f"{self.Name} your Scoree is: {self.Scoree} ")
    def select_cube(self):
        print("Please enter the letter of your cube: ")
        cube = input().upper()
        choosen = Box.check_choosen_already(Box(), cube)
        while choosen is True:
            print("This cube was already choosen. Please select another one: ")
            cube = input().upper()
            choosen = Box.check_choosen_already(Box(), cube)
        for i in range(8):
            if cube == Box().sets[i]:
                self.Updte_Scoree(i)
                Box.shw_val(Box(), i, self.Name)
                self.Shw_Scoree()
    def check_winner(self, other_Scoree):
        if self.Scoree > other_Scoree:
            print(f"\nCONGRATULATIONS {self.Name} you have won!")
        elif self.Scoree < other_Scoree:
            print(f"\nSorry, {self.Name} you have lost. Good luck next time!")
        else:
            print(f"\nThere's a tie. Both of you won!")
class Cpu(Participant):
    def __init__(self):
        super(Participant).__init__()
        self.Name = "CPU"
        self.Scoree = 0
    def Shw_Scoree(self):
        print(f"CPU's Scoree is: {self.Scoree}")
    def select_cube(self):
        cube = Box().sets[randint(0, 7)]
        choosen = Box.check_choosen_already(Box(), cube)
        while choosen is True:
            cube = Box.sets[randint(0, 7)]
            choosen = Box.check_choosen_already(Box(), cube)
        for i in range(8):
            if cube == Box().sets[i]:
                self.Updte_Scoree(i)
                Box.shw_val(Box(), i, self.Name)
                self.Shw_Scoree()
class Player(Participant):
    def __init__(self):
        super(Participant).__init__()
        self.set_Name()
        self.Scoree = 0
    def set_Name(self):
        print("\nWhat is your Name? ")
        self.Name = input()
def menu():
    print("\n-welcome to my game-""\n\t1) Player Vs. CPU""\n\t2) Multiplayer""\n\t0) exit")
    print("\n\nSelect a game mode: ")
    optionn = input()
    return optionn
if __name__ == "__main__":
    opt = ""
    while opt != "0":
        cubee = Box()
        opt = menu()
        if opt == "1":
            print("\n\n[player vs cpu ]")
            cubee.fill_sets()
            cubee.fill_vals()
            player = Player()
            cpu = Cpu()
            while cubee.End_pts < 8:
                time.sleep(2)
                cubee.shw_cube()
                print(f"\n\n{player.Name} it's your turn")
                player.select_cube()
                cubee.update_End_pts()
                time.sleep(4)
                cubee.shw_cube()
                print("\n\nIt's the CPU'S turn")
                cpu.select_cube()
                cubee.update_End_pts()
            print("\nFinal Score: "f"\n{player.Name}: {player.Scoree}"f"\n{cpu.Name}: {cpu.Scoree}")
            player.check_winner(cpu.Scoree)
            input()
        elif opt == "2":
            print("\n[multiplayer]")
            cubee.fill_sets()
            cubee.fill_vals()
            player1 = Player()
            player2 = Player()
            while cubee.End_pts < 8:
                time.sleep(2)
                cubee.shw_cube()
                print(f"\n\n{player1.Name} it's your turn...")
                player1.select_cube()
                cubee.update_End_pts()
                time.sleep(2)
                cubee.shw_cube()
                print(f"\n\n{player2.Name} it's your turn...")
                player2.select_cube()
                cubee.update_End_pts()
            print("\nFinal Score: "f"\n{player1.Name}: {player1.Scoree}"f"\n{player2.Name}: {player2.Scoree}")
            player1.check_winner(player2.Scoree)
            player2.check_winner(player1.Scoree)
            input()