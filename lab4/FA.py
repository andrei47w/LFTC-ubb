class TransFunc:
    def __init__(self) -> None:
        self.elements = []

    def add(self, a: str, operation: str, b: str) -> None:
        self.elements.append([a, operation, b])

    def getA(self, index: int) -> str:
        if len(self.elements) > index:
            return self.elements[index][0]
        return None

    def getOP(self, index: int) -> str:
        if len(self.elements) > index:
            return self.elements[index][1]
        return None

    def getB(self, index: int) -> str:
        if len(self.elements) > index:
            return self.elements[index][2]
        return None

    def getSize(self) -> int:
        return len(self.elements)

    def __str__(self) -> str:
        return str(self.elements)

    def getResult(self, op: str, a: str):
        result = []

        for elem in self.elements:
            if a == elem[0] and op == elem[1]:
                result.append(elem[2])

        if len(result) != 1:
            return None

        return result[0]


class FA:
    def __init__(self, Q: list = [], Σ: list = [], δ: TransFunc = TransFunc(), q0: str = "", F: list = []) -> None:
        self.Q = Q
        self.E = Σ
        self.S = δ
        self.q0 = q0
        self.F = F

    def __str__(self) -> str:
        return \
            "Q = " + str(self.Q) + '\n' \
            + "Σ = " + str(self.E) + '\n' \
            + "δ = " + str(self.S) + '\n' \
            + "q0 = " + str(self.q0) + '\n' \
            + "F = " + str(self.F) + '\n'

    def scan(self, file_name: str) -> None:
        with open(file_name, 'r') as file:
            text = file.read()

            for i in range(0, len(text.split('\n'))):
                line = text.split('\n')[i]
                line = line.replace(" ", "").strip()
                if line == "":
                    break

                if line[0] == "Q":
                    line = line[line.find("=") + 1:]
                    self.Q = line.split(",")

                if line[0] == "E":
                    line = line[line.find("=") + 1:]
                    self.E = line.split(",")

                if line[0] == "S":
                    line = line[line.find("=") + 1:].split(";")
                    for group in line:
                        group = group.split(",")
                        self.S.add(group[0], group[1], group[2])

                if line[0:2] == "q0":
                    self.q0 = line[line.find("=") + 1:].strip()

                if line[0] == "F":
                    line = line[line.find("=") + 1:]
                    self.F = line.split(",")

    def testFA(self, sequence: list):
        state = self.q0

        for op in sequence:
            result = self.S.getResult(op, state)

            if result == None:
                return False

            state = result

        if state in self.F:
            return state
        return False


def menu():
    print("1.\tread FA file\n2.\ttest sequence\n3.\tprint FA\n\ncommand: ", end="")

    cmd = input()
    if cmd == "1":
        print("give file name: ", end="")
        file_name = input()
        fa.scan(file_name)

    elif cmd == "2":
        print("give sequence (in list of int format): ", end="")
        seq = input()
        seq = list(map(str, seq.replace(
            "[", "").replace(" ", "").replace("]", "").split(",")))
        print(seq)

        result = fa.testFA(seq)

        if result != False:
            print("valid sequence with final state:", result)
        else:
            print("invalid sequence")

    elif cmd == "3":
        print(str(fa))

    else:
        print("invalid command!")

    print()


fa = FA()
while True:
    menu()
