"""Create account table

Revision ID: e9f1bed1a9cf
Revises: 
Create Date: 2022-12-08 15:21:00.862254

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'e9f1bed1a9cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, autoincrement=True, unique=True, primary_key=True),
        sa.Column("first_name", sa.String, primary_key=True),
        sa.Column("second_name", sa.String, primary_key=True),
        sa.Column("age", sa.Integer),
        sa.Column("created_time", sa.DateTime, default=datetime.datetime.utcnow),
        sa.Column("hashed_password", sa.String, unique=True, primary_key=True),
    )


def downgrade() -> None:
    op.drop_table("users")
