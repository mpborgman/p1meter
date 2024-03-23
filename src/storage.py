async def write(values: dict, pg_pool):
    """

    :param values: dict with construction of "field": {"value": 123, "description": "KWH"}
    :param pg_connection: aiopg connection
    :return: None
    """
    # prep data
    columns = "{}".format("\",\"".join(k for k, _ in values.items()))
    sql_values = ""
    for k, v in values.items():
        value = f"{v['value']}," if k != "timestamp" else f"'{v['value']}',"
        sql_values += value
    sql_values = sql_values[:-1]  # cut the last comma

    # Open a cursor to perform database operations
    async with pg_pool.acquire() as conn:
        async with conn.cursor() as cur:
            sql = f"INSERT INTO p1data (\"{columns}\") VALUES ({sql_values});"
            await cur.execute(sql)
            print("Values written to DB...")
