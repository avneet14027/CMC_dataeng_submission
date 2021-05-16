import pandas as pd
import numpy as np
import random

compounds = [
    "biguanide",
    "thiazolidinedione",
    "sulfonylureas",
    "meglitinides",
    "vanadyl_sulfate",
]
sample_day_month = [
    ("31", "12"),
    ("27", "12"),
    ("18", "12"),
    ("6", "11"),
    ("1", "11"),
    ("31", "10"),
    ("27", "10"),
    ("18", "10"),
    ("6", "9"),
    ("1", "9"),
]
sample_day = [_[0] for _ in sample_day_month]
sample_month = [_[1] for _ in sample_day_month]
runtime = [random.random() for _ in range(len(sample_day_month))]
measurements = pd.DataFrame(np.random.randn(10, 5), columns=compounds).abs()
equipments = pd.DataFrame(
    {
        "sample_day": sample_day,
        "sample_month": sample_month,
        "runtime": runtime,
    }
)
equipments.index.name = "equipment_name"

# exercise 2.1 Get the random measurement of the equipment 2
# for meglitinides sampled the 18th of Decembre
equipment_measurements = None  # dataframe

# your solution here

keys = ("EQ2", "18", "12")
compound = "meglitinides"
meglitinides_measurement = equipment_measurements.loc[keys, compound]  # float

# exercise 2.2 Get the average runtime per month for the
# equipments that measured quantities of sulfonylureas
# and of biguanide that are greater than meglitinides_measurement
avg_monthly_runtime = None  # dataframe
'''
Solutionn 2.2
First, using the equipment_measurements dataframe, only those rows were selected
for which the measured quantities of sulfonylureas and biguanide were greater than 
the meglitinides_measurement computed before.
Then the resulting dataframe was grouped according to the sample month and the mean was 
computed using the agg function
'''
# your solution here
equipment_measurements_filtered = equipment_measurements[(equipment_measurements['biguanide']>meglitinides_measurement) & equipment_measurements['sulfonylureas']>meglitinides_measurement]
avg_monthly_runtime = equipment_measurements_filtered.groupby('sample_month').agg(['mean'])['runtime']
print(avg_monthly_runtime)
