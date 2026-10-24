"""create users and applications tables

Revision ID: fc35f6875253
Revises:
Create Date: 2026-10-24
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "fc35f6875253"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False, unique=True),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
    )
    op.create_index("ix_users_id", "users", ["id"], unique=False)

    op.create_table(
        "applications",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("company", sa.String(length=150), nullable=False),
        sa.Column("role", sa.String(length=150), nullable=False),
        sa.Column("status", sa.String(length=20), nullable=False),
        sa.Column("applied_date", sa.Date(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
    )
    op.create_index("ix_applications_id", "applications", ["id"], unique=False)

def downgrade() -> None:
    op.drop_index("ix_applications_id", table_name="applications")
    op.drop_table("applications")
    op.drop_index("ix_users_id", table_name="users")
    op.drop_table("users")
