from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tag',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, '커피맛'), (2, '인테리어'), (3, '디저트'), (4, '감성'), (5, '힙한'), (6, '집중'), (7, '데이트'), (8, '뷰')], max_length=15),
        ),
    ]