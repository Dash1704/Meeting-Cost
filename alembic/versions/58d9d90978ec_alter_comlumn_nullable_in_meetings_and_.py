"""Alter comlumn nullable in meetings and employees

Revision ID: 58d9d90978ec
Revises: 5e8f1717065b
Create Date: 2025-02-11 13:34:45.041060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '58d9d90978ec'
down_revision: Union[str, None] = '5e8f1717065b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('meetings', 'title', existing_type=sa.String(length=255), nullable=False)

    op.alter_column('employees', 'first_name', type_=sa.String(50), existing_type=sa.String(255), nullable=False) 
    op.alter_column('employees', 'last_name', type_=sa.String(50), existing_type=sa.String(255), nullable=False)  
    op.alter_column('employees', 'salary', existing_type=sa.Integer, nullable=False) 
    op.alter_column('employees', 'weekly_hours', existing_type=sa.Integer, nullable=False)


def downgrade() -> None:
    op.alter_column('meetings', 'title', existing_type=sa.String(length=255), nullable=True)

    op.alter_column('employees', 'first_name', type_=sa.String(255), existing_type=sa.String(50), nullable=True)  
    op.alter_column('employees', 'last_name', type_=sa.String(255), existing_type=sa.String(50), nullable=True)  
    op.alter_column('employees', 'salary', existing_type=sa.Integer, nullable=True)
    op.alter_column('employees', 'weekly_hours', existing_type=sa.Integer, nullable=True) 