# XDroid

**XDroid** is the most stupid IRC bot. He uses
[feedparser](http://code.google.com/p/feedparser/).

Licensed under the terms of MIT license.

## Usage

```bash
$ ./XDroid.py
```

Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to kill bot.

## Commands

All commands start with `+` to avoid conflicts with other IRC bots and
services.

* **+hi** — say *Hi!*
* **+time** — display current time
* **+channel** — display name of channel
* **+pi** — print pi value
* **+note** — display notice
* **+tux** — draw Tux
* **+feed** — display Atom or RSS feed items
* **+quit** — kill bot and exit from Python session
* **+rcn** — reconnect bot

## Customization

Variables you should change in `XDroid.py`:

* `server` (L15)
* `channel` (L16)
* `nick` (L17)
* `url` (L63)

To change range of parsed feed items, edit `n` in `range(1, n)` at L64.

Don't change L35 and L36 because of they aren't for any command, they are for
ping replies.

## Author

**Zlatan Vasović**

* [https://twitter.com/zdr0id](https://twitter.com/zdr0id)
* [https://github.com/ZDroid](https://github.com/ZDroid)