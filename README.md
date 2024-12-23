# Snow Animation in Terminal - "Za Rączkę" Christmas Challenge

## Description

This project is a simple Python script that generates a snow animation in the terminal. It uses Unicode characters to represent snowflakes that fall randomly across the screen, creating a wintery scene.

**WARNING**: Run this code only on Linux, as Unicode character display does not work correctly on Windows.

## Demo

Watch the snow animation in action on [YouTube](https://youtu.be/zv-8ctvnOHI).

## Requirements

- Python 3.x
- Linux operating system
- Terminal that supports Unicode characters

## Installation

1. **Download the Script**

   You can download the script directly or clone the repository if it's available.

   ```bash
   git clone https://gitlab.com/MarcinCichy/snowflakes.git
    ```
## Usage
1. Run the Script

    Ensure you have execute permissions for the script. You can set the permissions using the following command:

    ```bash
    chmod +x snow_animation.py
    ```
    Then, run the script:

    ```bash
    python3 snow_animation.py
    ```

2. Stop the Animation

    To stop the animation, press Ctrl + C in the terminal.

## How It Works
- **Snowflake Generation**: The script randomly generates snowflakes at the top of the screen.
- **Snowflake Movement**: Snowflakes move downward at varying speeds and may slightly shift left or right.
- **Screen Refreshing**: The screen is regularly cleared and redrawn to create a smooth animation effect.

## Notes
- **Compatibility**: The script is optimized to run on Linux systems. Displaying Unicode characters on Windows may be problematic, even after setting the appropriate code page.
- **Customization**: You can adjust SCREEN_WIDTH and SCREEN_HEIGHT to fit the size of your terminal.
- **Unicode Characters**: The list of available snowflake characters is stored in the SHAPES variable. You can add or change characters according to your preferences.








