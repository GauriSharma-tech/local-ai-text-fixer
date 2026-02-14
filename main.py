import time
from string import Template

import httpx
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip


controller = Controller()

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {
    "model": "phi3",
    "keep_alive": "5m",
    "stream": False,
    "options": {
        "temperature": 0.2,
        "num_ctx": 2048
    }
}

PROMPT_TEMPLATE = Template(
    """Fix spelling mistakes, typos, grammar, and punctuation.
Preserve all line breaks.
Do not explain anything.
Return only corrected text.

$text"""
)


def fix_text(text):
    prompt = PROMPT_TEMPLATE.substitute(text=text)

    try:
        response = httpx.post(
            OLLAMA_ENDPOINT,
            json={"prompt": prompt, **OLLAMA_CONFIG},
            headers={"Content-Type": "application/json"},
            timeout=120,
        )
    except httpx.ReadTimeout:
        print("Model took too long to respond.")
        return None
    except Exception as e:
        print("Error:", e)
        return None

    if response.status_code != 200:
        print("Error", response.status_code)
        return None

    return response.json()["response"].strip()



def fix_current_line():
    # Windows: select from cursor to start of line (Shift + Home)
    controller.press(Key.shift)
    controller.press(Key.home)

    controller.release(Key.home)
    controller.release(Key.shift)

    fix_selection()


def fix_selection():
    # 1. Copy selection to clipboard (Ctrl + C)
    with controller.pressed(Key.ctrl):
        controller.tap("c")

    # 2. Get the clipboard string
    time.sleep(0.1)
    text = pyperclip.paste()

    # 3. Fix string
    if not text:
        return
    fixed_text = fix_text(text)
    if not fixed_text:
        return

    # 4. Paste the fixed string to the clipboard
    pyperclip.copy(fixed_text)
    time.sleep(0.1)

    # 5. Paste clipboard and replace selected text (Ctrl + V)
    with controller.pressed(Key.ctrl):
        controller.tap("v")


def on_press(key):
    if key == Key.f9:
        fix_current_line()
    elif key == Key.f10:
        fix_selection()
    elif key == Key.esc:
        return False  # stop listener


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
