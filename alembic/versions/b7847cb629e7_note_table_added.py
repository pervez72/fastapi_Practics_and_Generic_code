"""note table added 

Revision ID: b7847cb629e7
Revises: ddf20f81c1da
Create Date: 2026-03-14 19:41:33.902280

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7847cb629e7'
down_revision: Union[str, Sequence[str], None] = 'ddf20f81c1da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "note",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String()),
        sa.Column("description", sa.String()),
        sa.Column("owner_id", sa.Integer(), sa.ForeignKey("users.id"))
    )
def downgrade() -> None:
    """Downgrade schema."""
    pass
