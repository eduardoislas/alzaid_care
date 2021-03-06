# Generated by Django 2.1.7 on 2019-05-03 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instruments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('valoracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumentanswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='instrumentanswer',
            name='valoration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valoration', to='valoracion.Valoracion'),
        ),
        migrations.AddField(
            model_name='answers',
            name='afirmation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instruments.Afirmation'),
        ),
        migrations.AddField(
            model_name='answers',
            name='instrument_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instruments.InstrumentAnswer'),
        ),
        migrations.AddField(
            model_name='answers',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instruments.Option'),
        ),
        migrations.AddField(
            model_name='afirmation',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instruments.Instrument'),
        ),
    ]
