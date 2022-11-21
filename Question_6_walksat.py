import random

def is_satisfied(clause, assignment):
   return any ( assignment [ symbol ] for symbol in clause )

def count_satisfied_clauses(symbol, unsatisfied_clauses, assignment):
    assignment[symbol] = not assignment[symbol]
    count = sum(is_satisfied(clause, assignment) for clause in unsatisfied_clauses)
    assignment[symbol] = not assignment[symbol]
    return count

def WalkSat ( clauses , p , max_flips ):
    symbols = set()
    for clause in clauses:
     symbols.update(clause)
    symbols = list(symbols)
    assignment = { symbol : random.choice ([ True , False ]) for symbol in symbols }
    for i in range ( max_flips ):         #1:100
        satisfied_clauses = [ clause for clause in clauses if is_satisfied ( clause , assignment )]     # defining satisfied clause
        if len ( satisfied_clauses ) == len ( clauses ):
            return assignment               #returning assignment if satisfied
        unsatisfied_clauses = [ clause for clause in clauses if not is_satisfied ( clause , assignment )]
        unsatisfied_clause = random.choice ( unsatisfied_clauses )
        if random.random () < p:
            symbol = random.choice(unsatisfied_clause)
        else :
            symbol = max(symbols , key = lambda symbol : count_satisfied_clauses(symbol, unsatisfied_clauses, assignment))
        assignment[symbol] = not assignment[symbol]
    return None                 #returning none if nonsatisfied assignment


def main():
    # Try 10 differnt inputs of random 3-CNF sentences with different clause/symbol ratio m/n to experience.
    for i in range(10):
        # Generate random 3-CNF sentences
        m = random.randint(1, 10)
        n = random.randint(1, 10)
        clauses = []
        for j in range(m):
            clause = []
            for k in range(3):
                clause.append(random.randint(1, n))     #adding values to clause 
            clauses.append(clause)                      #generating random clause
        print("\nClauses: ", clauses)
        assignment = WalkSat(clauses, 0.5, 100)            #calling Walksat
        if assignment is None:
            print("# No solution")
        else:
            print("Assignment: ", assignment)
            print("Satisfied clauses: ", [clause for clause in clauses if is_satisfied(clause, assignment)])



main()