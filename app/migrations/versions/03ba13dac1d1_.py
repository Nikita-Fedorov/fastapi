"""empty message

Revision ID: 03ba13dac1d1
Revises: 32d5227bfa03, 52098f869748
Create Date: 2023-11-09 01:59:30.566502

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03ba13dac1d1'
down_revision: Union[str, None] = ('32d5227bfa03', '52098f869748')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
