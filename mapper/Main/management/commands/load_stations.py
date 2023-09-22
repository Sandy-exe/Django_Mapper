import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from Main.models import EWaste_facility


class Command(BaseCommand):
    help = 'Load data from EV Station file'

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR /'Main' / 'data' / 'E.csv'
        keys = ('EWaste_facility_name','Longitude','Latitude')  # the CSV columns we will gather data from.
        print(data_file)
    
        records = []
        with open(data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append({k: row[k] for k in keys})

        # extract the latitude and longitude from the Point object
        for record in records:
            record['longitude'] = float(record['Longitude'])
            record['latitude'] = float(record['Latitude'])

            # add the data to the database
            EWaste_facility.objects.get_or_create(
                EWaste_facility_name=record['EWaste_facility_name'],
                latitude=record['latitude'],
                longitude=record['longitude']
            )