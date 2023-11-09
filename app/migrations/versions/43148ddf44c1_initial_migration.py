"""Initial migration

Revision ID: 43148ddf44c1
Revises: 6c866899ba2c
Create Date: 2023-11-09 02:44:35.752708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43148ddf44c1'
down_revision: Union[str, None] = '6c866899ba2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rooms', sa.Column('services', sa.JSON(), nullable=True))
    op.add_column('rooms', sa.Column('image_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rooms', 'image_id')
    op.drop_column('rooms', 'services')
    # ### end Alembic commands ###
