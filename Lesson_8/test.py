import pytest
from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:John62rus@localhost:5432/QA"

engine = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(engine)
    names = inspector.get_table_names()
    assert 'student' in names

def test_insert_student():

    with engine.connect() as connection:
        sql = text("INSERT INTO student ("
                   "user_id,"
                   " level, "
                   "education_form,"
                   " subject_id"
                   ") "
                   "VALUES (:user_id, :level, :education_form, :subject_id)")
        connection.execute(sql, {
            "user_id": 1, "level": "Beginner",
            "education_form": "group", "subject_id": 2
        })

        check_sql = text("SELECT level FROM student WHERE user_id = :user_id")
        result = connection.execute(check_sql, {"user_id": 1}).fetchone()
        assert result[0] == "Beginner"

        delete_sql = text("DELETE FROM student WHERE user_id = :user_id")
        connection.execute(delete_sql, {"user_id": 1})


def test_update_student():
    with engine.connect() as connection:
        insert_sql = text("INSERT INTO student ("
                          "user_id,"
                          " level,"
                          " education_form,"
                          " subject_id) "
                          "VALUES (:user_id, :level, "
                          ":education_form, :subject_id)"
                          )
        connection.execute(insert_sql, {
            "user_id": 1, "level": "Beginner",
            "education_form": "group", "subject_id": 1
        })

        update_sql = text("UPDATE student SET level = :level "
                          "WHERE user_id = :user_id")
        connection.execute(update_sql, {
            "level": "Intermediate", "user_id": 1
        })

        check_sql = text("SELECT level FROM student "
                         "WHERE user_id = :user_id")
        result = connection.execute(check_sql,
                                    {"user_id": 1}).fetchone()
        assert result[0] == "Intermediate"

        delete_sql = text("DELETE FROM student "
                          "WHERE user_id = :user_id")
        connection.execute(delete_sql, {"user_id": 1})


def test_delete_student():
    with engine.connect() as connection:
        insert_sql = text("INSERT INTO student ("
                          "user_id,"
                          "level,"
                          "education_form,"
                          "subject_id) "
                          "VALUES (:user_id, :level, "
                          ":education_form, :subject_id)")
        connection.execute(insert_sql, {
            "user_id": 1, "level": "Beginner",
            "education_form": "group", "subject_id": 2
        })

        delete_sql = text("DELETE FROM student "
                          "WHERE user_id = :user_id")
        connection.execute(delete_sql, {"user_id": 3})

        check_sql = text("SELECT user_id FROM student "
                         "WHERE user_id = :user_id")
        connection.execute(check_sql, {"user_id": 3}).fetchone()