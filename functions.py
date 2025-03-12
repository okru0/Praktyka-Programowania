
def Add(num):
    if num == "":
        return 0

    if num.find(",\n") != -1 or num.find("\n,") != -1:
        raise -1

    num = num.replace("\n", ",")

    if num.startswith(',') or num.endswith(','):
        return -1

    return sum(map(int, num.split(",")))

