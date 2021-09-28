#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    counter = 0
    values_num = []
    is_float = False
    if values is None:
        values = []
        while counter < 10:
            print("Entrez la valeur #", counter + 1)
            element = input()
            values.append(element)
            counter += 1
    try:
        float(values[0])
        is_float = True
    except ValueError:
        is_float = False

    if is_float:
        values_num = [float(element) for element in values]
        values_num.sort()
        print(values_num)
        return values_num
    else:
        values.sort()
        print(values)
        return values
        


def anagrams(words: list = None) -> bool:
    is_in_other = False
    all_letters = []
    if words is None:
        print("Entrez le premier mot:")
        mot1 = input()
        print("Entrez le deuxieme mot:")
        mot2 = input()
        words = [mot1, mot2]
    
    for letter in words[0]:
        is_in_other = False
        for letter1 in words[1]:
            if letter == letter1:
                is_in_other = True
                all_letters.append(is_in_other)
        if is_in_other == False:
            all_letters.append(False)
    
    if all(all_letters):
        print("C'est un anagram")
    else:
        print("Ce n'est pas un anagram")

    return False


def contains_doubles(items: list) -> bool:
    items = [2, 6, 3, 7, 8, 0]
    doublons = False
    for i, element in enumerate(items):
        for j, element1 in enumerate(items):
            if element == element1 and i != j:
                doublons = True
    
    if doublons:
        print("Elle a des doublons")
        return False
    else:
        print("Elle n'a pas de doublons")
        return True


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
