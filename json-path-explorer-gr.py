#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
json-path-explorer.py

Περιγραφή:
  Το πρόγραμμα διαβάζει ένα αρχείο JSON (data.json) και παρουσιάζει εποπτικά τη δομή του, όσο περίπλοκη και αν είναι (με φωλιασμένες λίστες και λεξικά), χρησιμοποιώντας αναδρομική συνάρτηση.
  Επίσης, για κάθε τιμή δημιουργείται το path που πρέπει να χρησιμοποιηθεί σε περιβάλλον Python  για την πρόσβαση σε αυτήν.

Input:
  Το αρχείο 'data.json' πρέπει να βρίσκεται στον ίδιο φάκελο με το script και να περιέχει έγκυρα δεδομένα JSON.

Output:
  Εμφανίζει τη δομή του JSON στον τερματικό με κατάλληλο indentation, ενδείξεις τύπων δεδομένων και το path πρόσβασης σε κάθε τιμή.

Συντάκτης: Βασίλειος Μπέλλης 
Ημερομηνία: 23/06/2025

Απαιτήσεις:
  Python 3.x
"""

import json


def analyze_content(data, path_str="data", level=0, output=None):
    """
    Αναλύει αναδρομικά τη δομή ενός αντικειμένου JSON και δημιουργεί αναφορά με indent.
    Επίσης, δημιουργεί για κάθε τιμή το path που μπορεί να χρησιμοποιηθεί σε περιβάλλον Python για την πρόσβαση σε αυτήν.

    Args:
        data: Τα δεδομένα JSON (dict, list ή απλή τιμή)
        path_str: Το path πρόσβασης σε κάθε τιμή
        level: Το επίπεδο βάθους για indent
        output: Λίστα στην οποία προστίθεται η ανάλυση (προαιρετική)

    Returns:
        output (list): Λίστα γραμμών με τη δομή των δεδομένων και το path πρόσβασης σε κάθε τιμή
    """
    output = output or []
    indent = "  " * level

    if isinstance(data, dict):
        output.append(f"{indent}Λεξικό:")
        for key, value in data.items():
            output.append(f"{indent}  Κλειδί: '{key}'")
            new_path = f"{path_str}['{key}']"
            analyze_content(value, new_path, level + 1, output)

    elif isinstance(data, list):
        output.append(f"{indent}Λίστα:")
        for index, item in enumerate(data):
            output.append(f"{indent}  Στοιχείο #{index + 1}:")
            new_path = f"{path_str}[{index}]"
            analyze_content(item, new_path, level + 1, output)

    else:
        output.append(f"{indent}Απλή τιμή: {repr(data)}")
        output.append(f"{indent}path: {path_str}")
    return output


def main():
    """
    Κεντρική συνάρτηση που διαβάζει το αρχείο και καλεί την analyze_content.
    """
    try:
        with open("data.json", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Σφάλμα: Το αρχείο 'data.json' δεν βρέθηκε.")
        return
    except json.JSONDecodeError as e:
        print(f"Σφάλμα: Το αρχείο δεν περιέχει έγκυρα JSON δεδομένα. ({e})")
        return

    result = analyze_content(data)

    # Εμφάνιση στον τερματικό
    for line in result:
        print(line)

    # Επιλογή αποθήκευσης σε αρχείο
    save_choice = input("\nΘέλεις να αποθηκευτεί το αποτέλεσμα σε αρχείο (Ν/Ο); ").strip().lower()
    if save_choice == "ν":
        with open("structure_output.txt", "w", encoding="utf-8") as out_file:
            out_file.write("\n".join(result))
        print("Η δομή αποθηκεύτηκε στο 'structure_output.txt'.")


if __name__ == "__main__":
    main()
