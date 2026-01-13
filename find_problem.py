import re

print("🔧 Автоматическое исправление main.py...")

# Читаем исходный файл
with open('main.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Удаляем ВСЕ упоминания проблемной переменной
patterns_to_remove = [
    r'sql\.execute\("INSERT OR IGNORE INTO global_managers.*?ВАШ_VK_ID.*?\)\)',
    r'ВАШ_VK_ID',
    r'YOUR_VK_ID',
    r'YOUR_REAL_VK_ID'
]

original_content = content
for pattern in patterns_to_remove:
    content = re.sub(pattern, '# УДАЛЕНО: проблемная переменная', content)

# Заменяем блок инициализации БД на чистый
new_db_code = '''# === ИСПРАВЛЕННАЯ БАЗА ДАННЫХ ===
import sqlite3

try:
    database = sqlite3.connect('database.db', check_same_thread=False)
    sql = database.cursor()
    
    sql.execute('''CREATE TABLE IF NOT EXISTS chats (
        chat_id BIGINT PRIMARY KEY,
        peer_id BIGINT,
        owner_id BIGINT,
        welcome_text TEXT,
        silence INTEGER,
        filter INTEGER,
        antiflood INTEGER,
        invite_kick INTEGER,
        leave_kick INTEGER,
        in_pull INTEGER
    )''')
    
    sql.execute('''CREATE TABLE IF NOT EXISTS global_managers (
        user_id BIGINT PRIMARY KEY,
        level INTEGER
    )''')
    
    database.commit()
    print("✅ База данных создана")
except Exception as e:
    print(f"⚠️ База данных: {e}")
'''

# Находим и заменяем старый блок БД
old_db_pattern = r'database = sqlite3\.connect\(.*?bot = Bot\(token=open_file\[\'bot-token\'\]\)'
content = re.sub(old_db_pattern, new_db_code + '\\n\\nbot = Bot(token=open_file[\'bot-token\'])', content, flags=re.DOTALL)

# Сохраняем исправленный файл
with open('main.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Файл main.py исправлен!")
print("🗑️ Удалены все проблемные переменные")
print("🔄 Перезаписан блок базы данных")

# Удаляем старый файл БД чтобы создать чистый
import os
if os.path.exists('database.db'):
    os.remove('database.db')
    print("🗑️ Старая БД удалена")

print("🎉 Теперь запускайте: python main.py")