from . import models
from .. import db


def add_user(f_name, l_name, nickname, birthday, now_place, phone, e_mail):
    new_entry = models.User(
        f_name=f_name,
        l_name=l_name,
        nickname=nickname,
        birthday=birthday,
        now_place=now_place,
        phone=phone,
        e_mail=e_mail,
    )
    db.session.add(new_entry)
    db.session.commit()


def add_event(
    name,
    description,
    art_form_id,
    genre_id,
    date_time,
    dt_start,
    dt_over,
    cost_min,
    cost_max,
    currency,
    organizer_id,
    place_id,
    link,
    photo,
):
    event = models.Event(
        name=name,
        description=description,
        art_form=art_form_id,
        genre=genre_id,
        date_time=date_time,
        dt_start=dt_start,
        dt_over=dt_over,
        cost_min=cost_min,
        cost_max=cost_max,
        currency=currency,
        organizer=organizer_id,
        place=place_id,
        link=link,
        photo=photo,
    )
    db.session.add(event)
    db.session.commit()


def add_organizer(name, description):
    organizer = models.Organizer(name=name, description=description)
    db.session.add(organizer)
    db.session.commit()


def add_place(
    name,
    description,
    country,
    city,
    district,
    street,
    num_building,
    liter_building,
    level,
    mono_address,
):
    place = models.Place(
        name=name,
        description=description,
        country=country,
        city=city,
        district=district,
        street=street,
        num_building=num_building,
        liter_building=liter_building,
        level=level,
        mono_address=mono_address,
    )
    db.session.add(place)
    db.session.commit()


def add_genre(name):
    genre = models.Genre(name=name)
    db.session.add(genre)
    db.session.commit()


def add_art_form(name):
    art_form = models.ArtForm(name=name)
    db.session.add(art_form)
    db.session.commit()


def add_user_friendly_event(user_id, event_id, friendly, is_visit):
    user_friendly_event = models.UserFriendlyEvent(
        id_user=user_id, id_event=event_id, friendly=friendly, is_visit=is_visit
    )
    db.session.add(user_friendly_event)
    db.session.commit()


def add_user_friendly_genre(user_id, genre_id, friendly):
    user_friendly_genre = models.UserFriendlyGenre(
        id_user=user_id, id_genre=genre_id, friendly=friendly
    )
    db.session.add(user_friendly_genre)
    db.session.commit()


def add_user_friendly_art_form(user_id, art_form_id, friendly):
    user_friendly_art_form = models.UserFriendlyArtForm(
        id_user=user_id, id_artform=art_form_id, friendly=friendly
    )
    db.session.add(user_friendly_art_form)
    db.session.commit()


def add_user_friendly_organizer(user_id, organizer_id, friendly):
    user_friendly_organizer = models.UserFriendlyOrganizer(
        id_user=user_id, id_organizer=organizer_id, friendly=friendly
    )
    db.session.add(user_friendly_organizer)
    db.session.commit()


def add_user_friendly_place(user_id, place_id, friendly):
    user_friendly_place = models.UserFriendlyPlace(
        id_user=user_id, id_place=place_id, friendly=friendly
    )
    db.session.add(user_friendly_place)
    db.session.commit()


def full_delete_table_records(tables):
    for table in tables:
        table_up = table.capitalize()
        table_class = globals()[table_up]
        db.session.query(table_class).delete()
        print(f"Таблица {table_up} полностью очищена.")
    db.session.commit()


# def total_delete_table_records(confirm):
#     if not confirm:
#         print(
#             "Введите в качестве аргумента - 1, для подтверждения полной очистки Базы Данных."
#         )
#     elif confirm == 1:
#         inspector = inspect(engine)
#         tables = inspector.get_table_names()

#         for table_name in tables:
#             if inspector.has_table(table_name):
#                 tbl = Table(table_name, metadata)
#                 db.session.execute(tbl.delete())

#         db.session.commit()
#         print("Все записи были успешно удалены из всех таблиц.")
#     else:
#         print(
#             "Вы вызвали функцию 'удаления всех значений из всех таблиц' и передали аргумент отменяющий это действие."
#         )


# def delete_concrete_entry_in_table(table_name, entry_id):
#     inspector = inspect(engine)
#     existing_tables = inspector.get_table_names()
#     table_lower = table_name.lower()
#     if table_lower in existing_tables:
#         # Получаем класс модели таблицы по имени таблицы
#         if table_name[0].isupper():
#             table_class = globals()[table_name]
#         else:
#             table_up = table_name.capitalize()
#             table_class = globals()[table_up]

