# python_lab_01

Лабораторная работа №1 по дисциплине «Алгоритмы и программирование на Python».

## О проекте

Репозиторий содержит 11 учебных заданий по основам Python:
работа со словарями, списками, кортежами, множествами, строками и срезами.

## Структура проекта

```
python_lab_01/
├── 00_distance.py           # расстояние между городами
├── 01_circle.py             # площадь круга и точка внутри круга
├── 02_operations.py         # расстановка знаков операций
├── 03_favorite_movies.py    # срезы строки с фильмами
├── 04_my_family.py          # список семьи и рост
├── 05_zoo.py                # работа со списком животных
├── 06_songs_list.py         # список и словарь песен
├── 07_secret.py             # расшифровка сообщения срезами
├── 08_garden.py             # множества цветов
├── 09_shopping.py           # словарь магазинов и цен
├── 10_store.py              # подсчёт стоимости товаров на складе
├── requirements.txt         # зависимости проекта
└── README.md
```

## Требования

- Python 3.10+
- pip

## Установка и запуск

1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/verrronikaat/python_lab_01.git
   cd python_lab_01
   ```

2. (Опционально) создать виртуальное окружение:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запустить любое задание:
   ```bash
   python 00_distance.py
   python 01_circle.py
   ...
   ```

## Список заданий

| Файл | Что делает |
|---|---|
| `00_distance.py` | Считает расстояния между городами по координатам |
| `01_circle.py` | Площадь круга и проверка точки внутри круга |
| `02_operations.py` | Расставляет знаки между числами 1 2 3 4 5 → 25 |
| `03_favorite_movies.py` | Извлекает фильмы из строки через срезы |
| `04_my_family.py` | Список семьи и общий рост |
| `05_zoo.py` | Вставка, добавление и удаление элементов списка |
| `06_songs_list.py` | Суммирует длительности песен (список и словарь) |
| `07_secret.py` | Расшифровывает фразу с помощью срезов |
| `08_garden.py` | Множества: объединение, пересечение, разность |
| `09_shopping.py` | Находит 2 магазина с минимальными ценами |
| `10_store.py` | Подсчёт количества и стоимости товаров на складе |

## Шпаргалка по git

```bash
git clone <url>              # клонировать репозиторий
git status                   # статус изменений
git add .                    # добавить все файлы
git add file.py              # добавить конкретный файл
git commit -m "сообщение"    # зафиксировать изменения
git push                     # отправить на GitHub
git pull                     # забрать изменения
git log --oneline            # история коммитов
```

## Автор

Вероника — [github.com/verrronikaat](https://github.com/verrronikaat)

## Материалы

- [Официальный туториал Python](https://docs.python.org/3/tutorial/)
- [Документация по срезам](https://docs.python.org/3/reference/expressions.html#slicings)
- [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/)