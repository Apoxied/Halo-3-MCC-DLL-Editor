# Halo 3 DLL Editor

Easily edit your halo3.dll file with easy to use checkbox options.

- Select your halo3.dll file
- Select what features you desire to have
- ✨Magic ✨

![alt text](https://imgur.com/l1k9PA9.png)

## Features

- I have it searching for the array of bytes, versus the offset, which has been able to successfully find pretty much all options on older seasons. It should be able to withstand future MCC updates without completely breaking. Most of the options, if not all, should stay intact.

- It can detect if you have certain modifications already applied upon opening, which will automatically check the boxes.
- Auto detects offset information.
- You can deselect boxes to restore the original values.
- "Clean DLL" button that deselects all options and restores your dll.
- Detects which version of the game the dll belongs to and will disable the options not available for previous updates.
- Detects if MCC is open, and will prevent you from opening the dll.
- I have it handling the messages to the user at the top. Each message lasts 3 seconds long and disappears, letting the user know if the button worked or not. If there's an error, I have it displaying the error where the problematic array is located so I can fix things more easily.
- Disallows the user from opening a file that's not named "halo3.dll" to prevent people from accidentally changing different dlls.
- "Note" button included that taks you to a mega folder containing DLL offset information.

## How it Works
H3 DLL Editor works by searching for the AOB (Array of Bytes) associated with the needed change. It recognizes patterns in your halo3.dll file and is able to make automatic changes upon checking a box. It's also able to reverse changes when unchecking a box. When initially opening a dll file inside the program, it will automatically scan for changes in the dll and check boxes on modifications already existent on your dll file.

> I know nothing about reverse enginerring.
> I wanted to create a program that makes these 
> changes easier for the general public. I want to
> thank PunctualAlex for a majority of the options.

## Installation

[H3 DLL Editor](https://github.com/Apoxied/Halo-3-DLL-Editor/releases/tag/Halo) is a standalone exe. It might register as a false postive on your anti-virus. Do not download unless you're willing to make exceptions to your anti virus software.

If you're downloading the [source code](https://github.com/Apoxied/Halo-3-DLL-Editor/blob/master/main.py), it requires [Python](https://www.python.org/downloads/) v3.11+ to run.

Install the dependencies:

```sh
pip install psutil
pip install win32api
pip install tkinter
pip install pypiwin32
```

## Development

Want to contribute? Great!

Feel free to download the [source code](https://github.com/Apoxied/Halo-3-DLL-Editor/blob/master/main.py).

Or, you're more than welcome to send me offset information and byte changes to Apoxied#1337 via Discord.


## License

MIT

**Free Software, Hell Yeah!**
