import __main__
from typing import Tuple

results = {}

def _get_attribut_from_notebook(var_name):
    """Hilfsfunktion, um eine Variable aus dem Hauptmodul (Notebook) zu holen."""
    if hasattr(__main__, var_name):
        return getattr(__main__, var_name)
    else:
        raise AttributeError(f"Attribut '{var_name}' nicht im Notebook gefunden.")

def task_1_1():
    try:
        name = _get_attribut_from_notebook('name')
        out_str = f'### {name}, herzlich willkommen zum Einführungskurs Python! ###'
        print('\033[1m' + '#'*len(out_str) + '\033[0m')
        print('\033[1m' + out_str + '\033[0m')
        print('\033[1m' + '#'*len(out_str)+ '\033[0m')

        age = _get_attribut_from_notebook('age')
        if isinstance(age, int):
            print(f"✅ Die Variable 'age' ist vom Typ int mit dem Wert: {age}")
        else:
            print(f"❌ Die Variable 'age' ist nicht vom Typ int, sondern vom Typ {type(age)}")

        size = _get_attribut_from_notebook('size')
        if isinstance(size, float):
            print(f"✅ Die Variable 'size' ist vom Typ float mit dem Wert: {size}")
        else:
            print(f"❌ Die Variable 'size' ist nicht vom Typ float, sondern vom Typ {type(size)}")
        
        name = _get_attribut_from_notebook('name')
        if isinstance(name, str):
            print(f"✅ Die Variable 'name' ist vom Typ str mit dem Wert: {name}")
        else:
            print(f"❌ Die Variable 'name' ist nicht vom Typ str, sondern vom Typ {type(name)}")

        is_student = _get_attribut_from_notebook('is_student')
        if isinstance(is_student, bool):
            print(f"✅ Die Variable 'is_student' ist vom Typ bool mit dem Wert: {is_student}")
        else:
            print(f"❌ Die Variable 'is_student' ist nicht vom Typ bool, sondern vom Typ {type(is_student)}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_1_2():
    try:
        multiline_str = _get_attribut_from_notebook('multiline_str')
        if isinstance(multiline_str, str) and '\n' in multiline_str:
            print("✅ Die Variable 'multiline_str' ist ein mehrzeiliger String.")
        elif not isinstance(multiline_str, str):
            print("❌ Die Variable 'multiline_str' ist kein String.")
        elif '\n' not in multiline_str:
            print("❌ Die Variable 'multiline_str' ist nicht mehrzeilig. Bitte füge einen Zeilenumbruch ein")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_2_1():
    try:
        result_sum = _get_attribut_from_notebook('result_sum')
        if result_sum == 42 + 17:
            print(f"✅ Die Variable 'result_sum' hat den korrekten Wert: {result_sum}")
        else:
            print(f"❌ Die Variable 'result_sum' hat den falschen Wert: {result_sum}. Erwartet wurde: {42 + 17}")

        quotient_float = _get_attribut_from_notebook('quotient_float')
        if quotient_float == 100 / 7:
            print(f"✅ Die Variable 'quotient_float' hat den korrekten Wert: {quotient_float}")
        else:
            print(f"❌ Die Variable 'quotient_float' hat den falschen Wert: {quotient_float}. Erwartet wurde: {100 / 7}")

        quotient_int = _get_attribut_from_notebook('quotient_int')
        if quotient_int == 100 // 7:
            print(f"✅ Die Variable 'quotient_int' hat den korrekten Wert: {quotient_int}")
        else:
            print(f"❌ Die Variable 'quotient_int' hat den falschen Wert: {quotient_int}. Erwartet wurde: {100 // 7}")

        remainder = _get_attribut_from_notebook('remainder')
        if remainder == 100 % 7:
            print(f"✅ Die Variable 'remainder' hat den korrekten Wert: {remainder}")
        else:
            print(f"❌ Die Variable 'remainder' hat den falschen Wert: {remainder}. Erwartet wurde: {100 % 7}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_2_2():
    try:
        a = _get_attribut_from_notebook('a')
        if a == 15:
            print(f"✅ Die Variable 'a' hat den korrekten Wert: {a}")
        else:
            print(f"❌ Die Variable 'a' hat den falschen Wert: {a}. Erwartet wurde: 15")

        b = _get_attribut_from_notebook('b')
        if b == 10:
            print(f"✅ Die Variable 'b' hat den korrekten Wert: {b}")
        else:
            print(f"❌ Die Variable 'b' hat den falschen Wert: {b}. Erwartet wurde: 10")

        c = _get_attribut_from_notebook('c')
        if c == 20:
            print(f"✅ Die Variable 'c' hat den korrekten Wert: {c}")
        else:
            print(f"❌ Die Variable 'c' hat den falschen Wert: {c}. Erwartet wurde: 20")

        d = _get_attribut_from_notebook('d')
        if d == 5:
            print(f"✅ Die Variable 'd' hat den korrekten Wert: {d}")
        else:
            print(f"❌ Die Variable 'd' hat den falschen Wert: {d}. Erwartet wurde: 5")

        check1 = _get_attribut_from_notebook('check1')
        if check1 == (a > b) and (a < c):
            print(f"✅ Die Variable 'check1' hat den korrekten Wert: {check1}")
        else:
            print(f"❌ Die Variable 'check1' hat den falschen Wert: {check1}. Erwartet wurde: {(a > b) and (a < c)}")
        check2 = _get_attribut_from_notebook('check2')
        if check2 == (d >= b):
            print(f"✅ Die Variable 'check2' hat den korrekten Wert: {check2}")
        else:
            print(f"❌ Die Variable 'check2' hat den falschen Wert: {check2}. Erwartet wurde: {d >= b}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_3_1():
    try:
        days = _get_attribut_from_notebook('days')
        if isinstance(days, list) and len(days) == 7 and ["Montag", "Dienstag", "Donnerstag", "Freitag", "Samstag", "Sonntag", "Feiertag"] == days:
            print(f"✅ Die Variable 'days' ist eine Liste mit der korrekten Länge von 7.")
        else:
            print(f"❌ Die Variable 'days' ist keine Liste mit der korrekten Länge von 7. Aktuelle Länge: {len(days) if isinstance(days, list) else 'N/A'}")

        first_and_last = _get_attribut_from_notebook('first_and_last')
        if (isinstance(first_and_last, tuple) and len(first_and_last) == 2 and
            first_and_last[0] == "Montag" and first_and_last[1] == "Sonntag"):
            print(f"✅ Die Variable 'first_and_last' ist ein Tupel mit den korrekten Werten: {first_and_last}")
        else:
            print(f"❌ Die Variable 'first_and_last' ist kein Tupel mit den korrekten Werten. Aktueller Wert: {first_and_last}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_3_2():
    try:
        numbers_hat = _get_attribut_from_notebook('numbers')
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if numbers_hat == numbers:
            print(f"✅ Die Variable 'numbers' ist korrekt definiert.")
        else:
            print(f"❌ Die Variable 'numbers' ist falsch definiert. Aktueller Wert: {numbers_hat}")

        slice1_hat = _get_attribut_from_notebook('slice1')
        slice1 = numbers[2:8]
        if slice1_hat == slice1:
            print(f"✅ Die Variable 'slice1' ist korrekt definiert.")
        else:
            print(f"❌ Die Variable 'slice1' ist falsch definiert. Aktueller Wert: {slice1_hat}")

        slice2_hat = _get_attribut_from_notebook('slice2')
        slice2 = numbers[::2]
        if slice2_hat == slice2:
            print(f"✅ Die Variable 'slice2' ist korrekt definiert.")
        else:
            print(f"❌ Die Variable 'slice2' ist falsch definiert. Aktueller Wert: {slice2_hat}")

        result_sum_hat = _get_attribut_from_notebook('result_sum')
        result_sum = sum(numbers)
        if result_sum_hat == result_sum:
            print(f"✅ Die Variable 'result_sum' ist korrekt definiert.")
        else:
            print(f"❌ Die Variable 'result_sum' ist falsch definiert. Aktueller Wert: {result_sum_hat}")
        
        result_min_hat = _get_attribut_from_notebook('result_min')
        result_min = min(numbers)
        if result_min_hat == result_min:
            print(f"✅ Die Variable 'result_min' ist korrekt definiert.")
        else:
            print(f"❌ Die Variable 'result_min' ist falsch definiert. Aktueller Wert: {result_min_hat}")

        result_max_hat = _get_attribut_from_notebook('result_max')
        result_max = max(numbers)
        if result_max_hat == result_max:
            print(f"✅ Die Variable 'result_max' ist korrekt definiert.")
        else:
            print(f"❌ Die Variable 'result_max' ist falsch definiert. Aktueller Wert: {result_max_hat}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_4_1():
    try:
        student = _get_attribut_from_notebook('student')
        if (isinstance(student, dict)):
            if 'name' not in student:
                print(f"❌ Der Schlüssel 'name' fehlt im Dictionary 'student'.")
            elif 'mat_nr' not in student:
                print(f"❌ Der Schlüssel 'mat_nr' fehlt im Dictionary 'student'.")
            elif 'study_program' not in student:
                print(f"❌ Der Schlüssel 'study_program' fehlt im Dictionary 'student'.")
            elif 'semester' not in student:
                print(f"❌ Der Schlüssel 'semester' fehlt im Dictionary 'student'.")
            elif not type(student.get('name')) == str:
                print(f"'❌ student' ist kein Dictionary.")
            elif not type(student.get('mat_nr')) in [int, str]:
                print(f"❌ 'mat_nr' ist weder Zeichenkette noch Integer. Aktueller Typ: {type(student['mat_nr'])}")
            elif not type(student.get('study_program')) == str:
                print(f"❌ 'study_program' ist keine Zeichenkette. Aktueller Typ: {type(student['study_program'])}")
            elif not type(student.get('semester')) == int:
                print(f"❌ 'semester' ist kein Integer. Aktueller Typ: {type(student['semester'])}")
            else:
                print("✅ Das Dictionary 'student' ist korrekt definiert.")
        else:
            print(f"❌ Das Dictionary 'student' ist falsch definiert. Aktueller Wert: {student}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_4_2():
    try:
        student = _get_attribut_from_notebook('student')
        dict_content = _get_attribut_from_notebook('dict_content')

        if len(student.keys()) == len(dict_content):
            print(f"✅ Die Liste 'dict_content' hat die gleiche Länge wie 'student' items hat. Der Inhalt ist:")
            for row in dict_content:
                print(row)
        else:
            print(f"❌ Die Liste 'dict_content' hat eine andere Länge ({len(dict_content)}) als 'student' Items ({len(student.keys())}) hat.")

    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_5_1():
    def is_int_triple(obj):
        return (
            isinstance(obj, tuple) and 
            len(obj) == 3 and 
            all(isinstance(x, int) for x in obj)
        )

    try:
        tuple1 = _get_attribut_from_notebook('tuple1')
        if not is_int_triple(tuple1):
            print(f"❌ 'tuple1' ist kein Tupel mit drei Integer-Werten. Aktueller Typ: {type(tuple1)}")
        elif tuple1[0] != 255 or tuple1[1] != 0 or tuple1[2] != 0:
            print(f"❌ Tupel 'tuple1' hat die falschen Werte. Aktuelle Werte: {tuple1}")
        else:
            print(f"✅ Das Tupel 'tuple1' ist korrekt definiert.")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_5_2():
    try:
        course_a_hat = _get_attribut_from_notebook("course_a")
        course_a = {"Anna", "Ben", "Clara", "David"}
        if course_a != course_a_hat:
            print(f"❌ Das Set 'course_a' ist falsch definiert. Erwartet wurde: {course_a}, aber erhalten: {course_a_hat}")
        else:
            print(f"✅ Das Set 'course_a' ist korrekt definiert.")

        course_b_hat = _get_attribut_from_notebook("course_b")
        course_b = {"Clara", "David", "Emma", "Felix"}
        if course_b != course_b_hat:
            print(f"❌ Das Set 'course_b' ist falsch definiert. Erwartet wurde: {course_b}, aber erhalten: {course_b_hat}")
        else:
            print(f"✅ Das Set 'course_b' ist korrekt definiert.")

        all_students_hat = _get_attribut_from_notebook("all_students")
        all_students = course_a | course_b
        if all_students != all_students_hat:
            print(f"❌ Das Set 'all_students' hat den falschen Inhalt. Erwartet wurde: {all_students}, aber erhalten: {all_students_hat}")
        else:
            print(f"✅ Das Set 'all_students' wurde korrekt definiert.")

        students_in_both_coureses = course_a & course_b
        students_in_both_coureses_hat = _get_attribut_from_notebook("students_in_both_coureses")
        if students_in_both_coureses != students_in_both_coureses_hat:
            print(f"❌ Das Set 'students_in_both_coureses' hat den falschen Inhalt. Erwartet wurde: {students_in_both_coureses}, aber erhalten: {students_in_both_coureses_hat}")
        else:
            print(f"✅ Das Set 'students_in_both_coureses' wurde korrekt definiert.")

        students_just_in_a_hat = _get_attribut_from_notebook("students_just_in_a")
        students_just_in_a = course_a - course_b
        if students_just_in_a != students_just_in_a_hat:
            print(f"❌ Das Set 'students_just_in_a' hat den falschen Inhalt. Erwartet wurde: {students_just_in_a}, aber erhalten: {students_just_in_a_hat}")
        else:
            print(f"✅ Das Set 'students_just_in_a' wurde korrekt definiert.")

    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_6_1():
    try:
        number = _get_attribut_from_notebook("number")
        result_hat = _get_attribut_from_notebook("result")

        if number > 0:
            result = "Positiv"
        elif number < 0:
            result = "Negativ"
        else:
            result = "Null"

        if result != result_hat:
            print(f"❌ Die Variable 'result' hat den falschen Wert. Erwartet wurde: {result}, aber erhalten: {result_hat}")
        else:
            print(f"✅ Die Variable 'result' wurde korrekt definiert.")

    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_6_2():
    try:
        results = [0, 1, 2, 3, 4, 6, 7]
        results_hat = _get_attribut_from_notebook("results")
        if results != results_hat:
            print(f"❌ Die Variable 'results' hat den falschen Wert. Erwartet wurde: {results}, aber erhalten: {results_hat}")
        else:
            print(f"✅ Die Variable 'results' wurde korrekt definiert.")

    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_6_3():
    try:
        number = _get_attribut_from_notebook("number")
        result_hat = _get_attribut_from_notebook("result")

        result = 1
        n = number
        while n > 1:
            result *= n
            n -= 1

        if result != result_hat:
            print(f"❌ Die Variable 'result' hat den falschen Wert. Erwartet wurde: {result}, aber erhalten: {result_hat}")
        else:
            print(f"✅ Die Variable 'result' wurde korrekt definiert. Ergebnis: {result}")

    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_7_1():
    try:
        area_function = _get_attribut_from_notebook('calculate_area')
        if not callable(area_function):
            print("❌ 'calculate_area' ist keine Funktion.")
            return

        a = _get_attribut_from_notebook('a')
        b = _get_attribut_from_notebook('b')

        if not area_function(a, b) == a * b:
            print(f"❌ Die Funktion 'calculate_area' liefert falsche Ergebnisse für a={a}, b={b}.")
            return

        result = a * b
        result_hat = _get_attribut_from_notebook('result')

        if result != result_hat:
            print(f"❌ Die Variable 'result' hat den falschen Wert. Erwartet wurde: {result}, aber erhalten: {result_hat}")
        else:
            print(f"✅ Die Variable 'result' wurde korrekt definiert. Ergebnis: {result}")
    
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_7_2():
    try:
        prime_function = _get_attribut_from_notebook('is_prime')
        if not callable(prime_function):
            print("❌ 'is_prime' ist keine Funktion.")
            return

        number = _get_attribut_from_notebook('number')
        if not isinstance(number, int):
            print("❌ 'number' ist keine ganze Zahl.")
            return

        test_values = {
            2: True,
            3: True,
            4: False,
            5: True,
            10: False,
            13: True,
            25: False,
            29: True
        }

        for n, expected in test_values.items():
            result = prime_function(n)
            if result != expected:
                print(f"❌ Die Funktion 'is_prime' liefert falsche Ergebnisse für n={n}. Erwartet: {expected}, aber erhalten: {result}")

        print("✅ Die Funktion 'is_prime' wurde korrekt definiert und liefert die erwarteten Ergebnisse.")

    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_7_3():
    try:
        sum_function = _get_attribut_from_notebook('calculate_sum')
        if not callable(sum_function):
            print("❌ 'calculate_sum' ist keine Funktion.")
            return

        test_args = (1, 2, 3, 4, 5)
        expected_sum = sum(test_args)
        result = sum_function(*test_args)

        if result != expected_sum:
            print(f"❌ Die Funktion 'calculate_sum' liefert falsche Ergebnisse für Argumente {test_args}. Erwartet: {expected_sum}, aber erhalten: {result}")
        else:
            print(f"✅ Die Funktion 'calculate_sum' wurde korrekt definiert.")

    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_8_1():
    try:
        results_hat = _get_attribut_from_notebook("results")
        expected_results = [i**2 for i in range(1, 21)]

        if results_hat != expected_results:
            print(f"❌ Die Variable 'results' hat den falschen Wert. Erwartet wurde: {expected_results}, aber erhalten: {results_hat}")
        else:
            print(f"✅ Die Variable 'results' wurde korrekt definiert.")

    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_8_2():
    try:
        results_hat = _get_attribut_from_notebook("results")
        expected_results = [i for i in range(1, 51) if i % 3 == 0 and i % 5 == 0]

        if results_hat != expected_results:
            print(f"❌ Die Variable 'results' hat den falschen Wert. Erwartet wurde: {expected_results}, aber erhalten: {results_hat}")
        else:
            print(f"✅ Die Variable 'results' wurde korrekt definiert.")

    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_8_3():
    try:
        results_hat = _get_attribut_from_notebook("results")
        words = _get_attribut_from_notebook("words")
        expected_results = {word: len(word) for word in words}

        if results_hat != expected_results:
            print(f"❌ Die Variable 'results' hat den falschen Wert. Erwartet wurde: {expected_results}, aber erhalten: {results_hat}")
        else:
            print(f"✅ Die Variable 'results' wurde korrekt definiert.")

    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_9_1():
    import inspect
    try:
        class_BankAccount = _get_attribut_from_notebook('BankAccount')
        if not inspect.isclass(class_BankAccount):
            print(f"❌ 'BankAccount' ist keine Klasse, sondern: {type(class_BankAccount)}")
        else:
            print(f"✅ Bankaccount Klasse gefunden.")

        bankAccount = class_BankAccount('Robert Schulz')
        if not hasattr(bankAccount, 'owner'):
            print(f"❌ Die Klasse 'BankAccount' hat kein Attribut 'owner'.")
        else:
            print(f"✅ Attribut 'owner' vorhanden. Wert: {bankAccount.owner}")

        if not hasattr(bankAccount, 'balance'):
            print(f"❌ Die Klasse 'BankAccount' hat kein Attribut 'balance'.")
        else:
            print(f"✅ Attribut 'balance' vorhanden. Wert: {bankAccount.balance}")

        if not hasattr(bankAccount, 'deposit'):
            print(f"❌ Die Klasse 'BankAccount' hat keine Methode 'deposit'.")
        else:
            print(f"✅ Methode 'deposit' vorhanden.")

        if not hasattr(bankAccount, 'withdraw'):
            print(f"❌ Die Klasse 'BankAccount' hat keine Methode 'withdraw'.")
        else:
            print(f"✅ Methode 'withdraw' vorhanden.")

        if not hasattr(bankAccount, 'get_balance'):
            print(f"❌ Die Klasse 'BankAccount' hat keine Methode 'get_balance'.")
        else:
            print(f"✅ Methode 'get_balance' vorhanden.")

        amount1 = 15.45
        bankAccount.deposit(amount1)
        if bankAccount.balance != amount1:
            print(f"❌ Die Methode 'deposit' hat den Kontostand nicht korrekt erhöht. Erwartet: {amount1}, Tatsächlich: {bankAccount.balance}")
        else:
            print(f"✅ Die Methode 'deposit({amount1})' hat den Kontostand korrekt erhöht: {bankAccount.balance}")

        amount2 = 14.
        bankAccount.withdraw(amount2)
        if bankAccount.balance != amount1-amount2:
            print(f"❌ Die Methode 'withdraw' hat den Kontostand nicht korrekt veringert. Erwartet: {amount1-amount2}, Tatsächlich: {bankAccount.balance}")
        else:
            print(f"✅ Die Methode 'deposit({amount2})' hat den Kontostand korrekt veringer: {bankAccount.balance}")

        amount3 = 4.0
        result = bankAccount.withdraw(amount3)
        if result != None:
            print(f"❌ Die Methode 'withdraw' hat den Kontostand nicht korrekt überprüft. Der Rückgabewert war: {result}, Erwartet: None")
        else:
            print(f"✅ Die Kontostandsüberprüfung der Methode 'withdraw' war erfolgreich.")

        balance = bankAccount.get_balance()
        if not isinstance(balance, float):
            print(f"❌ Die Methode 'get_balance' hat {balance} {type(balance)} zurückgegeben. Erwartet: float")
        elif balance != amount1 - amount2:
            print(f"❌ Die Methode 'get_balance' hat einen falschen Wert zurückgegeben: {balance}, Erwartet: {amount1-amount2}")
        else:
            print(f"✅ Die Methode 'get_balance' hat den korrekten Wert zurückgegeben.")

        pass
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_9_2():
    import inspect
    try:
        class_Car = _get_attribut_from_notebook('Car')
        if not inspect.isclass(class_Car):
            print(f"❌ 'Car' ist keine Klasse, sondern: {type(class_Car)}")
        else:
            print(f"✅ 'Car' Klasse gefunden.")

        class_ElectricCar = _get_attribut_from_notebook('ElectricCar')
        if not inspect.isclass(class_ElectricCar):
            print(f"❌ 'ElectricCar' ist keine Klasse, sondern: {type(class_ElectricCar)}")
        else:
            print(f"✅ 'ElectricCar' Klasse gefunden.")

        electricCar = class_ElectricCar('Polestar', '5', 650)
        if not hasattr(electricCar, 'brand'):
            print(f"❌ Die Klasse 'ElectricCar' hat kein Attribut 'brand'.")
        else:
            print(f"✅ Attribut 'brand' in Klasse 'ElectricCar' vorhanden.")

        if not hasattr(electricCar, 'model'):
            print(f"❌ Die Klasse 'ElectricCar' hat kein Attribut 'model'.")
        else:
            print(f"✅ Attribut 'model' in Klasse 'ElectricCar' vorhanden.")

        if not hasattr(electricCar, 'mileage'):
            print(f"❌ Die Klasse 'ElectricCar' hat kein Attribut 'mileage'.")
        else:
            print(f"✅ Attribut 'mileage' in Klasse 'ElectricCar' vorhanden.")

        if not hasattr(electricCar, 'battery_capacity'):
            print(f"❌ Die Klasse 'ElectricCar' hat kein Attribut 'battery_capacity'.")
        else:
            print(f"✅ Attribut 'battery_capacity' in Klasse 'ElectricCar' vorhanden.")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_10_1():
    try:
        divide_method = _get_attribut_from_notebook('divide')

        try:
            a = 3
            b = 0
            result = divide_method(a, b)
        except ZeroDivisionError as e:
            print(f"✅ 'ZeroDivisionError' ausgelöst.")
        else:
            print(f"❌ 'ZeroDivisionError' nicht ausgelöst für a={a} und b={b}.")

        try:
            a = 'Zeichenkette'
            b = True
            result = divide_method(a, b)
        except ValueError as e:
            print(f"✅ 'ValueError' ausgelöst.")
        else:
            print(f"❌ 'ValueError' nicht ausgelöst für a={a} ({type(a)}) und b={b} ({type(b)}).")
    
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_10_2():
    try:
        class_SmallValueError = _get_attribut_from_notebook('SmallValueError')
        method_check_value = _get_attribut_from_notebook('check_value')

        try:
            method_check_value(3)
        except class_SmallValueError as e:
            print(f"✅ 'SmallValueError' ausgelöst für Wert 3.")
        else:
            print(f"❌ 'SmallValueError' nicht ausgelöst für Wert 3.")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_11_1():
    import os
    try:
        if not os.path.isfile('notizen.txt'):
            print(f"❌ Datei 'notizen.txt' nicht gefunden.")
        else:
            print(f"✅ Datei 'notizen.txt' gefunden.")

        with open('notizen.txt', 'r') as f:
            lines = f.readlines()

        if len(lines) != 3:
            print(f"❌ Datei 'notizen.txt' enthält keine 3 Zeilen, sondern {len(lines)}.")
        else:
            print(f"✅ Datei 'notizen.txt' korrekt erstellt.")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_11_2():
    import os
    try:
        results = _get_attribut_from_notebook('results')
        for i, result in enumerate(results):
            i_hat = int(result[0])
            if i != i_hat:
                print(f"❌ Zeile {i} falsch formatiert. Erwartet {i} an 1. Stelle. Tatsächöich: {i_hat}")
            else:
                print(f"✅ Zeile {i} korrekt formatiert.")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_11_3():
    import os
    import json
    try:
        in_dict = _get_attribut_from_notebook('in_dict')
        out_dict = _get_attribut_from_notebook('out_dict')

        if not os.path.isfile('student.json'):
            print(f"❌ Datei 'student.json' nicht gefunden.")
        else:
            print(f"✅ Datei 'student.json' existiert.")

        if in_dict != out_dict:
            print(f"❌ 'in_dict' ungleich 'out_dict'.\n'in_dict: {in_dict}'\nout_dict: {out_dict}")
        else:
            print(f"✅ 'in_dict' gleich 'out_dict'")

        with open('student.json', 'r') as f:
            loaded_dict = json.load(f)

        if in_dict != loaded_dict:
            print(f"❌ 'in_dict' ungleich 'loaded_dict'.\n'in_dict: {in_dict}'\nloaded_dict: {out_dict}")
        else:
            print(f"✅ 'in_dict' gleich Dateiinhalt.")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_12_1():
    try:
        list1 = _get_attribut_from_notebook('list1')
        list2 = _get_attribut_from_notebook('list2')
        result1 = _get_attribut_from_notebook('result1')
        result2 = _get_attribut_from_notebook('result2')
        
        if result1 in range(1, 101):
            print(f"✅ Zufallszahl 'result1' liegt in [1, 100].")
        else:
            print(f"❌ Zufallszahl 'result1' liegt nicht in [1, 100]. 'result1={result1}'")

        if result2 in list1:
            print(f"✅ Zufallszahl 'result2' in 'list1'.")
        else:
            print(f"❌ Zufallszahl 'result2' nicht in 'list1={list1}'. 'result2={result2}'")
 
        if list1 == list2:
            print(f"❌ 'list2' gleich 'list1' -> nicht geshuffelt.")
        elif sorted(list1) != sorted(list2):
            print(f"❌ 'list2' enthält andere Elemente als 'list1'.\n'list1={list1}'\n'list2={list2}'")
        else:
            print(f"✅ Liste erfolgreich geshuffelt.")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_12_2():
    try:
        import datetime
        date_today_hat = _get_attribut_from_notebook('date_today')
        time_now_hat = _get_attribut_from_notebook('time_now')
        days_until_silvester_hat = _get_attribut_from_notebook('days_until_silvester')

        date_today = datetime.date.today()
        time_now = datetime.datetime.now().time()
        days_until_silvester = (datetime.date(date_today.year, 12, 31) - date_today).days

        if date_today == date_today_hat:
            print(f"✅ 'date_today' ist korrekt.")
        else:
            print(f"❌ 'date_today' ist falsch. Soll: {date_today}, Ist: {date_today_hat}")

        if time_now.hour == time_now_hat.hour and time_now.minute == time_now_hat.minute:
            print(f"✅ 'time_now' ist korrekt.")
        else:
            print(f"❌ 'time_now' ist falsch. Soll: {time_now}, Ist: {time_now_hat}")

        if days_until_silvester == days_until_silvester_hat:
            print(f"✅ 'days_until_silvester' ist korrekt.")
        else:
            print(f"❌ 'days_until_silvester' ist falsch. Soll: {days_until_silvester}, Ist: {days_until_silvester_hat}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_13_1():
    try:
        import numpy as np

        array1_hat = _get_attribut_from_notebook('array1')
        array2_hat = _get_attribut_from_notebook('array2')
        array_mean_hat = _get_attribut_from_notebook('array_mean')
        array_std_hat = _get_attribut_from_notebook('array_std')
        array_sum_hat = _get_attribut_from_notebook('array_sum')

        array1 = np.arange(20)
        
        print("t1")
        if np.equal(array1, array1_hat).all():
            print(f"✅ 'array1' korrekt.")
        else:
            print(f" 'array1' fehlerhaft.\nSoll: {array1}\nIst: {array1_hat}")

        print('t: array1', array1)
        print('t: array2_hat.shape', array2_hat.shape)
        if array2_hat.shape[0] == 4 and array2_hat.shape[1] == 5:
            print(f"✅ 'array2' hat den richtigen shape.")
        else:
            print(f"❌ 'array2' hat den falschen shape. Soll: (2, 5), Ist: {array2_hat.shape}")

        array_mean = np.mean(array1)
        array_std = np.std(array1)
        array_sum = np.sum(array1)

        if array_mean == array_mean_hat:
            print(f"✅ Mittelwert 'array_mean' korrekt ermittelt.")
        else:
            print(f"❌ Mittelwert 'array_mean' falsch ermittelt.\nSoll: {array_mean}\nIst: {array_mean_hat}")

        if array_std == array_std_hat:
            print(f"✅ Standardabweichung 'array_std' korrekt ermittelt.")
        else:
            print(f"❌ Standardabweichung 'array_std' falsch ermittelt.\nSoll: {array_std}\nIst: {array_std_hat}")

        if array_sum == array_sum_hat:
            print(f"✅ Summe 'array_sum' korrekt ermittelt.")
        else:
            print(f"❌ Summe 'array_sum' falsch ermittelt.\nSoll: {array_sum}\nIst: {array_sum_hat}")

    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_13_2():
    try:
        import numpy as np

        array1 = _get_attribut_from_notebook('array1')
        array2 = _get_attribut_from_notebook('array2')
        array3 = array1 + array2
        array4 = array1 * array2
        det = np.linalg.det(array1)

        array3_hat = _get_attribut_from_notebook('array3')
        array4_hat = _get_attribut_from_notebook('array4')
        det_hat = _get_attribut_from_notebook('det')

        if np.equal(array3, array3_hat).all():
            print(f"✅ Elementweise Summe korrekt berechnet.")
        else:
            print(f"❌ Elementweise Summe falsch berechnet.\nSoll: {array3}\nIst: {array3_hat}")

        if np.equal(array4, array4_hat).all():
            print(f"✅ Elementweises Produkt korrekt berechnet.")
        else:
            print(f"❌ Elementweises Produkt falsch berechnet.\nSoll: {array4}\nIst: {array4_hat}")

        if det == det_hat:
            print(f"✅ Determinante korrekt berechnet.")
        else:
            print(f"❌ Determinante falsch berechnet.\nSoll: {det}\nIst: {det_hat}")

    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_13_3():
    try:
        import numpy as np

        array1_hat = _get_attribut_from_notebook('array1')
        array2_hat = _get_attribut_from_notebook('array2') 

        array2 = array1_hat[array1_hat > 1]

        std, mean = np.std(array1_hat), np.mean(array1_hat)
        if len(array1_hat) != 1000:
            print(f"❌ Länge von 'array1' ungleich 1000.")
        else:
            print(f"✅ Länge von 'array1' korrekt.")

        if std < 0.97 or std > 1.03 or np.abs(mean) > 0.06:
            print(f"❌ 'array1' entspricht nicht der Normalverteilung. std is {std}, mean is {mean}")
        else:
            print(f"✅ 'array1' entspricht der Normalverteilung.")
        
        if np.equal(array2, array2_hat).all():
            print(f"✅ Werte korrekt ausgewählt.")
        else:
            print(f"❌ Werte nicht korrekt ausgewählt. 'array2': {array2_hat}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_14_1():
    try:
        import torch

        tensor1 = _get_attribut_from_notebook('tensor1')
        tensor2 = _get_attribut_from_notebook('tensor2')
        tensor3_hat = _get_attribut_from_notebook('tensor3')
        tensor4_hat = _get_attribut_from_notebook('tensor4')
        tensor5_hat = _get_attribut_from_notebook('tensor5')

        tensor3 = tensor1 + tensor2
        if torch.all(tensor3 == tensor3_hat):
            print(f"✅ Summe korrekt berechnet.")
        else:
            print(f"❌ Summe falsch berechnet.\nSoll: {tensor3}\nIst: {tensor3_hat}")

        tensor4 = tensor1 * tensor2
        if torch.all(tensor4 == tensor4_hat):
            print(f"✅ Produkt korrekt berechnet.")
        else:
            print(f"❌ Produkt falsch berechnet.\nSoll: {tensor4}\nIst: {tensor4_hat}")

        tensor5 = torch.mm(tensor1, tensor2)
        if torch.all(tensor5 == tensor5_hat):
            print(f"✅ Matrix-Multiplikation korrekt durchgeführt.")
        else:
            print(f"❌ Matrix-Multiplikation falsch durchgeführt.\nSoll: {tensor5}\nIst: {tensor5_hat}")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_14_2():
    try:
        import torch

        x_hat:torch.Tensor = _get_attribut_from_notebook('x')
        y_hat:torch.Tensor = _get_attribut_from_notebook('y')

        x:torch.Tensor = torch.tensor(x_hat, requires_grad=True)
        y:torch.Tensor = 3*x**2 + 2*x + 1
        y.backward()

        if x.grad == x_hat.grad:
            print(f"✅ Gradient korrekt berechnet: {x.grad}")
        else:
            print(f"❌ Gradient falsch berechnet. Soll: {x.grad}, Ist: {x_hat.grad}")
        pass
    except Exception as e:
        print(f"❌ Fehler: {e}")

def task_14_3():
    try:
        import torch

        def check_linear(module, in_features, out_features):
            if isinstance(module, torch.nn.Linear):
                if module.in_features == in_features and module.out_features == out_features:
                    print(f"✅ Layer {i} ist korrekt implementiert.")
                else:
                    print(f"❌ Layer {i} ist falsch implementiert.\nSoll: {torch.nn.Linear} ({in_features}, {out_features})\nIst: {type(module)} ({module.in_features}, {module.out_features})")
            else:
                print(f"❌ Layer {i} ist falsch implementiert.\nSoll: {torch.nn.Linear}\nIst: {type(module)}")


        model_hat:torch.nn.Module = _get_attribut_from_notebook('model')
        for i, (module) in enumerate(model_hat.modules()):
            if isinstance(module, torch.nn.Linear):
                module:torch.nn.Linear = module

            if i == 0:
                pass
            elif i == 1:
                check_linear(module, 5, 10)
            elif i == 2:
                if isinstance(module, torch.nn.ReLU):
                    print(f"✅ ReLU korrekt implementiert.")
                else:
                    print(f"❌ An Stelle 2 müsste {torch.nn.ReLU} stehen. Ist: {type(module)}")
            elif i == 3:
                check_linear(module, 10, 2)
            else:
                modules = list(model_hat.modules())
                print(f"❌ Modell hat zu viele Layer. Soll: 3, Ist: {len(list(model_hat.modules()))}")

    except Exception as e:
        print(f"❌ Fehler: {e}")