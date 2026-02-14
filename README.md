# Offline AI Writing Assistant

A lightweight, system-wide writing assistant that corrects grammar, typos, casing, and punctuation using a local LLM through Ollama. It runs fully offline and is suitable for low-resource machines.

## Highlights

- Works across apps: Notepad, VS Code, browser text boxes, mail, docs, and chat apps
- Preserves line breaks while correcting text
- Global hotkeys:
- `F9`: fix current line
- `F10`: fix selected text
- Fully offline after model setup
- Runs on CPU-only systems

## Tech Stack

- Python `3.10+`
- [Ollama](https://ollama.com)
- Local model (for example, `phi3` or your configured model in `main.py`)
- `httpx` for local API calls
- `pynput` for global keyboard hooks
- `pyperclip` for clipboard flow

## How It Works

1. You trigger a hotkey.
2. The assistant copies the current selection (or line) to clipboard.
3. Text is sent to your local Ollama endpoint.
4. Corrected text is placed back and pasted over the original text.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/offline-ai-writing-assistant.git
cd offline-ai-writing-assistant
```

### 2. Create and activate a virtual environment

Windows (`cmd`):

```bat
python -m venv venv
venv\Scripts\activate.bat
```

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Ollama and pull model

```bash
ollama pull phi3
```

Make sure Ollama is running before launching the app.

### 5. Run the assistant

```bash
python main.py
```

## Usage

- Select text, then press `F10` to fix selection.
- Place cursor on a line, then press `F9` to fix current line.
- Press `Esc` to stop the listener.

If your laptop maps `F9/F10` to system actions, use `Fn+F9/F10` or enable Fn Lock.

## Build Windows Executable (Optional)

```bat
python -m PyInstaller --onefile --noconsole main.py
```

Output:

- `dist\main.exe`

## Configuration Notes

- Update model name in `main.py` if you use a different Ollama model.
- Default endpoint is `http://localhost:11434/api/generate`.
- If `F9/F10` conflict with hardware shortcuts, switch to custom combos like `Ctrl+Alt+H` and `Ctrl+Alt+I`.

## Troubleshooting

- `ModuleNotFoundError`: install dependencies with `pip install -r requirements.txt`
- `pyinstaller not recognized`: use `python -m PyInstaller ...`
- Hotkeys not triggering: run terminal as normal user and test with `Fn` key behavior

## License

Add your preferred license in this section (for example, MIT).

Acknowledgements

This project is inspired by [patrickloeber/ai-typing-assistant](https://github.com/patrickloeber/ai-typing-assistant).
