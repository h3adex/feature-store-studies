import random
from typing import List

import pandas as pd
from datetime import datetime, timedelta
from pandas import DataFrame

retrieval_date: datetime = datetime.utcnow().replace(tzinfo=None)
retrieval_outside_max_age_date: datetime = retrieval_date + timedelta(1)
event_date: datetime = retrieval_date - timedelta(2)
creation_date: datetime = retrieval_date - timedelta(1)

base_student: int = 822594
students: List[int] = [base_student + x for x in range(100)]
semester: List[int] = []
farmed_credits: List[int] = []
is_done: List[bool] = []

for x in students:
    if (x % 3) == 0:
        semester.append(random.randint(5, 9))
    else:
        semester.append(random.randint(1, 5))

for k, v in enumerate(semester):
    if v > 5:
        farmed_credits.append(random.randint(70, 120))
    else:
        farmed_credits.append(random.randint(0, 70))

for k, v in enumerate(semester):
    if v >= 6 and farmed_credits[k] >= 90:
        is_done.append(True)
    else:
        is_done.append(False)

semester_df: DataFrame = pd.DataFrame(
    {
        "event_timestamp": [event_date for _ in students],
        "created_timestamp": [creation_date for _ in students],
        "student": students,
        "semester": semester,
        "is_done": is_done
    }
)

credits_df: DataFrame = pd.DataFrame(
    {
        "event_timestamp": [event_date for _ in students],
        "created_timestamp": [creation_date for _ in students],
        "student": students,
        "credits": farmed_credits,
    }
)

students_df: DataFrame = pd.DataFrame(
    {
        "event_timestamp": [retrieval_date - timedelta(1) for _ in students] +
                           [retrieval_outside_max_age_date for _ in students],
        "student": students + students,
    }
)

semester_df.to_parquet("data/semester.parquet")
students_df.to_parquet("data/students.parquet")
credits_df.to_parquet("data/credits.parquet")
