# Shakes and Fidget Bot for Debian

Welcome to the Shakes and Fidget Bot for Debian! This bot is an adaptation and improvement of the [MFBot](https://www.mfbot.de/en/) designed specifically to run on Debian systems. It automates various tasks in the game Shakes and Fidget, helping you progress more efficiently.

## Features

- Automates quests and battles
- Manages resources and inventory
- Handles guild tasks
- Customizable settings for different play styles
- Easy setup and maintenance

## Requirements

- Debian-based system (Debian, Ubuntu, etc.)
- Python 3.x
- Git

## Installation

1. **Update your system:**
    ```bash
    sudo apt update
    sudo apt upgrade
    ```

2. **Install Python 3 and Git:**
    ```bash
    sudo apt install python3 python3-pip git
    ```

3. **Clone the repository:**
    ```bash
    git clone https://github.com/karlogb/SFBot
    cd SFBot
    ```

4. **Install required Python packages:**
    ```bash
    pip3 install -r requirements.txt
    ```

5. **Configure the bot:**
    - Open `Acc.ini` file and fill in your game credentials and desired settings.

## Usage

To start the bot, simply run:
```bash
python3 bot.py
