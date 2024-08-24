from apscheduler.schedulers.background import BackgroundScheduler
from util.connection_helper import get_connection

def deactivate_inactive_users():
    # print('deactivating inactive users')
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql = """
            UPDATE Account
            SET activity = 0
            WHERE last_login < NOW() - INTERVAL 24 HOURS
            """
            cursor.execute(sql)
        conn.commit()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(deactivate_inactive_users, 'interval', hours=1)
    scheduler.start()
