# Автор
PLushkin https://t.me/plushkin_blog        

**На чай с плюшками автору:**
Полигон, БСК, Арбитрум - любые токены - `0x79a266c66cf9e71Af1108728e455E0B1D311e95E`
Трон TRC-20 только USDT, остальное не доходит - `TEZG4iSmr31wWnvBixKgUN9Aax4bbgu1s3`

# Чё делает
генерирует аптос адресса из приватных ключей.

ДОбавьте ваши приватники в файл private_keys.txt
и запускайте.  На выходе получите еще один файл с адресами, порядок сдресов соответствует порядку приватников.


Установка и запуск: Linux/Mac

```
python -m venv .venv
source .venv/bin/activate
pip install aptos-sdk==0.4.1

python main.py

```
Windows - https://www.youtube.com/watch?v=EqC42mnbByc

```
pip install virtualenv
virtualenv .venv
.venv\Scripts\activate
pip install aptos-sdk==0.4.1

python main.py
```


