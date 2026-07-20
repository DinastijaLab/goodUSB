# goodUSB

This project turns a CircuitPython-compatible microcontroller (like a Raspberry Pi Pico or Adafruit board) into an automated keystroke injector (BadUSB). When plugged into a fresh Windows machine, it automatically launches PowerShell, pulls down a public powershell setup, and runs a software installation script using Windows Package Manager (winget).

## ✨ Features
- The physical device only executes a single command line, the bulk of the installation logic runs directly from a [PowerShell setup file](./payload.ps1) in the offical repo.
- The physical device waits for the user to press **caps lock** to confirm that the powershell terminal has opended.

## 🛠️ Hardware Requirements
- Any microcontroller running **CircuitPython 10.x+**.

## 📖 Deployment & Customization
- Modify the Payload: Update the target setup URL link in `settings.toml` *(PAYLOAD_URL)* with your own script URL.
- Copy: Copy `boot.py`, `code.py`, `settings.toml`, and ***adafruit_hid/ folder into the lib/ folder*** directly onto your microcontroller's storage drive.
- You can also add `payload.ps1` to the root folder and use it by setting `"ONLINE_MODE"` to `0`.