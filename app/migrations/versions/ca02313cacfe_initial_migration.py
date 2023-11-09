"""Initial migration

Revision ID: ca02313cacfe
Revises: 7ddd4926c183
Create Date: 2023-11-09 02:24:20.430267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca02313cacfe'
down_revision: Union[str, None] = '7ddd4926c183'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
