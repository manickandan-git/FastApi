"""create content column posts table

Revision ID: 4834f34b77e9
Revises: 7706fe996176
Create Date: 2026-02-12 21:33:49.592687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4834f34b77e9'
down_revision: Union[str, Sequence[str], None] = '7706fe996176'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))   
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')  
    pass

