from django.test import TestCase
from django.test import Client
from .models import Message


class MessageTest(TestCase):
    # 添加数据
    def setUp(self):
        Message.objects.create(name='Lucy', content='test', timestamp='2015-01-01')
        Message.objects.create(name='May', content='test', timestamp='2015-01-01')

    def test_Message(self):
        info = Message.objects.get(name='Lucy')
        self.assertIsNotNone(info.timestamp)

    def test_post(self):
        c = Client()
        data = {
            'name': 'Tim',
            'content': '删库'
        }
        response = c.post('/', data=data)
        status_code = response.status_code
        info = Message.objects.get(name='Tim')
        self.assertEqual(status_code, 302)
        self.assertEqual(info.content, '删库')
