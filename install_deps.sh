#!/bin/bash
echo "Установка зависимостей для VK бота..."
pip install --upgrade pip
pip install vkbottle==4.6.2
pip install Flask==2.3.0
pip install python-dotenv==1.0.0
echo "✅ Зависимости установлены!"
