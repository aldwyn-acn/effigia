# Generated by Django 2.1.2 on 2018-10-05 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='from_addr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='message_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chat',
            name='to_addr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='message_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chats.Chat'),
        ),
    ]
