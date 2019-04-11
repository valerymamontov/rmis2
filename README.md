# парсинг XML с помощью xml.dom.minidom
была задача:
- найти внутри xml-файла значения в тегах
- подняться по Dom-структуре на уровень выше и добавить новый тег со значением
- тег добавить не в произвольное место, а между двумя заданными тегами

Не смог решить только одну проблему:
как в заголовке добавить перенос строки

## получалось так:
```
<?xml version="1.0" encoding="Windows-1251"?><ZL_LIST>
  <ZGLV>
```

## а хотел сделать так (как в исходнике):
```
<?xml version="1.0" encoding="Windows-1251"?>

<ZL_LIST>
  <ZGLV>
```
