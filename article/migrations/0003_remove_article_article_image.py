

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20180327_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_image',
        ),
    ]