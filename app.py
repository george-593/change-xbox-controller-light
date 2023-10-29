import sys, subprocess, pyuac


def exit():
    print("Usage: python app.py <light target [0-1]>")
    sys.exit(1)


def getTargetLight():
    if len(sys.argv) < 2:
        exit()

    try:
        target = float(sys.argv[1])
    except:
        exit()

    if target < 0 or target > 1:
        exit()

    return target


target = getTargetLight()

if not pyuac.isUserAdmin():
    print("Not running as admin. Restarting as admin...")
    pyuac.runAsAdmin()
else:
    print("Setting light to " + str(target))
    subprocess.run(
        ["setx", f"SDL_JOYSTICK_HIDAPI_XBOX_ONE_HOME_LED", str(target), "/M"]
    )
    """
    p = subprocess.Popen(
        ["setx", f"SDL_JOYSTICK_HIDAPI_XBOX_ONE_HOME_LED", str(target), "/M"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = p.communicate()
    print(out)
    """
    print("Changed light brightness, please reconnect the controller to apply changes.")
    # PYUAC restarts in a py shell that autocloses, so we need to wait for user input to keep the window open
    input("\nPress any key to exit...")
