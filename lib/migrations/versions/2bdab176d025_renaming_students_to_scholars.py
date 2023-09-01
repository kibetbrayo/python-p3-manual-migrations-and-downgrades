"""Renaming students to scholars

Revision ID: 2bdab176d025
Revises: 791279dd0760
Create Date: 2023-09-01 18:02:23.417666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bdab176d025'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
     op.rename_table('scholars', 'students')
