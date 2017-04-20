from Prac07.programmingLanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # print(ruby)
    languages = [ruby, python, vb]
    # for language in languages:
    #     print(language)

    for language in languages:
        print("The dynamically typed languages are:")
        if language.is_dynamic():
            print(language.name)

main()
