from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from ..models import DataCollection, CatchLocations, FishDetails, bioticData
from ..forms import DataCollectionForm, CatchLocationsForm, BioticDataForm
from maintenance.models import MaintenanceSpeciesList

class FykeAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.data_collection = DataCollection.objects.create(
            date=datetime.now().date(),
            time=datetime.now().time(),
            tidal_phase='High',
            salinity=35.0,
            temperature=15.0,
            wind_direction='N',
            wind_speed=10,
            secchi_depth=5.0,
            fu_scale=3,
            fishingday=1,
            fyke='Fyke1',
            duration=2,
            collect='Collect1',
            remarks='Test remarks',
            observer='Observer1',
            version='1.0',
            changed_by_id=1,
            last_change=timezone.now()
        )
        self.catch_location = CatchLocations.objects.create(
            location_name='Test Location',
            latitude=52.0,
            longitude=4.0,
            remarks='Test remarks'
        )
        self.fish_detail = FishDetails.objects.create(
            collectdate=datetime.now().date(),
            registrationtime=datetime.now().time(),
            collectno=1,
            species=MaintenanceSpeciesList.objects.create(species_id=1, nl_name='Test Species', latin_name='Testus species'),
            condition='Good',
            total_length=30.0,
            fork_length=25.0,
            standard_length=20.0,
            fresh_weight=200.0,
            liver_weight=10.0,
            total_wet_mass=210.0,
            stomach_content='Full',
            gonad_mass=5.0,
            sexe='M',
            ripeness='Ripe',
            otolith='Present',
            total_length_frozen=30.0,
            fork_length_frozen=25.0,
            standard_length_frozen=20.0,
            frozen_mass=200.0,
            height=5.0,
            age=2,
            rings=3,
            ogew1=1.0,
            ogew2=2.0,
            tissue_type='Muscle',
            vial='Vial1',
            comment='Test comment'
        )
        self.biotic_data = bioticData.objects.create(
            date=self.data_collection,
            fishid=self.fish_detail,
            totallength=30.0,
            weight=200.0,
            sex='M',
            maturity='Ripe',
            remarks='Test remarks'
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_datacollection_view(self):
        response = self.client.get(reverse('datacollection'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'datacollection.html')
        self.assertIn('data', response.context)
        self.assertIn('years', response.context)

    def test_new_record_view(self):
        response = self.client.get(reverse('new_record'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'datacollection/new_record.html')
        self.assertIn('form', response.context)

    def test_edit_record_view(self):
        response = self.client.get(reverse('edit_record', args=[self.data_collection.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'datacollection/edit_record.html')
        self.assertIn('form', response.context)

    def test_biotic_view(self):
        response = self.client.get(reverse('biotic', args=[self.data_collection.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'datacollection/biotic.html')
        self.assertIn('form', response.context)
        self.assertIn('species_data', response.context)

    def test_fishdetails_view(self):
        response = self.client.get(reverse('fishdetails'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fishdetails.html')
        self.assertIn('data', response.context)
        self.assertIn('years', response.context)

    def test_species_search_view(self):
        response = self.client.get(reverse('species_search'), {'q': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_catchlocations_view(self):
        response = self.client.get(reverse('catchlocations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catchlocations.html')
        self.assertIn('data', response.context)

    def test_new_location_view(self):
        response = self.client.get(reverse('new_location'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catchlocations/new_location.html')
        self.assertIn('form', response.context)

    def test_edit_location_view(self):
        response = self.client.get(reverse('edit_location', args=[self.catch_location.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catchlocations/edit_location.html')
        self.assertIn('form', response.context)

    def test_exportdata_view(self):
        response = self.client.get(reverse('exportdata'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exportdata.html')
        self.assertIn('years', response.context)

    def test_abiotic_csv_view(self):
        response = self.client.get(reverse('abiotic_csv', args=[0]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')

    def test_biotic_csv_view(self):
        response = self.client.get(reverse('biotic_csv', args=[0]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')

    def test_cutting_csv_view(self):
        response = self.client.get(reverse('cutting_csv', args=[0]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')

    def test_stomach_csv_view(self):
        response = self.client.get(reverse('stomach_csv', args=[0]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')