"""--------------1-------------------"""
from sqlalchemy import create_engine

# The Engine is the starting point for any SQLAlchemy application
# It's a "home base" for the actual database connections
engine = create_engine("sqlite:///bird_ringing.db")

"""--------------2-------------------"""
# Connection String Examples:
# PostgreSQL: postgresql+psycopg2://scott:tiger@localhost/mydatabase
# SQLite (Relative path): sqlite:///field_data.db

from sqlalchemy import create_engine

engine = create_engine("sqlite:///field_data.db")

# Establish a connection
with engine.connect() as connection:
    print("Connection established successfully.")

"""--------------3-------------------"""
from sqlalchemy import text

query_str = "SELECT species, wing_length FROM captures WHERE wing_length > 70"

with engine.connect() as conn:
  # Execute raw SQL
  result = conn.execute(text(query_str))

  for row in result:
    # Access by column name
    print(f"Species: {row.species}, Wing: {row.wing_length}")

"""--------------4-------------------"""
# DANGEROUS - DO NOT DO THIS:
# sql = f"SELECT * FROM birds WHERE ring = '{user_input}'"

# SECURE Approach:
search_ring = "AX-9921'; DROP TABLE birds; --" # Malicious input

query = text("SELECT * FROM birds WHERE ring_number = :ring")

with engine.connect() as conn:
    # Pass parameters as a dictionary
    result = conn.execute(query, {"ring": search_ring})
    # The DB treats the input strictly as a value, not executable code.

"""--------------5-------------------"""
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
  pass


class Bird(Base):
  __tablename__ = "bird_inventory"

  id: Mapped[int] = mapped_column(primary_key=True)
  species: Mapped[str]
  weight: Mapped[float]


# Usage
with Session(engine) as session:
  # Create object instead of writing INSERT SQL
  new_bird = Bird(species="Blackbird", weight=95.2)
  session.add(new_bird)
  session.commit()  # Saves to DB

"""--------------6-------------------"""
# Lab Starter Hint
from sqlalchemy import create_engine, text

# Connect to the provided lab database
engine = create_engine("sqlite:///lab_data.db")

# Test connection
with engine.connect() as conn:
    print("Database reachable.")

