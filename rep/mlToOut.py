def mlToOut(mlOut):
    """takes the output of our ml and turns it into a final stances
    :param mlOut: a list<pair<source, stance>>
    """
    opinions = list<opinion>
    for ml in mlOut:
        opinions.add(opinion(ml.source, ml.stance))
    return avgStance(opinions)

class opinion:
    def __init__(self, source, stance):
        self.source = source
        self.stance = stance

def avgStance(opinions):
    """takes a list of opinions and calculates the final stance
    :param opinions: a list<opinion> of all opinions to average
    """
    finalStance #to hold our final stance
    for op in opinions
        #disagree
        if op.stance == 0:
            finalOpinion -= calcRep(op.source)
        #agree
        if op.stance == 1:
            finalOpinion += calcRep(op.source)
        #unrelated
        if op.stance == 2:
            #do nothing
        #discuss
        if op.stance == 3:
            finalOpinion += calcRep(op.source)/4
    return finalStance/opinions.size


def calcRep(source):
