# XDroid

**XDroid** is the most stupid IRC bot. He uses
[feedparser](http://code.google.com/p/feedparser/).

Licensed under the terms of MIT license.

## Usage

```bash
$ ./XDroid.py
```

Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to kill bot.

## Functions

All function names start with `+` to avoid conflicts with other IRC bots and
services.

* **+hi** — just say *Hi!*
* **+time** — display current time
* **+channel** — display name of channel
* **+pi** — print pi value
* **+note** — throw off notice
* **+tux** — draw Tux
* **+feed** — parse an Atom or RSS feed
* **+quit** — kill the bot and exit from Python session
* **+rcn** — reconnect the bot

## Customization

Variables you should change in `XDroid.py`:

* `server` (L15)
* `channel` (L16)
* `nick` (L17)
* `url` (L63)

To change range of parsed feed items, change `n` in `range(1, n)` at L64.

## Author

**Zlatan Vasović**

* https://twitter.com/zdr0id
* https://github.com/ZDroid