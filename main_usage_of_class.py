
path_a = "/home/rodrigo"
path_b = "/home/rodrigo/git/pga_parameter_evaluation"
import sys

sys.path.append(path_b)

import objectiveFunctionClass as of

X = [0.1,0.05,0.1]


c = of.evaluateFuturesParams()
r = c.f(X)