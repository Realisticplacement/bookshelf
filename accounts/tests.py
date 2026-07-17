from types import SimpleNamespace

from django.test import SimpleTestCase

from accounts.permissions import IsLibarianOrAdmin


class IsLibarianOrAdminTests(SimpleTestCase):
    def setUp(self):
        self.permission = IsLibarianOrAdmin()

    def make_user(self, role="reader", is_staff=False, is_superuser=False):
        return SimpleNamespace(
            is_authenticated=True,
            role=role,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )

    def test_librarian_is_allowed(self):
        request = SimpleNamespace(user=self.make_user(role="libarian"))
        self.assertTrue(self.permission.has_permission(request, None))

    def test_admin_role_is_allowed(self):
        request = SimpleNamespace(user=self.make_user(role="admin"))
        self.assertTrue(self.permission.has_permission(request, None))

    def test_reader_is_denied(self):
        request = SimpleNamespace(user=self.make_user(role="reader"))
        self.assertFalse(self.permission.has_permission(request, None))
