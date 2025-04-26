# TELEGRAM TF-IDF ЧАТ-БОТ

Простой бот (не умный) построен на базе TF-IDF + cosine similarity, ищет лучший ответ из кастомного датасета. 

## Что делает бот

- Ты пишешь сообщение → бот анализирует → бот отвечает на основе самого близкого по смыслу текста из датасета.
- Работает на твоём собственном корпусе данных (`dataset.json.gz`).
- Прямо на базе `telegram` бота через `python-telegram-bot v20+`.

---

## Как запустить

1. Установи все зависимости:

```bash
pip install -r requirements.txt

2. Скачай датасет
https://drive.google.com/file/d/1bDTiUAeIlB_jSLR4hENAT6QvYC7w0zFh/view?usp=drive_link

3. Получи API 
@BotFather
