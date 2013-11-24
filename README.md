# XDroid

**XDroid** is a potentially good IRC bot. He uses
[feedparser](http://code.google.com/p/feedparser/).

Licensed under the MIT License.

## Usage

```bash
$ ./XDroid.py
```

Press <kbd>Ctrl</kbd> + <kbd>C</kbd> in console to kill bot.

## Commands

Commands start with `+` to avoid conflicts with other IRC bots and services.

* **+time** — display current time
* **+channel** — display name of channel
* **+pi** — display pi value
* **+note** — display notice
* **+tux** — draw Tux
* **+feed** — parse RSS or Atom feed items
* **+quit** — kill bot and exit from Python session
* **+rcn** — reconnect bot

## Customization

Variables you should change in `XDroid.py`:

* `server` (L16)
* `port` (L17)
* `channel` (L18)
* `nick` (L19)
* `url` (L65)

It would be nice to change welcome messages at L29.

To change range of feed items for parse, change `n` in `range(1, n)` at L66.

### Adding a new command

Adding new command isn't hard. The best solution is to append your commands to
the file's end, with consistent ident. Command syntax:

```python
  if msg.find("+command_name") != -1:
    do_something()
```

## Author

**Zlatan Vasović**

* <https://twitter.com/zdr0id>
* <https://github.com/ZDroid>