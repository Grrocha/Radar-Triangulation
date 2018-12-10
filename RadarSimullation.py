import numpy as np
import math
from scipy.optimize import fsolve
import matplotlib
import matplotlib.pyplot as plt
import sympy
from sympy.solvers import solve
from sympy import *
import pandas as pd

GenData = pd.DataFrame(columns = ["Response1", "Response2", "Response3", "FoundLocation"])

print(GenData)

X, Y = symbols('x y')
Radar1 = {"PositionX": 0, "PositionY": 0, "ResponseTime": 0, "Distance": 0}
Radar2 = {"PositionX": 0, "PositionY": 0, "ResponseTime": 0, "Distance": 0}
Radar3 = {"PositionX": 0, "PositionY": 0, "ResponseTime": 0, "Distance": 0}
Emissor = {"PositionX": 0, "PositionY": 0}
MapRange = 10
Emissor["PositionX"] = np.random.random()*MapRange
Emissor["PositionY"] = np.random.random()*MapRange
Radar1["PositionX"] = np.random.random()*MapRange
Radar1["PositionY"] = np.random.random()*MapRange
Radar2["PositionX"] = np.random.random()*MapRange
Radar2["PositionY"] = np.random.random()*MapRange
Radar3["PositionX"] = np.random.random()*MapRange
Radar3["PositionY"] = np.random.random()*MapRange
T = 1
Z = 1
x0 = np.array([0.1,0.1])
def SetResponseTime(Radar, Emissor):
	ResponseTime = (np.sqrt(math.pow((Radar["PositionX"] - Emissor["PositionX"]), 2) + math.pow((Radar["PositionY"] - Emissor["PositionY"]), 2)))/299792458
	Radar["ResponseTime"] = ResponseTime
	print("Response Time: " + str(ResponseTime) + " Seconds")
	return ResponseTime
def GetDistance(Radar):
	Distance = Radar["ResponseTime"]*299792458
	print("Distance: " + str(Distance) + " Meters")
	Radar["Distance"] = Distance

def GetLocation(Radar1,Radar2,Radar3):
	Posit1x = Radar1["PositionX"]
	Posit2x = Radar2["PositionX"]
	Posit3x = Radar3["PositionX"]
	Posit1y = Radar1["PositionY"]
	Posit2y = Radar2["PositionY"]
	Posit3y = Radar3["PositionY"]
	Radius1 = Radar1["Distance"]
	Radius2 = Radar2["Distance"]**2
	Radius3 = Radar3["Distance"]
	y = solve([sympy.sqrt((Posit1x - X)**2 + (Posit1y - Y)**2) - Radius1, ((Posit2x - X)**2 + (Posit2y - Y)**2) - Radius2], [X, Y])
	ReturnedValue01 = y[0][0]
	ReturnedValue02 = y[0][1]
	ReturnedValue03 = y[1][0]
	ReturnedValue04 = y[1][1]
	result = (Posit3x - ReturnedValue01)*(Posit3x - ReturnedValue01) + (Posit3y - ReturnedValue02)*(Posit3y - ReturnedValue02) - Radius3*Radius3
	print(str(math.ceil(result)) + " For " + str(y[0]))
	result2 = (Posit3x - ReturnedValue03)*(Posit3x - ReturnedValue03) + (Posit3y - ReturnedValue04)*(Posit3y - ReturnedValue04) - Radius3*Radius3
	print(str(math.ceil(result2)) + " For " + str(y[1]))
	if math.ceil(result) == 0 or math.floor(result) == 0:
		print("Emitter Position: " + str(y[0]))
		plt.plot([y[0][0]],[y[0][1]], 'bo')
	else:
		print("Emitter Position: " + str(y[1]))
		plt.plot([y[1][0]],[y[1][1]], 'bo')
	print(y)

SetResponseTime(Radar1, Emissor)
GetDistance(Radar1)
SetResponseTime(Radar2, Emissor)
GetDistance(Radar2)
SetResponseTime(Radar3, Emissor)
GetDistance(Radar3)
GetLocation(Radar1,Radar2,Radar3)

c1 = plt.Circle((Radar1["PositionX"],Radar1["PositionY"]), Radar1["Distance"], color='b', fill=False)
c2 = plt.Circle((Radar2["PositionX"],Radar2["PositionY"]), Radar2["Distance"], color='b', fill=False)
c3 = plt.Circle((Radar3["PositionX"],Radar3["PositionY"]), Radar3["Distance"], color='b', fill=False)
ax = plt.gca()
ax.add_artist(c1)
ax.add_artist(c2)
ax.add_artist(c3)
plt.plot([Radar1["PositionX"]],[Radar1["PositionY"]], 'ro')
plt.plot([Radar2["PositionX"]],[Radar2["PositionY"]], 'ro')
plt.plot([Radar3["PositionX"]],[Radar3["PositionY"]], 'ro')
plt.show()