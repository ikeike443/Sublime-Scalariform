# Sublime Scalariform plugin

This is a plugin for the [Sublime Text 2](http://www.sublimetext.com/) text
editor that allows you to format scala source code using [Scalariform](https://github.com/mdr/scalariform) [command line tool](https://github.com/mdr/scalariform/wiki/Command-line-tool).


## Prerequisite

* Ensure java command available on your computer

* Relaxedness to wait for the seconds until code formatting completed


## Installation

**The easiest way to install is via the** [**Sublime Package Control**](http://wbond.net/sublime_packages/package_control) **plugin.**
Just open "Package Control: Install Package" in your Command Palette and search for
"Sublime-Scalariform" (or, if you already have it installed, select "Package Control: Upgrade Package"
to upgrade).

To install it manually in a shell/Terminal (on OS X, Linux or Cygwin), via git:

    cd ~/"Library/Application Support/Sublime Text 2/Packages/" # location on OS X; will be different on Linux & Windows
    git clone https://github.com/ikeike443/Sublime-Scalariform.git

The plugin should be picked up automatically. If not, restart Sublime Text.


## Usage

Just type the short cut key below and wait for seconds.

    ctrl + alt + l     //Linux and Windows
    command + alt + l //OSX

Then, you can see the formatted code.


You can also access this functionality via main menu and context menu.

    Tools > Scalariform > format  // main menu
    Scalariform > format           // context menu


## Settings & Key Bindings

You can customize the formatting behavior via `Preferences > Package Settings > Scalariform > Settings - Default (or Settings - User)`.

```
{
  "formatting" :
    {
      "encoding" : "UTF-8"
      "alignParameters" : false
      "alignSingleLineCaseStatements" : false
      "alignSingleLineCaseStatements.maxArrowIndent" : 40
      "compactControlReadability" : false
      "compactStringConcatenation" : false
      "doubleIndentClassDeclaration" : false
      "formatXml" : true
      "indentLocalDefs" : false
      "indentPackageBlocks" : true
      "indentSpaces" : 2
      "indentWithTabs" : false
      "multilineScaladocCommentsStartOnFirstLine" : false
      "preserveDanglingCloseParenthesis" : false
      "placeScaladocAsterisksBeneathSecondAsterisk" : false
      "preserveSpaceBeforeArguments" : false
      "rewriteArrowSymbols" : false
      "spaceBeforeColon" : false
      "spaceInsideBrackets" : false
      "spaceInsideParentheses" : false
      "spacesWithinPatternBinders" : true
    }
}
```

These settings are compatible to [those command line options](https://github.com/mdr/scalariform/wiki/Command-line-tool).


You can also customize the key bindings via `Preferences > Package Settings > Scalariform > Key Bindings - Default (or Key Bindings - User)`.


## Bugs and Feature Requests

<https://github.com/ikeike443/sublime-Scalariform/issues>


## License

MIT License
