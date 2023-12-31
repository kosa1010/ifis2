from simpful import *
from ifis.interval_fuzzy_sets import *
from ifis.interval_fuzzy_system import *
from ifis.interval_linguistic_variable import *

# A simple interval fuzzy inference system for the tipping problem
# Create interval fuzzy system object
iFS = IntervalFuzzySystem()

# Define interval fuzzy sets and interval linguistic variables
S_1 = IntervalFuzzySet(function_start=Triangular_MF(a=0, b=0, c=5), function_end=Trapezoidal_MF(a=1, b=1, c=1, d=6),
                       term='poor')
S_2 = IntervalFuzzySet(function_start=Triangular_MF(a=0, b=5, c=10), function_end=Trapezoidal_MF(a=0, b=4, c=6, d=10),
                       term='good')
S_3 = IntervalFuzzySet(function_start=Trapezoidal_MF(a=4, b=9, c=10, d=10), function_end=Triangular_MF(a=5, b=10, c=10),
                       term='excellent')
# iFS.add_linguistic_variable("Service", IntervalLinguisticVariable([S_1, S_2, S_3], concept="Service quality", universe_of_discourse=[0, 10]))
iLV_1 = IntervalLinguisticVariable([S_1, S_2, S_3], concept="Service quality", universe_of_discourse=[0, 10])
# iLV_1.plot()
iFS.add_linguistic_variable("Service", iLV_1)

F_1 = IntervalFuzzySet(function_start=Triangular_MF(a=0, b=0, c=8), function_end=Trapezoidal_MF(a=1, b=1, c=2, d=10),
                       term='rancid')
F_2 = IntervalFuzzySet(function_start=Trapezoidal_MF(a=0, b=8, c=10, d=10), function_end=Triangular_MF(a=2, b=10, c=10),
                       term='delicious')
# iFS.add_linguistic_variable("Food", IntervalLinguisticVariable([F_1, F_2], concept="Food quality", universe_of_discourse=[0, 10]))
iLV_2 = IntervalLinguisticVariable([F_1, F_2], concept="Food quality", universe_of_discourse=[0, 10])
# iLV_2.plot()
iFS.add_linguistic_variable("Food", iLV_2)

# Define output crisp values
iFS.set_crisp_output_value("small", 5)
iFS.set_crisp_output_value("average", 15)

# Define function for generous tip (food score + service score + 5%)
iFS.set_output_function("generous", "Food+Service+5")

# Define fuzzy rules
R1 = "IF (Service IS poor) OR (Food IS rancid) THEN (Tip IS small)"
R2 = "IF (Service IS good) THEN (Tip IS average)"
R3 = "IF (Service IS excellent) OR (Food IS delicious) THEN (Tip IS generous)"
iFS.add_rules([R1, R2, R3])

# Set antecedents values
iFS.set_variable("Service", 4)
iFS.set_variable("Food", 8)

# Perform Sugeno interval inference and print output
print(iFS.Sugeno_interval_inference(["Tip"]))
