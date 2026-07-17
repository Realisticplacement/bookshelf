from types import SimpleNamespace

from django.test import SimpleTestCase

from books.permissions import IsBookManagerOrReadOnly


class IsBookManagerOrReadOnlyTests(SimpleTestCase):
    def setUp(self):
        self.permission = IsBookManagerOrReadOnly()

    def make_user(self, role="reader", is_staff=False, is_superuser=False, user_id=1):
        return SimpleNamespace(
            id=user_id,
            is_authenticated=True,
            role=role,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )

    def test_librarian_can_create_book(self):
        request = SimpleNamespace(method="POST", user=self.make_user(role="libarian"))
        self.assertTrue(self.permission.has_permission(request, None))

    def test_librarian_cannot_update_book(self):
        request = SimpleNamespace(method="PATCH", user=self.make_user(role="libarian"))
        self.assertFalse(self.permission.has_permission(request, None))

    def test_librarian_can_delete_own_upload(self):
        user = self.make_user(role="libarian", user_id=7)
        book = SimpleNamespace(uploaded_by=user)
        request = SimpleNamespace(method="DELETE", user=user)
        self.assertTrue(self.permission.has_object_permission(request, None, book))

    def test_librarian_cannot_delete_other_upload(self):
        librarian = self.make_user(role="libarian", user_id=7)
        other_user = self.make_user(role="libarian", user_id=8)
        book = SimpleNamespace(uploaded_by=other_user)
        request = SimpleNamespace(method="DELETE", user=librarian)
        self.assertFalse(self.permission.has_object_permission(request, None, book))

    def test_admin_can_delete_any_upload(self):
        admin = self.make_user(role="libarian", is_staff=True, user_id=9)
        book = SimpleNamespace(uploaded_by=self.make_user(role="libarian", user_id=10))
        request = SimpleNamespace(method="DELETE", user=admin)
        self.assertTrue(self.permission.has_object_permission(request, None, book))
