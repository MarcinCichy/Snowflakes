# Snow Animation in Terminal - "Za Rączkę" Christmas Challenge

## Description

This project is a simple Python script that generates a snow animation in the terminal. It uses Unicode characters to represent snowflakes that fall randomly across the screen, creating a wintery scene.

WARNING: This code works best on Linux. On Windows, you may experience issues with Unicode display. To fix this, set the terminal font to "MS Gothic" and change the code page by running:

```bash
chcp 65001
```

## Demo

Watch the snow animation in action on [YouTube](https://youtu.be/yP63y9B1MLk).

## Requirements

- Python 3.x
- Linux or macOS operating system (Windows requires additional setup)
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
    chmod +x snowflakes.py
    ```
    Then, run the script:

    ```bash
    python3 snowflakes.py
    ```
2. Run the Snow Animation with banner
   An alternative script snowflakes_banner.py has been created to display a custom message in falling snow. For example, to display "HAPPY NEW YEAR":
   ```bash
   python3 snowflakes_banner.py
    ```
3. Stop the Animation

    To stop the animation, press Ctrl + C in the terminal.

## How It Works
- **Snowflake Generation**: The script randomly generates snowflakes at the top of the screen.
- **Snowflake Movement**: Snowflakes move downward at varying speeds and may slightly shift left or right.
- **Screen Refreshing**: The screen is regularly cleared and redrawn to create a smooth animation effect.
- **Custom Banner**: The snowflakes_banner.py script overlays a user-defined message within the snow animation, creating a festive banner effect.

## Notes
- **Compatibility**: The script is optimized to run on Linux systems. Displaying Unicode characters on Windows may be problematic, even after setting the appropriate code page.
- **Customization**: You can adjust SCREEN_WIDTH and SCREEN_HEIGHT to fit the size of your terminal.
- **Unicode Characters**: The list of available snowflake characters is stored in the SHAPES variable. You can add or change characters according to your preferences.
- **Custom Messages**: With snowflakes_banner.py, you can display personalized messages setup in code as TEXT.

## Windows Support (Optional)

1. Open CMD or PowerShell.

2. Set the terminal font to MS Gothic.

3. Run the following command to enable UTF-8 encoding:
``` bash
chcp 65001
```

4. Now, you can run the script without issues.








