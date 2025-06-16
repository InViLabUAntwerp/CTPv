from src.core_toolbox.Plucker.Line import Line
import numpy as np

if __name__ == '__main__':
    L = Line()
    L.Ps = np.array([[1, 1, 0]])
    L.Pe = np.array([[2, 1, 0], ])
    print(L.V)
    L.PlotLine()
    L2 = Line()
    L2.Ps = np.array([[0, 0, 0]])
    L2.Pe = np.array([[20, 20, 0], ])
    print(L2.V)
    hook, hookDegree = L.AngleBetweenLines(L, L2)
    print(hookDegree)
    print(hook)