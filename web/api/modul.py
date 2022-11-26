import os
from datetime import datetime

def now_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M")

def put_log_api(mess):
    if not os.path.exists("api.log"):
        f=open("api.log", 'w')
        f.close()
    with open("api.log", 'r+') as dt:
        dt_d = dt.read()
        dt_d += f"\n[{now_time()}] {mess}"
        dt.seek(0)
        dt.write(dt_d)
        dt.truncate()
    

def insert_to_table(engine, table_name, frmt, values):
    with engine.connect() as conn:
        try:
            conn.execute("INSERT INTO {}({}) VALUES ('{}')".format(table_name, ",".join(frmt), "','".join(values)))
        except Exception as ex:
            # put_log_api(str(ex))
            put_log_api("[", now_time(), "]", str(ex))
            pass
    return

def list_all_data_add_sidikjari(engine, tb_name, type="dict"):
    with engine.connect() as conn:
        rows = conn.execute("SELECT * FROM {}".format(tb_name)).fetchall()
        if type == "dict":
            det = []
            for row in rows:
                det.append({"id": row[0], "finger": f"{row[1]}", "time_push": f"{row[2]}"})
            return det
        if type == "list":
            return rows

def del_data_in_tb(engine, tb_name, data):
    "data isi nya adalah 'by': key_value, 'value': value_data"
    with engine.connect() as conn:
        try:
            conn.execute('DELETE FROM {} WHERE {}="{}"'.format(tb_name, data["by"], data["value"]))
        except Exception as ex:
            put_log_api("[", now_time(), "]", str(ex))
            sta = False
        else: sta=True
    return sta