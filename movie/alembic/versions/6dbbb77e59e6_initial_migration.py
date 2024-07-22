"""Initial migration

Revision ID: 6dbbb77e59e6
Revises: 4d74fa6d0b4c
Create Date: 2024-07-16 23:19:55.007371

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6dbbb77e59e6'
down_revision: Union[str, None] = '4d74fa6d0b4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'employee_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('employee_id', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###