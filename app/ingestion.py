from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    Boolean,
    Float
)

engine = create_engine(
    "sqlite:///store.db",
    connect_args={"check_same_thread": False}
)

db_metadata = MetaData()

events = Table(
    "events",
    db_metadata,

    Column("event_id", String, primary_key=True),
    Column("store_id", String),
    Column("camera_id", String),
    Column("visitor_id", String),
    Column("event_type", String),
    Column("timestamp", String),
    Column("zone_id", String),
    Column("dwell_ms", Integer),
    Column("is_staff", Boolean),
    Column("confidence", Float),
    Column("event_metadata", String)
)

db_metadata.create_all(engine)

print("Database and events table created successfully.")