from django.db import migrations, models


def convert_sample_spaces(apps, schema_editor):
    Classroom = apps.get_model('booking', 'Classroom')
    samples = [
        ('A-101', 'Newton Lecture Hall', 'lecture', 80, '2500.00', 'A bright tiered lecture hall for classes, talks, and guest sessions.', 'Projector · Sound system · Whiteboard'),
        ('B-204', 'Ada Computer Lab', 'computer', 40, '3200.00', 'A fully equipped computer lab for practical lessons and workshops.', '40 computers · High-speed Wi-Fi · Projector'),
        ('C-301', 'Tagore Seminar Room', 'seminar', 20, '1800.00', 'A focused and flexible room for discussions, clubs, and meetings.', 'Smart display · Whiteboard · Video conferencing'),
    ]
    for classroom, values in zip(Classroom.objects.order_by('number'), samples):
        classroom.number, classroom.name, classroom.classroom_type, classroom.capacity, classroom.rate_per_day, classroom.description, classroom.amenities = values
        classroom.save()


class Migration(migrations.Migration):
    dependencies = [('booking', '0001_initial')]

    operations = [
        migrations.RenameModel(old_name='Room', new_name='Classroom'),
        migrations.RenameField(model_name='booking', old_name='room', new_name='classroom'),
        migrations.RenameField(model_name='classroom', old_name='room_type', new_name='classroom_type'),
        migrations.RenameField(model_name='classroom', old_name='price_per_night', new_name='rate_per_day'),
        migrations.AlterField(
            model_name='classroom',
            name='classroom_type',
            field=models.CharField(choices=[('lecture', 'Lecture Hall'), ('computer', 'Computer Lab'), ('seminar', 'Seminar Room')], max_length=20),
        ),
        migrations.AlterModelOptions(name='classroom', options={'ordering': ['rate_per_day', 'number']}),
        migrations.RunPython(convert_sample_spaces, migrations.RunPython.noop),
    ]
