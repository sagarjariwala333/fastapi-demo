"""Add employee and task models

Revision ID: 8f5ec5a9d5c8
Revises: 
Create Date: 2024-07-16 15:52:48.885797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f5ec5a9d5c8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movies_id'), 'movies', ['id'], unique=False)
    op.create_index(op.f('ix_movies_name'), 'movies', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_movies_name'), table_name='movies')
    op.drop_index(op.f('ix_movies_id'), table_name='movies')
    op.drop_table('movies')
    # ### end Alembic commands ###