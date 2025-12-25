import __main__

def _get_variable_from_notebook(var_name):
    """Hilfsfunktion, um eine Variable aus dem Hauptmodul (Notebook) zu holen."""
    if hasattr(__main__, var_name):
        return getattr(__main__, var_name)
    else:
        raise AttributeError(f"Variable '{var_name}' nicht im Notebook gefunden.")

def task_1_1():
    try:
        age = _get_variable_from_notebook('age')
        if isinstance(age, int):
            print(f"✅ Die Variable 'age' ist vom Typ int mit dem Wert: {age}")
        else:
            print(f"❌ Die Variable 'age' ist nicht vom Typ int, sondern vom Typ {type(age)}")

        size = _get_variable_from_notebook('size')
        if isinstance(size, float):
            print(f"✅ Die Variable 'size' ist vom Typ float mit dem Wert: {size}")
        else:
            print(f"❌ Die Variable 'size' ist nicht vom Typ float, sondern vom Typ {type(size)}")
        
        name = _get_variable_from_notebook('name')
        if isinstance(name, str):
            print(f"✅ Die Variable 'name' ist vom Typ str mit dem Wert: {name}")
        else:
            print(f"❌ Die Variable 'name' ist nicht vom Typ str, sondern vom Typ {type(name)}")

        is_student = _get_variable_from_notebook('is_student')
        if isinstance(is_student, bool):
            print(f"✅ Die Variable 'is_student' ist vom Typ bool mit dem Wert: {is_student}")
        else:
            print(f"❌ Die Variable 'is_student' ist nicht vom Typ bool, sondern vom Typ {type(is_student)}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_1_2():
    try:
        zeichenkette = _get_variable_from_notebook('zeichenkette')
        if isinstance(zeichenkette, str) and '\n' in zeichenkette:
            print("✅ Die Variable 'zeichenkette' ist ein mehrzeiliger String.")
        elif not isinstance(zeichenkette, str):
            print("❌ Die Variable 'zeichenkette' ist kein String.")
        elif '\n' not in zeichenkette:
            print("❌ Die Variable 'zeichenkette' ist nicht mehrzeilig. Bitte füge einen Zeilenumbruch ein")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_2_1():
    try:
        sum = _get_variable_from_notebook('sum')
        if sum == 42 + 17:
            print(f"✅ Die Variable 'sum' hat den korrekten Wert: {sum}")
        else:
            print(f"❌ Die Variable 'sum' hat den falschen Wert: {sum}. Erwartet wurde: {42 + 17}")

        quotient_float = _get_variable_from_notebook('quotient_float')
        if quotient_float == 100 / 7:
            print(f"✅ Die Variable 'quotient_float' hat den korrekten Wert: {quotient_float}")
        else:
            print(f"❌ Die Variable 'quotient_float' hat den falschen Wert: {quotient_float}. Erwartet wurde: {100 / 7}")

        quotient_int = _get_variable_from_notebook('quotient_int')
        if quotient_int == 100 // 7:
            print(f"✅ Die Variable 'quotient_int' hat den korrekten Wert: {quotient_int}")
        else:
            print(f"❌ Die Variable 'quotient_int' hat den falschen Wert: {quotient_int}. Erwartet wurde: {100 // 7}")

        remainder = _get_variable_from_notebook('remainder')
        if remainder == 100 % 7:
            print(f"✅ Die Variable 'remainder' hat den korrekten Wert: {remainder}")
        else:
            print(f"❌ Die Variable 'remainder' hat den falschen Wert: {remainder}. Erwartet wurde: {100 % 7}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_2_2():
    try:
        a = _get_variable_from_notebook('a')
        if a == 15:
            print(f"✅ Die Variable 'a' hat den korrekten Wert: {a}")
        else:
            print(f"❌ Die Variable 'a' hat den falschen Wert: {a}. Erwartet wurde: 15")

        b = _get_variable_from_notebook('b')
        if b == 10:
            print(f"✅ Die Variable 'b' hat den korrekten Wert: {b}")
        else:
            print(f"❌ Die Variable 'b' hat den falschen Wert: {b}. Erwartet wurde: 10")

        c = _get_variable_from_notebook('c')
        if c == 20:
            print(f"✅ Die Variable 'c' hat den korrekten Wert: {c}")
        else:
            print(f"❌ Die Variable 'c' hat den falschen Wert: {c}. Erwartet wurde: 20")

        d = _get_variable_from_notebook('d')
        if d == 5:
            print(f"✅ Die Variable 'd' hat den korrekten Wert: {d}")
        else:
            print(f"❌ Die Variable 'd' hat den falschen Wert: {d}. Erwartet wurde: 5")

        check1 = _get_variable_from_notebook('check1')
        if check1 == (a > b) and (a < c):
            print(f"✅ Die Variable 'check1' hat den korrekten Wert: {check1}")
        else:
            print(f"❌ Die Variable 'check1' hat den falschen Wert: {check1}. Erwartet wurde: {(a > b) and (a < c)}")
        check2 = _get_variable_from_notebook('check2')
        if check2 == (d >= b):
            print(f"✅ Die Variable 'check2' hat den korrekten Wert: {check2}")
        else:
            print(f"❌ Die Variable 'check2' hat den falschen Wert: {check2}. Erwartet wurde: {d >= b}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_3_1():
    try:
        days = _get_variable_from_notebook('days')
        if isinstance(days, list) and len(days) == 7 and ["Montag", "Dienstag", "Donnerstag", "Freitag", "Samstag", "Sonntag", "Feiertag"] == days:
            print(f"✅ Die Variable 'days' ist eine Liste mit der korrekten Länge von 7.")
        else:
            print(f"❌ Die Variable 'days' ist keine Liste mit der korrekten Länge von 7. Aktuelle Länge: {len(days) if isinstance(days, list) else 'N/A'}")

        first_and_last = _get_variable_from_notebook('first_and_last')
        if (isinstance(first_and_last, tuple) and len(first_and_last) == 2 and
            first_and_last[0] == "Montag" and first_and_last[1] == "Sonntag"):
            print(f"✅ Die Variable 'first_and_last' ist ein Tupel mit den korrekten Werten: {first_and_last}")
        else:
            print(f"❌ Die Variable 'first_and_last' ist kein Tupel mit den korrekten Werten. Aktueller Wert: {first_and_last}")
    except Exception as e:
        print(f"❌ Fehler: {e}")