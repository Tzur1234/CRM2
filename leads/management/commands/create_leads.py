from django.core.management.base import BaseCommand
from csv import reader, DictReader
from leads.models import Lead, UserProfile

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)
        parser.add_argument('organizer_email', type=str)

    def handle(self,*args, **arguments):

        # the UserProfile
        organization = UserProfile.objects.get(user__email=arguments['organizer_email']) 
        # Read from the csv file
        with open(arguments['file_name'], 'r') as read_obj:
            csv_reader = DictReader(read_obj)
            for mydic in csv_reader:
                first_name = mydic['first_name'] 
                last_name = mydic['last_name']
                email = mydic['email']
                organization = organization

                # Create a the new Lead obj
                Lead.objects.create(
                    first_name = first_name,
                    last_name = last_name,

                    email = email,
                    organization = organization
                ) 

        # Create a new lead (based on the the organizer's email)
        

        