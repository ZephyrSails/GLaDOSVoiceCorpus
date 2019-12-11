if __name__ == "__main__":
    with open("prompts_portal1.txt", "r") as prompts_portal1:
        with open("prompts_portal1_trim.txt", "w") as prompts_portal1_trim:
            for line in prompts_portal1.readlines():
                name, text = line.split("\t")
                text = text.strip()
                if text[0] == '"':
                    print(text)
                if text[0] == '"' and text[-1] == '"':

                    text = text[1:-1]
                prompts_portal1_trim.write("{}\t{}\n".format(name, text))
