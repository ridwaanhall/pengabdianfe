from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse

# class URLTests(TestCase):
#     def test_index_url(self):
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'index.html')

#     def test_list_pamong_url(self):
#         response = self.client.get(reverse('list-pamong'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'list-pamong.html')

#     def test_edit_pamong_url(self):
#         response = self.client.get(reverse('edit-pamong'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'edit-pamong.html')

#     def test_tambah_pamong_url(self):
#         response = self.client.get(reverse('tambah-pamong'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'tambah-pamong.html')

#     def test_list_kegiatan_url(self):
#         response = self.client.get(reverse('list-kegiatan'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'list-kegiatan.html')

#     def test_edit_kegiatan_url(self):
#         response = self.client.get(reverse('edit-kegiatan'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'edit-kegiatan.html')

#     def test_tambah_kegiatan_url(self):
#         response = self.client.get(reverse('tambah-kegiatan'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'tambah-kegiatan.html')

#     def test_login_url(self):
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'login.html')

#     def test_forgot_password_url(self):
#         response = self.client.get(reverse('forgot-password'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'forgot-password.html')
