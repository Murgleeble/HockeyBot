"""
lineJudge uses the inferential functions to get a "complex" value calculation of player performance
"""
import inferential as inf


"""
Runs a 'value test' on a given player, statistic, over/under line
"""
def compareH(firstname, lastname, line, type, over):
    if type == 'G':
        val = inf.inferHockeyG(firstname, lastname, line, over)
        if val == False:
            return False
    elif type =='A':
        val = inf.inferHockeyA(firstname, lastname, line, over)
        if val == False:
            return False
    elif type == 'S':
        val = inf.inferHockeyS(firstname, lastname, line, over)
        if val == False:
            return False
    elif type == 'H':
        val = inf.inferHockeyH(firstname, lastname, line, over)
        if val == False:
            return False
    elif type == 'B':
        val = inf.inferHockeyB(firstname, lastname, line, over)
        if val == False:
            return False
    
    """ if val > .838:
        return val
        #return 5
    elif val > .791:
        return val
        #return 4
    elif val > .733:
        return val
        #return 3
    elif val > .657:
        return val
        #return 2
    elif val > .543:
        return val
        #return 1
    else:
        return val
        #return 0 """
    
    return val
