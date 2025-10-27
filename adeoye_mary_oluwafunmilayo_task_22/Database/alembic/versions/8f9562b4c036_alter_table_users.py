"""alter table users

Revision ID: 8f9562b4c036
Revises: 
Create Date: 2025-10-23 04:07:18.551147

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f9562b4c036'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
               ALTER TABLE users
               ADD COLMN userType varchar(100)
               """)
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.execute("""
               ALTER TABLE users
               DROP COLUMN userType

    """)
    pass
