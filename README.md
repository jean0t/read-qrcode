# 📸 Read QR Code from Screen

A Python tool to capture a selected area of the screen and read QR codes using OpenCV. Perfect for quickly extracting QR code data from images! 🚀 
***
Reason why I created this tool:  
I use [pass](https://www.passwordstore.org/) as my password manager and sometimes I need to take screenshots and read qr codes to get the otp to the 2 factors authentication, of course it isnt difficult to take a screenshot and use `zbarimg` to read the contents, but making it all in one command is easier and faster.  

## Dependencies

Wayland:  
    - `flameshot`

## 📥 Installation

Ensure you have Python 3.11.2+ installed, then run:  

```bash
pipx install ./*.whl
```

Or, if installing from source:

```bash
git clone https://github.com/jean0t/read-qrcode.git
cd read-qrcode
pip install .
```

## 🛠 Usage

### 📌 Running from Terminal

Simply run the following command to select an area and extract QR code data:

```bash
read-qrcode
```

If a QR code is detected, the extracted information will be printed.

### ⚡ Quick Access via Keyboard Shortcut

For a faster workflow, you can bind `read-qrcode` to a keyboard shortcut and automatically copy the output to your clipboard. Example for Wayland users with `wl-copy`:

1. Add this shortcut command:
   ```bash
   read-qrcode | wl-copy
   ```
2. Now, pressing your custom shortcut will immediately copy the QR code content!

## 🤝 Contributing

Forks and contributions are welcome! Feel free to open an issue or submit a pull request. Let's improve this tool together! 🚀

## 📜 License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️  by Jean0t
