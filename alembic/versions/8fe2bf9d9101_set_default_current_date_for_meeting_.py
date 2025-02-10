"""Set default current date for meeting date

Revision ID: 8fe2bf9d9101
Revises: ef4c2b37f8be
Create Date: 2025-02-10 17:00:06.765040

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = '8fe2bf9d9101'
down_revision: Union[str, None] = 'ef4c2b37f8be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Alter the 'date' column to set the default value to CURRENT_TIMESTAMP
    op.alter_column(
        'meetings', 
        'date',
        type_=sa.DateTime(),  # Ensuring the type remains DATETIME
        server_default=sa.text('CURRENT_TIMESTAMP'),
        existing_type=sa.DateTime(),  # Existing column type is DATETIME
    )


def downgrade():
    # Remove the default value for the 'date' column if downgrading
    op.alter_column(
        'meetings', 
        'date',
        server_default=None,
        existing_type=sa.DateTime(),  # Existing column type is DATETIME
    )
