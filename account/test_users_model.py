from django.test import TestCase
import pytest
from .models import CustomUser  # Import your model

@pytest.mark.django_db
def test_create_user():
    user = CustomUser.objects._create_user(
        username='testuser',
        email='test@example.com',
        password='password123'
    )
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser
