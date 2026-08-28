from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyDiagnosticSearch(problem: SearchProblem):
    """
    Returns a hard-coded sequence of moves for the tinyDiagnostic layout.
    For any other station layout, the sequence of moves will be incorrect.
    """
    s = Directions.SOUTH
    e = Directions.EAST
    return [s, e, s, e, e, e, e, s, e, e, s, s, e, s, s, e, s, e, e, e, e, e, e, e]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # TODO: Add your code here DONE
    
    #crear pila para manejar los nodos a visitar, cnjunto para nodos visitados
    stack = utils.Stack()
    visited = set()
    
    #obtener estado inicial del problema 
    pos = problem.getStartState()
    stack.push((pos,[]))
    
    while not stack.isEmpty(): 
       state, path= stack.pop()
       
       #verificar si estado ya fue visitado
       if state not in visited: 
           visited.add(state)
           
           #verificar si estado actual es la meta
           if problem.isGoalState(state):
               return path
           
           #pedir estados sucesores
           succesors = problem.getSuccessors(state)
           for succesor in succesors:
                next_state, action , _ = succesor
                
                #verificar si estados ya han sido visitados
                if next_state not in visited:
                    new_path = path + [action]
                    stack.push((next_state, new_path))
    #si no se encontro ningun camino, retornar una lista sin acciones 
    return []



def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # TODO: Add your code here
    
    #Iniciar cola  y conjkunto para nodos viistados
    queue = utils.Queue()
    visited = set()
    
    #estado inicial robot
    pos = problem.getStartState()
    queue.push((pos,[] ))
    visited.add(pos)
    
    while not queue.isEmpty():
        state, path = queue.pop()
        
        #verificar si estado es la meta
        if problem.isGoalState(state):
            return path
            
        #si no, pedir estados sucesores
        successors = problem.getSuccessors(state)
            
        #procesar estaos siguientes
        for successor in successors:
            next_state, action, _ = successor
                
            #verificar si estados ya fuyeron visitados
            if next_state not in visited:
                visited.add(next_state)
                new_path = path + [action]
                queue.push((next_state, new_path))
                    
    #camino vacio si no encontro nada 
    return []


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
