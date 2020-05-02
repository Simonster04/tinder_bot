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

- Update `credentials.py` with the username and password you use in Tinder.

- Execute the code in interactive mode:

```python
python3 -i tinder_bot.py
```

After checking the bot's logging in was OK, execute a function in the interactive window as below:

```python
>>> bot.auto_like()
```

## Contributing:
The original idea came from [Aaron](https://github.com/aj-4/), as you can check in this [video](https://www.youtube.com/watch?v=lvFAuUcowT4).
