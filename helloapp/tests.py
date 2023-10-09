from django.test import SimpleTestCase, Client


class ViewTests(SimpleTestCase):
    def test_home_page_response(self):
        client = Client()
        resp = client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Hello, world!')
        self.assertContains(resp, 'About')

    def test_about_page_response(self):
        client = Client()
        resp = client.get('/about/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'This is an example')
        self.assertContains(resp, 'Home')
web: python3 -m ptvsd --port 3000 --host 0.0.0.0 manage.py runserver 0.0.0.0:8080 --noreload
source /Users/webtechnicom/PycharmProjects/venv/bin/activate
(base) webtechnicom@MacBook-Pro-de-steve hello-world-2 % source /Users/webtechnicom/PycharmP
rojects/venv/bin/activate
(venv) (base) webtechnicom@MacBook-Pro-de-steve hello-world-2 % >....                       
        echo "Expected content found -- site is up"
        echo "END CONTENT TEST: Success! ✅"