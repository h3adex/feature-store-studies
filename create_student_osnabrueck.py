import random
from typing import List

import pandas as pd
from datetime import datetime, timedelta
from pandas import DataFrame
import names

retrieval_date: datetime = datetime.utcnow().replace(tzinfo=None)
retrieval_outside_max_age_date: datetime = retrieval_date + timedelta(1)
event_date: datetime = retrieval_date - timedelta(2)
creation_date: datetime = retrieval_date - timedelta(1)

base_registration_number: int = 825594
registration_numbers: List[int] = [base_registration_number + x for x in range(100)]
student_names: List[str] = [names.get_full_name() for _ in registration_numbers]
semester: List[int] = []
farmed_credits: List[int] = []
graduated: List[bool] = []

for x in registration_numbers:
    if (x % 2) == 0:
        semester.append(random.randint(5, 9))
    else:
        semester.append(random.randint(1, 5))

for k, v in enumerate(semester):
    if v > 5:
        farmed_credits.append(random.randint(170, 240))
    else:
        farmed_credits.append(random.randint(0, 170))

for k, v in enumerate(semester):
    if v >= 6 and farmed_credits[k] >= 180:
        graduated.append(True)
    else:
        graduated.append(False)

semester_df: DataFrame = pd.DataFrame(
    {
        "event_timestamp": [event_date for _ in registration_numbers],
        "created_timestamp": [creation_date for _ in registration_numbers],
        "registration_number": registration_numbers,
        "semester": semester,
        "graduated": graduated
    }
)

credits_df: DataFrame = pd.DataFrame(
    {
        "event_timestamp": [event_date for _ in registration_numbers],
        "created_timestamp": [creation_date for _ in registration_numbers],
        "registration_number": registration_numbers,
        "credits": farmed_credits,
    }
)

event_timestamps_1 = [retrieval_date - timedelta(1) for _ in registration_numbers]
event_timestamps_2 = [retrieval_outside_max_age_date for _ in registration_numbers]

students_df: DataFrame = pd.DataFrame(
    {
        "event_timestamp": event_timestamps_1 + event_timestamps_2,
        "registration_number": registration_numbers + registration_numbers,
        "student_name": student_names + student_names
    }
)

semester_df.to_parquet("data/semester.parquet")
students_df.to_parquet("data/students.parquet")
credits_df.to_parquet("data/credits.parquet")
