from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
  pass


# Die Klasse IST die Tabelle
class User(Base):
  __tablename__ = "users"

  # Die Attribute SIND die Spalten (mit Type Annotations)
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str]
  email: Mapped[str | None]  # Optional[str] (Py 3.10+)