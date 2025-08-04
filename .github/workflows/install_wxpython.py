import platform
import subprocess
import sys

def install_wxpython():
    system = platform.system().lower()

    if system == 'linux':
        # Detect the Ubuntu version
        ubuntu_version = get_ubuntu_version()
        if ubuntu_version:
            url = f"https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-{ubuntu_version}"
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "-f", url, "wxPython"])
        else:
            print("Unsupported Linux distribution or unable to determine Ubuntu version.")
            sys.exit(1)
    elif system in ['windows', 'darwin']:  # 'darwin' is for macOS
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "wxPython"])
    else:
        print(f"Unsupported operating system: {system}")
        sys.exit(1)

def get_ubuntu_version():
    try:
        with open('/etc/os-release', 'r') as f:
            for line in f:
                if line.startswith('VERSION_ID'):
                    return line.split('=')[1].strip().strip('"')
    except FileNotFoundError:
        pass
    return None

if __name__ == "__main__":
    install_wxpython()
