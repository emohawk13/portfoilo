import pymysql
import config
import logging

def get_social_menu_items():
    query = "SELECT LinkName, LinkActual FROM Links WHERE LinkRelation = 'Social'"
    try:
        conn = pymysql.connect(
            host=config.MYSQL_HOST,
            port=config.MYSQL_PORT,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            db=config.MYSQL_DB,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        conn.close()

        social_menu_items = []
        for row in results:
            social_menu_items.append({'name': row['LinkName'], 'link': row['LinkActual']})
        return social_menu_items

    except Exception as e:
        logging.error(f"An error occurred while fetching social menu items: {str(e)}")
        return []

# Example usage:
social_menu_items = get_social_menu_items()
print(social_menu_items)


