import os
import mysql.connector

from dotenv import load_dotenv

load_dotenv()


def get_connection():

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def create_case(
    case_id,
    product,
    question
):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO cases
    (
        case_id,
        product,
        category,
        status,
        question
    )
    VALUES (%s,%s,%s,%s,%s)
    """

    values = (
        case_id,
        product,
        "Support",
        "Open",
        question
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()


def update_response(
    case_id,
    response
):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    UPDATE cases
    SET response = %s
    WHERE case_id = %s
    """

    cursor.execute(
        query,
        (
            response,
            case_id
        )
    )

    connection.commit()

    cursor.close()
    connection.close()


def get_case_by_id(case_id):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM cases
    WHERE case_id = %s
    """

    cursor.execute(query, (case_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

def create_escalation(
    case_id,
    reason
):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO escalations
    (
        case_id,
        reason
    )
    VALUES (%s,%s)
    """

    cursor.execute(
        query,
        (
            case_id,
            reason
        )
    )

    connection.commit()

    cursor.close()
    connection.close()