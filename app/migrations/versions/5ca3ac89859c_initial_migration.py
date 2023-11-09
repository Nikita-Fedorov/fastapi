"""Initial migration

Revision ID: 5ca3ac89859c
Revises: d1d22dbc8856
Create Date: 2023-11-09 02:21:23.814190

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ca3ac89859c'
down_revision: Union[str, None] = 'd1d22dbc8856'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
