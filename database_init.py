import sqlite3
import os

def init_database():
    """Инициализация всей структуры базы данных"""
    
    # Подключаемся к БД
    database = sqlite3.connect('database.db')
    sql = database.cursor()
    
    print("🔄 Создаем структуру базы данных...")
    
    # Основные таблицы
    tables = [
        # Таблица чатов
        '''CREATE TABLE IF NOT EXISTS chats (
            chat_id BIGINT PRIMARY KEY,
            peer_id BIGINT,
            owner_id BIGINT,
            welcome_text TEXT DEFAULT 'Добро пожаловать, уважаемый %i пользователь!',
            silence INTEGER DEFAULT 0,
            filter INTEGER DEFAULT 0,
            antiflood INTEGER DEFAULT 0,
            invite_kick INTEGER DEFAULT 0,
            leave_kick INTEGER DEFAULT 0,
            in_pull INTEGER DEFAULT 0
        )''',
        
        # Таблица глобальных менеджеров
        '''CREATE TABLE IF NOT EXISTS global_managers (
            user_id BIGINT PRIMARY KEY,
            level INTEGER DEFAULT 0
        )'''
    ]
    
    # Создаем основные таблицы
    for table_sql in tables:
        sql.execute(table_sql)
    
    # ⚠️ УДАЛЕНО: проблемная строка с ВАШ_VK_ID
    # sql.execute("INSERT OR IGNORE INTO global_managers (user_id, level) VALUES (?, ?)", (ВАШ_VK_ID, 2))
    
    database.commit()
    print("✅ База данных успешно инициализирована!")
    print("📊 Созданы таблицы:")
    print("   - chats (настройки чатов)")
    print("   - global_managers (глобальные админы)")
    print("")
    print("📝 Таблицы для каждого чата будут создаваться автоматически при активации бота")
    
    database.close()

if __name__ == "__main__":
    # Проверяем, существует ли уже БД
    if os.path.exists('database.db'):
        response = input("База данных уже существует. Пересоздать? (y/n): ")
        if response.lower() == 'y':
            os.remove('database.db')
            init_database()
        else:
            print("Отмена.")
    else:
        init_database()