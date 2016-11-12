from django.test import TestCase
from django.http import HttpRequest

from signup.views import home_page
from signup.forms import SubscriberForm
from signup.models import Subscriber, City


# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_uses_attendee_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], SubscriberForm)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['email'] = 'new@email.com'
        City.objects.create(name='Boston', state='MA')
        request.POST['city'] = 'Boston'

        response = home_page(request)

        self.assertEqual(Subscriber.objects.count(), 1)
        new_subscriber = Subscriber.objects.first()
        self.assertEqual(new_subscriber.email, 'new@email.com')
        self.assertEqual(new_subscriber.city.name, 'Boston')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_prevents_duplicate_email(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['email'] = 'new@email.com'
        city = City.objects.create(name='Boston', state='MA')
        Subscriber.objects.create(email='new@email.com', city=city)
        request.POST['city'] = 'Boston'
        self.assertEqual(Subscriber.objects.count(), 1)

        home_page(request)

        self.assertEqual(Subscriber.objects.count(), 1)
