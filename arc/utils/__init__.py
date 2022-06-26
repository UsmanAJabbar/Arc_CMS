from arc import db


def row_to_dict(row: db.Entity) -> dict:
    """
    -----------
    ROW TO DICT
    -----------
    Takes in a Pony ORM row and returns a dictionary
    reprentation of a row { column_name: row_value }

    Returns: dict
    """
    return {
        c: getattr(row, c)
        for c in row._columns_
    }
