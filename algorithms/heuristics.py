from typing import Tuple
from algorithms import utils
from algorithms.problems import SystemRepairProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.

    Baseline rule for this workshop: estimate the direct distance to the next
    mandatory target:
    - K if the robot does not have the kit yet.
    - the nearest pending T if the robot has the kit and systems remain.
    - C if all systems have been repaired.
    """
    # TODO: Add your code here
    posicion, tieneKit, sitiosParaResolver = state
    
    if not tieneKit:
        return calcDistanciaManjatan(posicion,problem.kitPosition)
    if not len(sitiosParaResolver) == 0:
        distanciaMin = 9999999
        for sitioParaResolver in sitiosParaResolver:
            distancia = calcDistanciaManjatan(sitioParaResolver,posicion)
            if distancia < distanciaMin:
                distanciaMin = distancia
        return distanciaMin
    return calcDistanciaManjatan(posicion,problem.controlPosition)
    
def calcDistanciaManjatan(punto1,punto2):
    return abs(punto1[0]-punto2[0]) + abs(punto1[1]-punto2[1])

def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.

    Baseline rule for this workshop: estimate the direct distance to the next
    mandatory target:
    - K if the robot does not have the kit yet.
    - the nearest pending T if the robot has the kit and systems remain.
    - C if all systems have been repaired.
    """
    # TODO: Add your code here

    posicion, tieneKit, sitiosParaResolver = state
    
    if not tieneKit:
        return calcDistanciaEuclid(posicion,problem.kitPosition)
    if not len(sitiosParaResolver) == 0:
        distanciaMin = 9999999
        for sitioParaResolver in sitiosParaResolver:
            distancia = calcDistanciaEuclid(sitioParaResolver,posicion)
            if distancia < distanciaMin:
                distanciaMin = distancia
        return distanciaMin
    return calcDistanciaEuclid(posicion,problem.controlPosition)

def calcDistanciaEuclid(punto1,punto2):
    return ((punto1[0]-punto2[0])**2 + (punto1[1]-punto2[1])**2)**(0.5)


def systemRepairHeuristic(
    state: Tuple[Tuple, bool, Tuple], problem: SystemRepairProblem
):
    """
    Your heuristic for the SystemRepairProblem.

    state: (position, hasKit, pendingSystems)
    problem: SystemRepairProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider the kit, pending systems, and the final return to control center
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    # TODO: Add your code here

    posicion, tieneKit, sitiosParaResolver = state
    
    if problem.heuristicInfo == {}:
        backState = [problem.kitPosition , True, list(sitiosParaResolver)]
        next = problem.kitPosition

        while next != problem.controlPosition:
            newNext = calcularSiguiente(backState, problem)
            if newNext in backState[2]:
                backState[2].remove(newNext)
            problem.heuristicInfo[next] = newNext
            next = newNext
    print(problem.heuristicInfo)

    totalDis = 0

    while posicion != problem.controlPosition:
        if posicion not in problem.heuristicInfo:
            newPosicion = calcularSiguiente(state,problem)
        else:
            newPosicion = problem.heuristicInfo[posicion]

        totalDis += calcDistanciaManjatan(posicion, newPosicion)
        posicion = newPosicion
    return totalDis
        


def calcularSiguiente(state, problem:SystemRepairProblem):
    posicion, tieneKit, sitiosParaResolver = state
    
    if not tieneKit:
        return problem.kitPosition
    if not len(sitiosParaResolver) == 0:
        nextSitio = None
        distanciaMin = 999999999999
        for sitioParaResolver in sitiosParaResolver:
            distancia = calcDistanciaManjatan(sitioParaResolver,posicion)
            if distancia > 0 and (nextSitio == None or distancia < distanciaMin):
                nextSitio = sitioParaResolver
                distanciaMin = distancia
        return nextSitio
    return problem.controlPosition

