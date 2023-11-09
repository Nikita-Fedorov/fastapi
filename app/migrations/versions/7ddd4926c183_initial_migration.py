"""Initial migration

Revision ID: 7ddd4926c183
Revises: 5ca3ac89859c
Create Date: 2023-11-09 02:23:12.584719

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ddd4926c183'
down_revision: Union[str, None] = '5ca3ac89859c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
