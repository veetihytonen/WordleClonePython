# Wordle

This app is a clone of the popular game wordle. The state of an ongoing game is saved on quitting the app and loaded automatically on starting the app. The app has no separate users for now, as it is not necessary for this manner of app, though they could potentially be implemented if there is sufficent time.

## About Python version

This app has been tested on Python 3.9. Different versions may cause issues.

## Documentation

[vaatimusmäärittely.md](https://github.com/veetihytonen/WordleClonePython/blob/main/dokumentaatio/vaatimusmäärittely.md)

[tuntikirjanpito.md](https://github.com/veetihytonen/WordleClonePython/blob/main/dokumentaatio/tuntikirjanpito.md)

[changelog.md](https://github.com/veetihytonen/WordleClonePython/blob/main/dokumentaatio/changelog.md)

## Installation

1. Install dependencies with command:

```bash
poetry install
```

2. Run the app with command start

(doesn't actually do much for now since I've only implemented the game logic, not the functionality that uses it)

```bash
poetry run invoke start
```

## Command line commands 

## Run the app

```bash
poetry run invoke start
```

## Testing

Tests are run with 

```bash
poetry run invoke test
```

## Test coverage

```bash
poetry run invoke coverage-report
```

Report is generated into htmlcov file


