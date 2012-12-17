Recessify
=======

A simple plugin for Sublime Text 2 that cleans your CSS/LESS files using Twitter's [RECESS](https://github.com/twitter/recess) tool written by [Jacob Thornton](https://twitter.com/fat).

Requires Node.js, currently only supports Windows (feel free to contribute OSX/Linux support)

**Installation**

1. Install RECESS

  `npm install recess -g`

2. Install Recessify

  `git clone git://github.com/tcrosen/recessify.git %APPDATA%/Sublime\ Text\ 2/Packages/Recessify`

3. Add a keybinding to call the plugin in *Preferences -> Key Bindings -> User*

  `{ "keys": ["ctrl+k", "ctrl+d"], "command": "recessify" }`