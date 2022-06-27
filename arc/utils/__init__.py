from arc.database import db


default_exclude_fields = (
    'password',
)
def row_to_dict(
    row: db.Entity,
    exclude_fields: tuple = default_exclude_fields
) -> dict:
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
        if c not in exclude_fields
    }
