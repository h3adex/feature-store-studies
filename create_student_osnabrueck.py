from typing import List

import pandas as pd
from datetime import datetime, timedelta
import numpy as np
from pandas import DataFrame

retrieval_date: datetime = datetime.utcnow().replace(tzinfo=None)
retrieval_outside_max_age_date: datetime = retrieval_date + timedelta(1)
event_date: datetime = retrieval_date - timedelta(2)
creation_date: datetime = retrieval_date - timedelta(1)

base_student: int = 822594
students: List[int] = [base_student + x for x in range(100)]
semester: List[int] = [np.random.randint(1, 10) for _ in students]
is_done = []

for x in semester:
    is_done.append(True if x >= 6 else False)

semester_df: DataFrame = pd.DataFrame(
    {
        "event_timestamp": [event_date for _ in students],
        "created_timestamp": [creation_date for _ in students],
        "student": students,
        "semester": semester,
        "is_done": is_done
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
