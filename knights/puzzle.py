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
    Or(AKnight, AKnave),  
    Not(And(AKnight, AKnave)),    #A can't be both 
    Implication(AKnight, AKnave),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, And(AKnave, BKnave)),   # if A is Knight, not possible bc statement can't be true
    Implication(AKnave, BKnight )       # if A is Knave, B  must be a Knight bc statement is false

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, BKnight),  # if A is Knight, statement must be true so B is Knight
    Implication(AKnave, BKnight),   # if A is Knave, statement must be false so B is a different kind: B is Knight
    Implication(BKnight, AKnave),   # if B is Knight, statement must be true so A is Knave 
    Implication(BKnave, AKnave)     # if B is Knave, statement must be false so A is same kind: A is Knave too
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    Implication(CKnight, AKnight),      # if C is Knight, statement is true so A is Knight
    Implication(CKnave, AKnave),        # if C is Knave, statement is false so A is Knave
    Implication(BKnight, And(CKnave, Implication(AKnight, AKnave), Implication(AKnave, AKnight))),
        # if B is Knight, statements are true, so C is Knave AND we know that is A said that, it is true if he is a 
        # Knight (does not make sense) but false if he is a Knave(also does not make sense)
    Implication(BKnave, CKnight),       # if B is Knave, statement is false so A did not say that and we can't conclude anything about A
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
