# XDroid

> Pure droid-powered IRC bot

Requires [feedparser](http://code.google.com/p/feedparser/).

## Usage

```bash
$ ./XDroid.py
```

Bot sends random greeting when it joins a channel.

Press <kbd>Ctrl</kbd> + <kbd>C</kbd> in console to kill bot.

## Commands

Commands start with `+` to avoid conflicts with other IRC bots.

- **+time:** display current time
- **+channel:** display channel name
- **+pi:** display pi value
- **+note:** display notice
- **+tux:** draw Tux
- **+site:** display URL of your or any other site
- **+feed:** parse RSS or Atom feed items
- **+quit:** kill bot and exit from Python session
- **+rcn:** reconnect bot

## Configuration

Variables you may want to change in `XDroid.py`:

- `server`
- `port`
- `nick`
- `password`
- `channel`
- `join_delay`
- `greetings`
- `site`
- `feed`

## New command

Adding a new command isn't hard. The best way is to append your commands to the
file end, with consistent indent.

Syntax:

```python
  if msg.find("+command") != -1:
    do_something
```

## License

MIT &copy; [Zlatan Vasović](https://github.com/ZDroid)