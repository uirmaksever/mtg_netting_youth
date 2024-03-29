# Generated by Django 2.2.3 on 2019-07-29 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netting_youth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='problem',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='problem',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
