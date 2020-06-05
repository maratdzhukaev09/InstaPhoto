# Космический [Инстаграм](https://www.instagram.com/)

Данный проект позволит получить фотографии с последнего запуска ракет [SpaceX](https://www.spacex.com/) и фотографии снятые [астрономической обсерваторией Hubble](https://hubblesite.org/) с помощью API [[1](https://github.com/r-spacex/SpaceX-API)], [[2](http://hubblesite.org/api/documentation)] и опубликовать их в [Инстаграм](https://www.instagram.com/).

## Подготовка к запуску

Для запуска кода у вас уже должен быть установлен Python 3.

- Скачайте код.
- Создайте файл `.env`. В нём должны быть ваш логин и пароль от вашего Инстаграма:
```
INSTAGRAM_LOGIN=ваш_логин
INSTAGRAM_PASSWORD=ваш_пароль
```
- Установите зависимости с помощью `pip` (или `pip3`, есть есть конфликт с Python2) командой `pip install -r requirements.txt`.

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

## Запуск кода

-  `python fetch_spacex.py` - получите фотографии с последнего запуска [SpaceX](https://www.spacex.com/)
-  `python fetch_hubble.py коллекция` - получите фотографии из коллекций [Hubble](https://hubblesite.org/)
-  `python post_pictures.py` - опубликует скачанные фотографии

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](dvmn.org).