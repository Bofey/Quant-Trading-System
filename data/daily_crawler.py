from util.database import DB_CONN

daily = DB_CONN.daily.find_one({})
