from __future__ import annotations

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_add_not_null_column_runsql_default_before_not_null", "0001_initial")
    ]

    operations = [
        migrations.RunSQL(
            sql="ALTER TABLE app_add_not_null_column_runsql_default_before_not_null_a ADD COLUMN not_null_field INTEGER DEFAULT 0 NOT NULL;",
            reverse_sql="ALTER TABLE app_add_not_null_column_runsql_default_before_not_null_a DROP COLUMN not_null_field;",
            state_operations=[
                migrations.AddField(
                    model_name="a",
                    name="not_null_field",
                    field=models.IntegerField(default=0),
                )
            ],
        )
    ]
