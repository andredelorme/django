# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("migrations", "thefirst"),
        ("migrations2", "0002_second"),
    ]

    operations = [

        migrations.DeleteModel("Tribble"),

        migrations.RemoveField("Author", "silly_field"),

        migrations.AddField("Author", "rating", models.IntegerField(default=0)),

        migrations.CreateModel(
            "Book",
            [
                ("id", models.AutoField(primary_key=True)),
                ("author", models.ForeignKey("migrations.Author", null=True)),
            ],
        )

    ]
