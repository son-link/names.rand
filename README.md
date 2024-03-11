# Names.rand
![GitHub License](https://img.shields.io/github/license/son-link/names.rand)
![GitHub Repo stars](https://img.shields.io/github/stars/son-link/names.rand)
[![Build status](https://ci.appveyor.com/api/projects/status/vua95l4w1jwtwkmy?svg=true)](https://ci.appveyor.com/project/son-link/names-rand)
![GitHub release (with filter)](https://img.shields.io/github/v/release/son-link/names.rand)
![](https://img.shields.io/github/downloads/son-link/names.rand/total)

![Screenshot](screenshot.png)

Generates names for various fantasy races, and, in the future, names in different languages.

Available for Linux, Windows and Mac OS. In the future it will also be available for Android and as PWA (Progressive Web App).

Under the GNU/GPLv3 or newer license.

Make with :heart:, [Python](https://www.python.org/) and [Flet](https://flet.dev)

&copy; 2024 Alfonso Saavedra "Son Link"

## Available generators:

### Fantasy races:

* Demons
* Dragons
* Drows / Dark elfs
* Dwarven
* Elfs
* Gnomes
* Halflings
* Orcs

### Languages:

* Chinese
* English
* French
* Germany
* Italian
* Muslim
* Portuguese
* Russian
* Spanish

## How to use

#### Executables

To make it work just download the zip for your operating system, give run permissions (only necessary for the GNU/Linux executable) and double click on it.

#### From source

This requires Python version 3.x (recommended minimum 3.8), as well as the package flet

```sh
python3 main.py
```

#### Binaries

You can download executables for Windows, Linux and Mac OS from [release page](https://github.com/son-link/names.rand/releases)


On GNU/Linux, since flet 0.20.0 you need to have mpv installed.

On **Ubuntu 22.04** and earlier:

`apt install libmpv1`

On other distributions, such as Arch Linux, follow these 2 steps:

* Install the mpv package
* Create a symbolic link to the library: `ln /usr/lib/libmpv.so.2 /usr/lib/libmpv.so.1` (The path may vary depending on the distribution).