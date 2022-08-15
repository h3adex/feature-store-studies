# This is an example feature definition file

from datetime import timedelta

from feast import Entity, Feature, FeatureView, ValueType, FileSource

batch_source = FileSource(
    name="student_batch_source",
    path="/home/mauritz/PycharmProjects/feast-example/data/credits.parquet",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp",
)

student = Entity(
    name="student",
    value_type=ValueType.INT64
)

customer_events = FeatureView(
    name="student_credits",
    entities=["student"],
    ttl=timedelta(days=1),
    features=[
        Feature(name="credits", dtype=ValueType.INT64),
    ],
    online=True,
    source=batch_source,
    tags={},
)