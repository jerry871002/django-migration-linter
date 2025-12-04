from __future__ import annotations

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_add_not_null_column_runsql_not_null_before_default", "0001_initial")
    ]

    operations = [
        migrations.RunSQL(
            sql="ALTER TABLE app_add_not_null_column_runsql_not_null_before_default_a ADD COLUMN not_null_field INTEGER NOT NULL DEFAULT 0;",
            reverse_sql="ALTER TABLE app_add_not_null_column_runsql_not_null_before_default_a DROP COLUMN not_null_field;",
            state_operations=[
                migrations.AddField(
                    model_name="a",
                    name="not_null_field",
                    field=models.IntegerField(default=0),
                )
            ],
        )
    ]
