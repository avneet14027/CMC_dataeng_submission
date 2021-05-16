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
'''
Solution 2.1 
First, concatenate the dataframes along the first axis, 
so that we have all the equipments along with their corresposing measurements on the various days.
Then the index was set using "equipment_name","sample_day","sample_month" to allow indexing using 
a multiindex 
Lastly, measurement was computed by selecting the relevant rows,cols indexed by the 3 columns
as mentioned above. 
'''
equipment_measurements = pd.concat([equipments,measurements],axis=1)
equipment_measurements['equipment_name'] = [('EQ'+ str(i)) for i in range(0,10)]
equipment_measurements = (equipment_measurements.set_index(['equipment_name',"sample_day","sample_month"]))

keys = ("EQ2", "18", "12")
compound = "meglitinides"
meglitinides_measurement = equipment_measurements.loc[keys, compound]  # float
print(meglitinides_measurement)

# exercise 2.2 Get the average runtime per month for the
# equipments that measured quantities of sulfonylureas
# and of biguanide that are greater than meglitinides_measurement
avg_monthly_runtime = None  # dataframe

# your solution here
