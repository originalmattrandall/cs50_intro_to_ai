from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a knight or a knave
    Or(AKnight, AKnave),

    # it cannot be both
    Not(And(AKnight, AKnave)),

    # A is a knight if and only if it is a knight and a knave
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is either a knight or a knave
    Or(AKnight, AKnave),

    # A and B cannot be both
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # A is a knight if and only if A and B are both knaves
    Biconditional(AKnight, And(AKnave, BKnave)),

    # B is a knight if A is a knave
    Implication(AKnave, BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A and B are both either a Knight or a Knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),

    # A and B cannot be both
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # A states we are the same
    # It can only be a knight if and only if A and B are both Knights or they are both Knaves
    Biconditional(AKnight, Or(And(AKnight, BKnight),
                              And(AKnave, BKnave))),

    # B states they are different
    # We can assume now that if A is a knight then B will be a Knave. otherwise B is a Knight.
    Implication(AKnight, BKnave)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A, B and C are both either a Knight or a Knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    # A, B and C cannot be both
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    Implication(AKnave, And(BKnight, CKnave)),

    Biconditional(BKnight, Biconditional(AKnight, AKnave)),

    Implication(CKnave, And(AKnave, BKnight)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
