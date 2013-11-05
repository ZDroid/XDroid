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

* **+hi** — say *Hi!*
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

* `server` (L15)
* `port` (L16)
* `channel` (L17)
* `nick` (L18)
* `url` (L64)

To change range of feed items for parse, change `n` in `range(1, n)` at L64.

Don't change L36 and L37 because of they're for ping replies.

## Author

**Zlatan Vasović**

* <https://twitter.com/zdr0id>
* <https://github.com/ZDroid>