"""Initial migration

Revision ID: d1d22dbc8856
Revises: 867c0eed46e8
Create Date: 2023-11-09 02:18:21.422772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1d22dbc8856'
down_revision: Union[str, None] = '867c0eed46e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
