# smulepy

[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/mit-license.php) [![Python](https://img.shields.io/badge/Written%20in-Python%203-blue.svg)](https://www.python.org/)

Re-implementation of `smulerb` in Python 3.

## How to use
0. Assuming you have Python SDK installed in your machine.
1. Clone or download this repo.
2. Extract the files to wherever you want, and change current directory to the directory where `smule.py` was extracted.
3. Run `pip3 install -r requirements.txt`.
4. Make the `smule.py` file executable by using `chmod a+x`.
5. Download a song or video from Smule by using the following command on Terminal.
```
./smule.py <link to smule collab>
```
e.g.
```
./smule.py https://www.smule.com/recording/shimo-kumikyoku-nico-nico-douga/519002350_1591579869
```
5. The file will be downloaded at the same location where `smule.py` is placed.

## Checklists

- [x] Accept link arguments from terminal.
- [ ] Add exceptions.
- [ ] Add progress bar during file download.
- [ ] Add ability to change default download location.

