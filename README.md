# Tinder Bot:

The idea of this project is to automate likes (Tinder working for its own).

## Recomendations:
Create a virtual enviroment fo executing the code:

- `cd` to the folder you want to install the bot in

- `pip install virtualenv`

- `virtualenv venv`

- `source venv/bin/activate`

## Functions:

- `auto_like()`
- `auto_super()`
- `auto_like_alt()`
- `auto_super_alt()`

## Usage:

- Download chromedriver, unzip, move to /usr/local/bin (Mac OS / Linux)

- Install `selenium` package:

```bash
pip install foobar
```

- Update `credentials.py` with the username and password you use in Tinder (you must log in with a Facebook account).

- Execute the code in interactive mode if you want to try the self methods by your own:

```python
python3 -i tinder_bot.py
```

or executed normally if you want to let the code does its job:

```python
python3 tinder_bot.py
```

```auto_like()``` is the default method and will execute automatically. You can change it at the end of `tinder_bot.py` script.

## Contributing:
The original idea came from [Aaron](https://github.com/aj-4/), as you can check in this [video](https://www.youtube.com/watch?v=lvFAuUcowT4).
