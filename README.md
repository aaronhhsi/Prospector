# Prospector Macro Controller

A modern, GUI-based macro automation tool for mining/prospecting activities with precise timing controls and real-time mouse hold duration tracking.

## Features

- **Modern Dark Theme GUI** - Professional interface with intuitive controls
- **Configurable Settings** - Customize digs, sift time, cycles, and timing
- **Real-time Mouse Tracking** - Displays actual mouse hold duration
- **Keyboard Shortcuts** - Quick access via hotkeys
- **Always-on-Top Window** - Stays visible while working with other applications
- **Safe Stop Mechanisms** - Multiple ways to stop the macro instantly

## Prerequisites

### Installing Python

#### Windows:
1. Visit [python.org](https://www.python.org/downloads/)
2. Download Python 3.8 or newer (recommended: latest stable version)
3. **Important**: During installation, check "Add Python to PATH"
4. Run the installer and follow the setup wizard
5. Verify installation by opening Command Prompt and typing:
   ```cmd
   python --version
   ```

#### macOS:
**Option 1: Using Homebrew (Recommended)**
1. **Open Terminal**:
   - Press `Cmd + Space` to open Spotlight search
   - Type "Terminal" and press Enter
   - A black window will open where you can type commands

2. **Install Homebrew** (if you don't have it):
   - Homebrew does NOT come pre-installed on Mac
   - Copy and paste this command into Terminal and press Enter:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   - Follow the prompts and enter your Mac password when asked
   - This may take several minutes to complete

3. **Install Python using Homebrew**:
   - In the same Terminal window, type:
   ```bash
   brew install python
   ```

4. **Verify installation**:
   ```bash
   python3 --version
   ```

**Option 2: Direct Download**
1. Visit [python.org](https://www.python.org/downloads/)
2. Click "Download Python" (it will auto-detect macOS)
3. Open the downloaded .pkg file and follow the installer
4. **Verify installation**:
   - Open Terminal (Cmd + Space, type "Terminal")
   - Type: `python3 --version`

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

## Installation

### 1. Download the Application
- Download `prospector.py` to your desired folder
- Or clone this repository:
  ```bash
  git clone [repository-url]
  cd prospector
  ```

### 2. Install Required Dependencies
**Windows:**
- Open Command Prompt (Press `Windows + R`, type `cmd`, press Enter)
- Navigate to your project folder or run from anywhere:
```cmd
pip install pynput
```

**macOS:**
- Open Terminal (Press `Cmd + Space`, type "Terminal", press Enter)
- Run this command:
```bash
pip3 install pynput
```

**Linux:**
- Open Terminal (Ctrl + Alt + T)
- Run this command:
```bash
pip3 install pynput
```

**Note**: `tkinter` is included with most Python installations by default.

### 3. Platform-Specific Setup

#### Windows:
- No additional setup required
- The application should run directly

#### macOS:
- You may need to grant accessibility permissions for the app to control mouse/keyboard:
  1. Open **System Preferences** (Apple menu → System Preferences)
  2. Click **Security & Privacy**
  3. Click the **Privacy** tab
  4. Select **Accessibility** from the left sidebar
  5. Click the lock icon and enter your password
  6. Click the **+** button and add **Terminal** or **Python**
  7. Make sure the checkbox next to it is checked

#### Linux:
- Install tkinter if not included:
  ```bash
  sudo apt install python3-tk
  ```

## Usage

### Running the Application

**Windows:**
1. Open Command Prompt (Windows + R, type `cmd`, press Enter)
2. Navigate to the folder containing `prospector.py`:
   ```cmd
   cd "C:\path\to\your\prospector\folder"
   ```
3. Run the application:
   ```cmd
   python prospector.py
   ```

**macOS:**
1. Open Terminal (Cmd + Space, type "Terminal", press Enter)
2. Navigate to the folder containing `prospector.py`:
   ```bash
   cd /path/to/your/prospector/folder
   ```
   (Tip: You can drag the folder from Finder into Terminal to auto-fill the path)
3. Run the application:
   ```bash
   python3 prospector.py
   ```

**Linux:**
1. Open Terminal (Ctrl + Alt + T)
2. Navigate to the folder containing `prospector.py`:
   ```bash
   cd /path/to/your/prospector/folder
   ```
3. Run the application:
   ```bash
   python3 prospector.py
   ```

### GUI Controls

#### Configuration Panel:
- **Digs Until Full**: Number of dig cycles before sifting (1-10)
- **Seconds to Sift**: Duration to hold mouse for sifting (1-20)
- **Number of Cycles**: Total macro cycles to execute (1-100)
- **Base Sleep Time**: Base timing for dig operations in seconds (0.1-2.0)

#### Mouse Hold Timer:
- Displays the duration of your physical mouse clicks
- Useful for calibrating timing settings

#### Control Button:
- **START MACRO**: Begin the automation sequence
- **STOP MACRO**: Immediately halt all operations

### Keyboard Shortcuts

- **DELETE**: Toggle macro start/stop
- **LEFT ARROW**: Exit the application
- **Physical Mouse Hold**: Measure and display hold duration

### Macro Sequence

Each cycle performs the following actions:
1. Execute configured number of "digs" with randomized timing
2. Move forward (W key) briefly
3. Single click
4. Hold left mouse for sifting duration
5. Move backward (S key) briefly
6. Repeat for specified number of cycles

## Safety Features

- **Instant Stop**: Multiple ways to halt execution immediately
- **Background Monitoring**: Continuous checking for stop signals
- **Safe Threading**: Non-blocking execution with proper cleanup
- **Always Accessible**: GUI stays on top for quick access

## Troubleshooting

### Common Issues:

**"pynput not found"**
```bash
pip install --upgrade pynput
```

**"Permission denied" (macOS/Linux)**
- Grant accessibility permissions in system settings
- Run with appropriate privileges if needed

**"tkinter not found" (Linux)**
```bash
sudo apt install python3-tk
```

**Macro not responding**
- Press DELETE key to force stop
- Click STOP MACRO button
- Press LEFT ARROW to exit application

### Performance Tips:

- Close unnecessary applications for more consistent timing
- Test with small cycle counts first
- Use mouse hold timer to calibrate your settings
- Adjust base sleep time based on system performance

## System Requirements

- **Python**: 3.8 or newer
- **RAM**: 50MB minimum
- **OS**: Windows 10+, macOS 10.14+, or Linux with X11
- **Dependencies**: pynput, tkinter (usually pre-installed)

## License

This project is for educational and personal use only. Use responsibly and in accordance with the terms of service of any applications you use it with.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all dependencies are properly installed
3. Ensure you have necessary system permissions