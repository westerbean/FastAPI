"""add content column to posts table

Revision ID: 19460af37abd
Revises: ee13641c126a
Create Date: 2025-01-14 11:51:22.459394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19460af37abd'
down_revision: Union[str, None] = 'ee13641c126a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
