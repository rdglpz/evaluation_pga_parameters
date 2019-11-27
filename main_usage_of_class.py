
path_a = "/home/rodrigo"
path_b = "/home/rodrigo/git/pga_parameter_evaluation"

import sys

sys.path.append(path_b)

import objectiveFunctionClass as of

#compactness mean
cm = 0.1 

#compactness_range
cr = 0.05 

#discount factor
df = 0.1 

X = [cm,cr,df]

c = of.evaluateFuturesParams()
r = c.f(X)