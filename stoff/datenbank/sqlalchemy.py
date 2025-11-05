from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
  pass


# Die Klasse IST die Tabelle
class User(Base):
  __tablename__ = "users"

  # Die Attribute SIND die Spalten (mit Type Annotations)
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str]
  email: Mapped[str | None]



# --- INSERT ---
new_user = User(name="Bob", email="bob@mail.com")
session.add(new_user)

# --- SELECT ---
# Kein SQL! Nur Python-Objekte und Methoden.
# IDE kann dies automatisch vervollständigen!
user = session.query(User).filter_by(name="Bob").first()

if user:
    print(f"Gefunden: {user.name} (ID: {user.id})")

session.commit()