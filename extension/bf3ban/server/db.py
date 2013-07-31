import sqlite3
con = sqlite3.connect('db.sqlite')


def init_db():
    try:
        con.execute("SELECT * FROM servers LIMIT 1")
    except sqlite3.OperationalError:
        con.execute("""
            CREATE TABLE servers
            (ip_address varchar(15), description text, reason text)
        """)


def add_server(ip_address, reason="default", description="-"):
    data = (ip_address, reason, description)
    con.execute(
        "INSERT INTO servers VALUES (?, ?, ?)",
        data
    )
    con.commit()


def delete_server(ip_address):
    data = (ip_address, )
    con.execute(
        "DELETE FROM servers WHERE ip_address = ?",
        data
    )
    con.commit()


def update_server(ip_address, reason="default", description="-"):
    data = (reason, description, ip_address)
    con.execute(
        "UPDATE servers SET reason=?, description=? WHERE ip_address=?",
        data
    )
    con.commit()


def get_servers():
    servers = []
    for row in con.execute("SELECT * FROM servers"):
        servers.append(dict(
            zip(('ip', 'description', 'reason'), row)
        ))
    return servers


def main():
    init_db()

if __name__ == '__main__':
    main()
