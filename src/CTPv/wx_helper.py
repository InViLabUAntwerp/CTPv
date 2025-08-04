# src/CTPv/wx_helper.py
import platform
import subprocess
import sys
import importlib


def ensure_wxpython():
    try:
        import wx
        return True
    except ImportError:
        print("wxPython not found. Attempting to install...")

    system = platform.system().lower()

    if system == "linux":
        ubuntu_version = get_ubuntu_version()
        if ubuntu_version:
            url = f"https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-{ubuntu_version}"
            try:
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", "-U",
                    "-f", url,
                    "wxPython"
                ])
                print("wxPython installed successfully.")
                return True
            except subprocess.CalledProcessError:
                print(f"Failed to install wxPython from {url}")
                suggest_manual_install()
                return False
        else:
            print("Could not detect Ubuntu version.")
            suggest_manual_install()
            return False

    elif system in ["windows", "darwin"]:
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-U", "wxPython"
            ])
            print("wxPython installed successfully.")
            return True
        except subprocess.CalledProcessError:
            print("Failed to install wxPython via pip.")
            suggest_manual_install()
            return False
    else:
        print(f"Unsupported OS: {system}")
        suggest_manual_install()
        return False


def get_ubuntu_version():
    try:
        with open('/etc/os-release') as f:
            for line in f:
                if line.startswith("VERSION_ID"):
                    return line.split("=")[1].strip().strip('"')
    except Exception:
        pass
    return None


def suggest_manual_install():
    system = platform.system().lower()
    if system == "linux":
        print("Please install wxPython manually using:")
        print("  pip install -U -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-20.04 wxPython")
        print("Replace 'ubuntu-20.04' with your version if needed.")
    else:
        print("Please run: pip install -U wxPython")


# Optional: auto-run on import
if __name__ == "__main__":
    ensure_wxpython()