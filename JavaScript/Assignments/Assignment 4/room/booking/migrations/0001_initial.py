from django.core.validators import MinValueValidator
from django.db import migrations, models
import django.db.models.deletion


def create_sample_rooms(apps, schema_editor):
    Room = apps.get_model('booking', 'Room')
    Room.objects.bulk_create([
        Room(number='101', name='The Linden', room_type='cozy', capacity=2, price_per_night='4200.00', description='A calm king room with soft light and garden views.', amenities='King bed · Wi-Fi · Breakfast included'),
        Room(number='204', name='The Terrace', room_type='deluxe', capacity=2, price_per_night='6400.00', description='A spacious suite made for slow mornings and long evenings.', amenities='King bed · Private terrace · Breakfast included'),
        Room(number='301', name='The Hearth', room_type='family', capacity=4, price_per_night='7800.00', description='An easy, generous space for families and friends.', amenities='Two queen beds · Lounge area · Breakfast included'),
    ])


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=80)),
                ('room_type', models.CharField(choices=[('cozy', 'Cozy King'), ('deluxe', 'Deluxe Suite'), ('family', 'Family Residence')], max_length=20)),
                ('capacity', models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.CharField(max_length=180)),
                ('amenities', models.CharField(max_length=240)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'ordering': ['price_per_night', 'number']},
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=100)),
                ('guest_email', models.EmailField(max_length=254)),
                ('guests', models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('confirmation_code', models.CharField(max_length=14, unique=True)),
                ('status', models.CharField(choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='confirmed', max_length=12)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='booking.room')),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.RunPython(create_sample_rooms, migrations.RunPython.noop),
    ]
