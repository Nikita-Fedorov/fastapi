"""Initial migration

Revision ID: 867c0eed46e8
Revises: 03ba13dac1d1
Create Date: 2023-11-09 02:00:18.391633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '867c0eed46e8'
down_revision: Union[str, None] = '03ba13dac1d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
