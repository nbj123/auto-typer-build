import pyautogui
from pynput import keyboard

# 运行后让用户输入自定义内容
print("=== 请输入你想自动输入的内容：")
CUSTOM_TEXT = input("> ")
is_typing = False

def on_press(key):
    global is_typing
    if is_typing:
        return
    try:
        # 改为按 F3 触发
        if key == keyboard.Key.f3:
            is_typing = True
            pyautogui.write(CUSTOM_TEXT)
    finally:
        is_typing = False

def on_release(key):
    # ESC 退出程序
    if key == keyboard.Key.esc:
        print("\nESC 退出程序")
        return False

print(f"\n✅ 已设置：按 F3 自动输入 → {CUSTOM_TEXT}")
print("❌ 按 ESC 退出程序\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
