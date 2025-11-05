# unittest (Umständlich)
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)


# pytest (Pythonic, sauber)
# (Keine Imports, keine Klasse nötig)

def test_add():
    assert add(2, 3) == 5


def test_capitalize():
  assert "hello".capitalize() == "Hello"


def test_type_error():
  # Testet, ob der erwartete Fehler auftritt
  with pytest.raises(TypeError):
    "string" + 5



import pytest

@pytest.fixture
def empty_user_db():
    """Stellt eine leere In-Memory-DB bereit."""
    db = setup_database()
    yield db # 1. Test läuft hier...
    db.cleanup() # 2. ...Teardown (wird garantiert ausgeführt)

# --- Nutzung ---

def test_add_user(empty_user_db): # Fixture wird hier "injiziert"
    db = empty_user_db
    db.add_user("alice")
    assert db.count() == 1


def is_valid_email(email):
  # ... Logik ...
  pass


@pytest.mark.parametrize("email_input, expected_result", [
  ("test@mail.com", True),  # Fall 1
  ("user.name@sub.domain.org", True),  # Fall 2
  ("invalid-mail", False),  # Fall 3 (Edge Case)
  ("", False),  # Fall 4 (Edge Case)
  (None, False),  # Fall 5 (Edge Case)
])
def test_email_validation(email_input, expected_result):
  assert is_valid_email(email_input) == expected_result

def test_charge_user(mocker):  # 'mocker' Fixture anfordern

  # Ersetze 'requests.post' durch einen Mock,
  # der ein Fake-JSON zurückgibt
  mocker.patch("requests.post",
               return_value=MockResponse(status_code=200))

  # Führe den Test aus
  result = payment_service.charge_user("user_123", 100)

  # Teste *unseren* Code, nicht die API
  assert result == "SUCCESS"