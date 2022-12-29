from persistance.inter_tables import *


def execute_query_one():
    with engine.connect() as con:
        rows=[]
        query='SELECT DISTINCT * FROM author'
        keys=list(con.execute(query).keys())
        rs = con.execute(query)
        print(keys)
        for row in rs:
            rows.append(row)
        print(rows)
        return (rows,keys)