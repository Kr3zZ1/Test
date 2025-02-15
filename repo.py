from datetime import datetime
from uuid import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, String, Enum
import enum

# Класс для смены статуса у заявок
class StatusEnum(enum.Enum):
    NReady = "Не готово"
    GReady = "Готово"
    In_progress = "В работе"
    In_anticipation = "В ожидании"

class StatusUserEnum(enum.Enum):
    Client = "Клиент"
    Admin = "Администратор"

class Base(DeclarativeBase):
    pass

class OrderBase(Base):
    __tablename__ = "orders"

    id : Mapped[UUID] = mapped_column(primary_key=True)
    #created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow) еще одна запись даты, но она устанавливается автоматически
    date_start : Mapped[datetime] = mapped_column(DateTime) #с помощью этой строки мы даем понять что нужно вводить данные вручную
    date_end : Mapped[datetime] = mapped_column(DateTime)
    name : Mapped[str] = mapped_column(String(60))
    equipment : Mapped[str] = mapped_column(String(60))
    problem_tipe : Mapped[str] = mapped_column(String(200))
    description : Mapped[str] = mapped_column(String(200))
    status : Mapped[StatusEnum] = mapped_column(Enum(StatusEnum), default= StatusEnum.In_anticipation)
    worker : Mapped[str] = mapped_column(String(60))
    comment : Mapped[list[str]] = mapped_column(String(500))


class UserBase(Base):
    __tablename__ = "users"

    id : Mapped[UUID] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(60))
    status : Mapped[StatusEnum] = mapped_column(Enum(StatusUserEnum),default=StatusUserEnum.Client)


