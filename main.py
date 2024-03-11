import gifos

def clear(t, row, count):
    t.toggle_show_cursor(False)
    t.gen_prompt(row, count=count)
    t.toggle_show_cursor(True)
    t.gen_typing_text("clear", row, contin=True)
    t.clear_frame()

def command(t, row, count, name, output):
    t.toggle_show_cursor(False)
    t.gen_prompt(row, count=count)
    t.toggle_show_cursor(True)
    t.gen_typing_text(f"{name}.md", 1, contin=True)
    t.clone_frame(5)
    t.gen_text(output, row, count=1, contin=True)

def main():
    FONT="./fonts/gohufont-uni-14.pil"

    t = gifos.Terminal(750, 500, 15, 15, FONT, 15)
    gifos.Terminal.set_prompt(t, "\x1b[32mthomas@pompu \x1b[90m$ \x1b[0m")
    t.set_fps(15)

    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)

    t.gen_typing_text("Initializing GitHub README", 1, contin=True)
    t.clone_frame(5)
    t.gen_typing_text("...", 1, contin=True)
    t.clone_frame(5)
    t.clear_frame()

    t.gen_text("\x1b[93mREADME OS v2.24.3\x1b[0m", 1, count=5)
    t.clone_frame(2)

    t.gen_text("login: ", 3, count=5)

    t.toggle_show_cursor(True)
    t.gen_typing_text("thomas", 3, contin=True)

    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)

    t.toggle_show_cursor(True)
    t.gen_typing_text("************", 4, contin=True)

    t.toggle_show_cursor(False)
    t.gen_text("\x1b[32mWelcome to my profile :)\x1b[0m", 6, count=15)
    t.clear_frame()

    command(t, row=1, count=10, name="info", output=f"""
\x1b[30m\x1b[44mInfo\x1b[0m
\x1b[34mOS:     \x1b[37mManjaro Linux, Windows 11\x1b[0m
\x1b[34mHost:   \x1b[37mFacultad de Ingenieria de la Universidad de Buenos Aires \x1b[94m#FIUBA\x1b[0m
\x1b[34mKernel: \x1b[37mComputer Engineering \x1b[94m#CE\x1b[0m
\x1b[34mUptime: \x1b[37m20 years\x1b[0m
\x1b[34mIDE:    \x1b[37mVSCode, Android Studio\x1b[0m
""")

    clear(t, row=9, count=120)

    command(t, row=1, count=10, name="facts", output=f"""
\x1b[30m\x1b[44mFacts about me:\x1b[0m
\x1b[34mHobbies:  \x1b[37mAstronomy, Programming and Gaming\x1b[0m
\x1b[34mFav languages:  \x1b[37mPython, Kotlin\x1b[0m
\x1b[34mCurrently learning:  \x1b[37mAndroid and Web developing\x1b[0m
\x1b[34mFriends call me '\x1b[37mtho\x1b[34m'\x1b[0m
""")

#    clear(t, row=8, count=120)
#
#    command(t, row=1, count=10, name="contact", output=f"""
#\x1b[30m\x1b[44mContact:\x1b[0m
#\x1b[34mEmail:      \x1b[37mthomasjcabovianco@gmail.com\x1b[0m
#\x1b[34mLinkedIn:   \x1b[37mSoon...\x1b[0m
#""")

    # reboot
    # Note: row=6 if the 'contact' command is executed
    t.toggle_show_cursor(False)
    t.gen_prompt(8, count=120)
    t.toggle_show_cursor(True)
    t.gen_typing_text("reboot", 8, contin=True)
    t.clone_frame(5)

    t.gen_gif()

if __name__ == "__main__":
    main()

# Special thanks to https://github.com/x0rzavi
# Gif generated using https://github.com/x0rzavi/github-readme-terminal
