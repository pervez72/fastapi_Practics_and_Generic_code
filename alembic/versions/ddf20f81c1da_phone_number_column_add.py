"""phone number column add 

Revision ID: ddf20f81c1da
Revises: 
Create Date: 2026-03-14 18:57:13.563695

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ddf20f81c1da'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number', sa.String(), nullable=True)
)


def downgrade() -> None:
    """Downgrade schema."""
    pass
