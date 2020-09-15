from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says I am both a knight and a knave.
knowledge0 = And(Or(AKnight, AKnave))
knowledge = And(AKnave, AKnight)
if model_check(knowledge0, knowledge):
     knowledge0 = And(AKnight)
else:
     knowledge0 = And(AKnave)


knowledge0.add(Not(BKnave))
knowledge0.add(Not(BKnight))
knowledge0.add(Not(CKnave))
knowledge0.add(Not(CKnight))


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
        Or(AKnave, AKnight),
        Or(BKnave, BKnight)
)
knowledge1 = And(AKnave, BKnave)
knowledge.add(Not(knowledge1))
if model_check(knowledge, knowledge1) == False:
    knowledge1 = And(AKnave, BKnight)


knowledge1.add(Not(CKnave))
knowledge1.add(Not(CKnight))

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
        Or(AKnave, AKnight),
        Or(BKnave, BKnight)
)
knowledgeA = And(Or(And(AKnave, BKnave), And(AKnight, BKnight)))
knowledgeB = And(Or(And(AKnave, BKnight), And(AKnight, BKnave)))
if model_check(knowledgeA, knowledgeB):
    knowledge2 = And(AKnight, BKnight)
else:
    knowledge2 = And(AKnave, BKnight)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
        Or(AKnave, AKnight),
        Or(BKnave, BKnight),
        Or(CKnave, CKnight),
)
knowledgeA = And(Or(AKnight, AKnave))
if model_check(knowledge3, knowledgeA):
     knowledge3 = And(AKnight)
else:
    knowledge3 = And(AKnave)

if model_check(knowledge3, AKnight):
    knowledge3 = And(AKnight, CKnight)
else:
    knowledge3 = And(AKnave, CKnave)

knowledgeB = And(AKnave, CKnave)
if model_check(knowledge3, knowledgeB):
    knowledge3 = And(AKnave, BKnight, CKnave)
else:
    knowledge3 = And(AKnight, BKnave, CKnight)


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
