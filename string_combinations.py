def combinations (inputStr, mapping):
    combinations = ['']
    if not inputStr:
        return []
    elif not mapping:
        return []
    else:
        pass

    for char in inputStr:
        letters = mapping[char]
        temporaryCombinations = []
        for combination in combinations:
            for letter in letters:
                temporaryCombinations.append(combination + letter)
        combinations = temporaryCombinations
    return combinations
