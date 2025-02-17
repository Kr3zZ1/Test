from datetime import datetime
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import UUID, DateTime, ForeignKey, String, Enum, create_engine
import enum
import uuid
Base = declarative_base()


# Класс для смены статуса у заявок
class StatusEnum(enum.Enum):
    NReady = "Не готово"
    GReady = "Готово"
    In_progress = "В работе"
    In_anticipation = "В ожидании"

class WorkerStatusEnum(enum.Enum):
    Free = "Свободен"
    Busy = "Занят"

class PermissionEnum(enum.Enum):
    Client = "Клиент"
    Admin = "Администратор"
    Worker = "Работник"
    Menager = "Менеджер"

class UserBase(Base):
    __tablename__ = "users"

    id : Mapped[UUID] = mapped_column(String(36), primary_key=True)
    name : Mapped[str] = mapped_column(String(60), nullable=False)
    Permission : Mapped[PermissionEnum] = mapped_column(Enum(PermissionEnum),default=PermissionEnum.Client)

class WorkerBase(UserBase):
    __tablename__ = "worker"

    id: Mapped[UUID] = mapped_column(ForeignKey('users.id'), primary_key=True)
    status: Mapped[WorkerStatusEnum] = mapped_column(Enum(WorkerStatusEnum), nullable=False, default=WorkerStatusEnum.Free)

class ManagerBase(UserBase):
    __tablename__ = "Manager"

    id: Mapped[UUID] = mapped_column(ForeignKey('users.id'), primary_key=True)

class AdminBase(UserBase):
    __tablename__ = "Admin"

    id: Mapped[UUID] = mapped_column(ForeignKey('users.id'), primary_key=True)

class OrderBase(Base):
    __tablename__ = "orders"

    id : Mapped[UUID] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    date_start : Mapped[datetime] = mapped_column(DateTime, nullable=False)
    date_end : Mapped[datetime] = mapped_column(DateTime)
    name : Mapped[str] = mapped_column(String(60), nullable=False)
    equipment : Mapped[str] = mapped_column(String(60), nullable=False)
    problem_tipe : Mapped[str] = mapped_column(String(200), nullable=False)
    description : Mapped[str] = mapped_column(String(200))
    status : Mapped[StatusEnum] = mapped_column(Enum(StatusEnum), default= StatusEnum.In_anticipation)
    worker : Mapped[str] = mapped_column(String(60))
    comment : Mapped[list[str]] = mapped_column(String(500))


if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db', echo=True)
    Base.metadata.create_all(engine)
    print("База данных успешно создана!")

    
