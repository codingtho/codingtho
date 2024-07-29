import gifos

FONT="./fonts/gohufont-uni-14.pil"

def clear(t, row, count):
    t.toggle_show_cursor(False)
    t.gen_prompt(row, count=count)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[37mclear\x1b[0m", row, contin=True)
    t.clear_frame()

def command(t, row, count, command_name, output):
    t.toggle_show_cursor(False)
    t.gen_prompt(row, count=count)
    t.toggle_show_cursor(True)
    t.gen_typing_text(command_name, 1, contin=True)
    t.clone_frame(5)
    t.gen_text(output, row, count=1, contin=True)

def main():
    t = gifos.Terminal(750, 500, 15, 15, FONT, 15)
    gifos.Terminal.set_prompt(t, "\x1b[32mthomas \x1b[90m$ \x1b[0m")
    t.set_fps(20)

    command(t, row=1, count=10, command_name="profile --info", output=f"""
\x1b[34mName:\x1b[0m tho
\x1b[34mHost:\x1b[0m \x1b[37mEarth
\x1b[34mUptime:\x1b[0m 20 years
\x1b[34mAcademic Core:\x1b[0m Facultad de Ingenieria, Universidad de Buenos Aires \x1b[94m#FIUBA\x1b[0m
\x1b[34mKnowledge Node:\x1b[0m Computer Engineering \x1b[94m#CE\x1b[0m
""")
    
    clear(t, row=8, count=120)

    command(t, row=1, count=10, command_name="skills --list", output=f"""
\x1b[34mProgramming Languages:\x1b[0m
- Python
- Go
- Kotlin

\x1b[34mVersion Control:\x1b[0m
- Git
- GitHub

\x1b[34mFrameworks and Libraries:\x1b[0m
- Jetpack Compose
- Jetpack Navigation
- Retrofit
- Room
- Dagger Hilt
            
\x1b[34mTechnologies and Tools:\x1b[0m
- Kotlin Coroutines
- Flow
            
\x1b[34mArchitectures and Patterns:\x1b[0m
- MVVM Architecture
""")
    
    clear(t, row=25, count=220)

    # projects --featured

    command(t, row=1, count=10, command_name="learning --list", output=f"""
\x1b[34mLearning or want to learn:\x1b[0m
- SQL
- Preference Datastore
- WorkManager
- Firebase
- Testing
- Clean Architecture
- Design Patterns
- Algorithms and Data Structures
""")
    
    # contact --info

    t.toggle_show_cursor(False)
    t.gen_prompt(12, count=180)
    t.toggle_show_cursor(True)
    t.gen_typing_text("reboot", 12, contin=True)
    t.clone_frame(5)

    t.gen_gif()

if __name__ == "__main__":
    main()

# Special thanks to https://github.com/x0rzavi
# Gif generated using https://github.com/x0rzavi/github-readme-terminal
