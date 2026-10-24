from logging.config import fileConfig
import os
from pathlib import Path

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool

# Ensure imports and .env work even if Alembic is launched outside backend/.
BACKEND_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BACKEND_DIR / ".env")
import sys
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from db.connection import Base  # noqa: E402
import models  # noqa: E402,F401 -- registers User and Application tables

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

url = os.getenv("DATABASE_URL")
if not url:
    raise RuntimeError(
        "DATABASE_URL is missing. Create backend/.env from backend/.env.example "
        "and add your MySQL connection URL."
    )
config.set_main_option("sqlalchemy.url", url.replace("%", "%%"))
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
