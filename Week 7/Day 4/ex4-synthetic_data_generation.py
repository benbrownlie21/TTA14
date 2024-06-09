import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()

# Use the Python Faker library to generate a list of 100 random names, addresses, and email addresses.
data = [(fake.name(), fake.address(), fake.email()) for _ in range(100)]

df_1 = pd.DataFrame(data, columns=["Name", "Address", "Email"])

# Use numpy to add a column of random ages (between 20 and 60) and a column of random income levels (within a reasonable range).
data_2 = [
    (np.random.randint(20, 60), np.random.randint(18000, 75000)) for _ in range(100)
]

# Combine this data into a pandas DataFrame and name the columns appropriately.
df_2 = pd.DataFrame(data_2, columns=["Random Ages", "Random Income Levels"])

df_all = pd.concat([df_1, df_2], axis=1)

# Display the first 10 rows of your DataFrame.
print(df_all.head(10))
