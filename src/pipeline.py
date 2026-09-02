"""
Main data pipeline.

This file runs the full pipeline:

1. Ingest new CSV files into the raw schema.
2. Run transformation stored procedures to refresh the harmonized schema.
"""

import logging

from sqlalchemy.exc import SQLAlchemyError

from ingest_files import ingest_new_files
from run_transformations import run_transformations


# ============================================================
# Logging configuration
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)