#         # Ищем запись по первичному ключу
#         entry = db.session.query(table_class).get(entry_id)
#         if entry:
#             # Удаляем запись из сессии и подтверждаем изменения
#             db.session.delete(entry)
#             db.session.commit()
#             print(
#                 f"Запись с id={entry_id} успешно удалена из таблицы {table_name.capitalize()}."
#             )
#         else:
#             print(
#                 f"Запись с id={entry_id} не найдена в таблице {table_name.capitalize()}."
#             )
#     else:
#         print(
#             f"Таблицы {table_name} не существует. Существующие таблицы: {', '.join(existing_tables)}."
#         )


# def update_cell_in_table(table_name, field, id, value):
#     if table_name[0].isupper():
#         table_class = globals()[table_name]
#     else:
#         table_name = table_name.capitalize()
#         table_class = globals()[table_name]
#     # Ищем пользователя по первичному ключу
#     table = db.session.query(table_class).get(id)

#     if table:
#         # Обновляем поле соответствующее переданному значению
#         setattr(table, field, value)
#         db.session.commit()
#         print(f"Поле '{field}' строки с id={id} успешно обновлено.")
#     else:
#         print(f"Пользователь с id={id} не найден.")


# def print_table(table_name):
#     inspector = inspect(engine)
#     existing_tables = inspector.get_table_names()
#     table_lower = table_name.lower()
#     # Проверяем, существует ли таблица
#     if table_lower in existing_tables:
#         # Получаем класс таблицы по названию
#         table_class = globals()[table_name]

#         # Получаем все записи из таблицы
#         records = db.session.query(table_class).all()

#         # Выводим значения записей
#         for record in records:
#             record_dict = {}
#             for column in table_class.__table__.columns:
#                 if column.name == "id":
#                     # Добавляем поле 'id' со значением record.id в словарь
#                     record_dict["id"] = record.id
#                 else:
#                     # Добавляем все остальные поля со значениями в словарь
#                     value = getattr(record, column.name)
#                     record_dict[column.name] = value
#             print(record_dict)
#     else:
#         print(f"Таблицы {table_name} не существует.")


# def get_table(table_name):
#     inspector = inspect(engine)
#     existing_tables = inspector.get_table_names()
#     table_lower = table_name.lower()

#     # Проверяем, существует ли таблица
#     if table_lower in existing_tables:
#         # Получаем класс таблицы по названию
#         table_class = globals()[table_name]

#         # Получаем все записи из таблицы
#         records = db.session.query(table_class).all()

#         rows = []

#         # Проходимся по записям и формируем значения строк
#         for record in records:
#             row_dict = {}
#             for column in table_class.__table__.columns:
#                 if column.name == "id":
#                     # Добавляем поле 'id' со значением record.id в словарь
#                     row_dict["id"] = record.id
#                 else:
#                     # Добавляем все остальные поля со значениями в словарь
#                     value = getattr(record, column.name)
#                     row_dict[column.name] = value
#             rows.append(row_dict)

#         return rows
#     else:
#         print(f"Таблицы {table_name} не существует.")
#         return []


# def get_table_row(table_name, row_id):
#     inspector = inspect(engine)
#     existing_tables = inspector.get_table_names()
#     table_lower = table_name.lower()

#     # Проверяем, существует ли таблица
#     if table_lower in existing_tables:
#         # Получаем класс таблицы по названию
#         table_class = globals()[table_name]

#         # Получаем запись из таблицы по указанному идентификатору
#         record = db.session.query(table_class).get(row_id)

#         # Проверяем, найдена ли запись
#         if record is not None:
#             row_dict = {}
#             for column in table_class.__table__.columns:
#                 if column.name == "id":
#                     # Добавляем поле 'id' со значением record.id в словарь
#                     row_dict["id"] = record.id
#                 else:
#                     # Добавляем все остальные поля со значениями в словарь
#                     value = getattr(record, column.name)
#                     row_dict[column.name] = value

#             return row_dict
#         else:
#             print(
#                 f"Запись с идентификатором {row_id} не найдена в таблице {table_name}."
#             )
#     else:
#         print(f"Таблицы {table_name} не существует.")
