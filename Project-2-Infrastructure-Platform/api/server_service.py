from database import get_connection


#------create new server-----------------
def create_server(hostname, ip_address, os, environment):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO servers (hostname, ip_address, os, environment)
        VALUES (%s, %s, %s, %s)
        RETURNING server_id, hostname, ip_address, os, environment
    """, (hostname, ip_address, os, environment))

    row = cursor.fetchone()
    connection.commit()

    cursor.close()
    connection.close()

    return {
        "server_id": row[0],
        "hostname": row[1],
        "ip_address": str(row[2]),
        "os": row[3],
        "environment": row[4]
    }

#----fetch all server list-----
def get_all_servers():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT server_id, hostname, ip_address, os, environment
        FROM servers
    """)

    rows = cursor.fetchall()

    servers = []

    for row in rows:
      server = {
         "server_id": row[0],
         "hostname": row[1],
         "ip_address": str(row[2]),
         "os": row[3],
         "environment": row[4]
      }

      servers.append(server)

    cursor.close()
    connection.close()

    return servers

#fetch one server info by server_id--------------
def get_one_server(server_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT server_id, hostname, ip_address, os, environment
    FROM servers
    WHERE server_id = %s
    """, (server_id,))

    rows = cursor.fetchone()
    if rows is None:
      return jsonify({"error": "Server not found"}), 404

    server = {
      "server_id": rows[0],
      "hostname": rows[1],
      "ip_address": str(rows[2]),
      "os": rows[3],
      "environment": rows[4]
    }
    cursor.close()
    connection.close()
    return server

doc
# ------ update server -----------------------
def update_server(server_id, hostname, ip_address, os, environment):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE servers
        SET hostname = %s,
            ip_address = %s,
            os = %s,
            environment = %s
        WHERE server_id = %s
        RETURNING server_id, hostname, ip_address, os, environment
    """, (hostname, ip_address, os, environment, server_id))

    row = cursor.fetchone()

    if row is None:
        connection.rollback()
        cursor.close()
        connection.close()
        return None

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "server_id": row[0],
        "hostname": row[1],
        "ip_address": str(row[2]),
        "os": row[3],
        "environment": row[4]
    } 

