# pathlib is used to work with file and folder paths in a clean way.
# It is preferable to manually concatenating strings for paths.
from pathlib import Path

# datetime is used to register when files were loaded or processed.
from datetime import datetime

# Displays informational and error messages in the terminal.
import logging

# pandas is used to read CSV files and load them into PostgreSQL.
import pandas as pd

# text is used to safely execute SQL queries with parameters.
from sqlalchemy import text

# SQLAlchemyError is used to catch database-related errors.
from sqlalchemy.exc import SQLAlchemyError

# get_engine centralizes the database connection logic.
# The credentials are handled in src/db_connection.py using the .env file.
from db_connection import get_engine