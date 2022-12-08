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


class Sex:
    val: int

    def __str__(self):
        return 'male' if self.val else 'female'


class Passport:
    series: str
    number: str


class User:
    login: str
    password: str
    name: str
    secondName: str
    patronymic: str
    birthday: str
    sex: Sex
    phone: str
    snils: str
    passport: Passport


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("user", User, unique=True, primary_key=True)
    )


def downgrade() -> None:
    op.drop_table("users")
