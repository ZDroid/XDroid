# XDroid

> Potentially good IRC bot

Requires [feedparser](http://code.google.com/p/feedparser/).

Licensed under the MIT License.

## Usage

```bash
$ ./XDroid.py
```

Bot sends random greeting when join a channel.

Press <kbd>Ctrl</kbd> + <kbd>C</kbd> in console to kill bot.

## Commands

Commands start with `+` to avoid conflicts with other IRC bots and services.

* **+time** — display current time
* **+channel** — display channel name
* **+pi** — display pi value
* **+note** — display notice
* **+tux** — draw Tux
* **+site** — display URL of your or any other site
* **+feed** — parse RSS or Atom feed items
* **+quit** — kill bot and exit from Python session
* **+rcn** — reconnect bot

## Customization

Variables you should change in `XDroid.py`:

* `server`
* `port`
* `nick`
* `password`
* `channel`
* `join_delay`
* `greetings`
* `site`
* `feed`

### Adding a new command

Adding new command isn't hard. The best solution is to append your commands to
the file end, with consistent indent. Syntax:

```python
  if msg.find("+command") != -1:
    do_something()
```