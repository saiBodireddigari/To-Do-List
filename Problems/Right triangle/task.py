class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here

    def calculations(self):
        if (self.a ** 2) + (self.b ** 2) != self.c ** 2:
            print("Not right")
        else:
            print((self.a * self.b) / 2)


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

right = RightTriangle(input_c, input_a, input_b)

RightTriangle.calculations(right)