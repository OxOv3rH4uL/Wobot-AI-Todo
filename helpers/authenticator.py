from helpers import connector
from helpers import hash


def authenticate_user(username:str,password:str):
    conn = connector.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select * from users where username=%s",(username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user is not None and hash.verify_password(password,user['password']):
        return user
    return None