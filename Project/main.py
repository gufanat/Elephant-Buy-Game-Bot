import random


# Вступний текст
def intro():
    print("""
    Вітаємо у грі "А ти купи слона"!
    У цій грі комп'ютер намагатиметься переконати вас купити слона.
    На кожну вашу відповідь комп'ютер буде писати переконливі тексти.
    Гра закінчується, коли ви погодитесь купити слона або вирішите завершити гру достроково.
    Ваше завдання - відмовлятися якомога довше.

    Коли ви розпочнете гру ви зможете:
    написати будь-яку відповідь комп'ютеру,
    написати "так" щоб погодитись купити слона, після чого ви побачете підсумок,
    написати "стоп" щоб достроково завершити гру, після чого підсумка не буде.""")


# Меню гри
def menu():
    print("\nМеню:\n1. Почати гру\n2. Переглянути свій рекорд\n3. Вийти")


# Основна логіка гри
def start_game():
    elephant_responses = [
        "Слон дуже корисний для дому.",
        "Слони - це найкращі друзі.",
        "Слон може стати вашим новим улюбленцем.",
        "Слона можна навчити багатьом трюкам.",
        "Слони приносять удачу."
    ]

    response_count = 0

    while True:
        player_response = input("\nХочете купити слона?\nВаша відповідь: ").strip().lower()
        if player_response == "так":
            return response_count, False
        elif player_response == "стоп":
            return response_count, True
        else:
            response = random.choice(elephant_responses)
            print(f'\nВсі кажуть "{player_response}", а ти купи слона. {response}')
            response_count += 1


# Головна функція
def main():
    intro()
    best_record = None

    while True:
        menu()
        choice = input("Зробіть свій вибір (1, 2 або 3): ").strip()

        if choice == "1":
            response_count, stopped_early = start_game()
            if stopped_early:
                print("\nВи завершили гру достроково, підсумків не буде.")
            else:
                if best_record is None or response_count > best_record:
                    best_record = response_count
                    print(f"\nВітаємо! Ви погодились купити слона після {response_count} відмов.")
                    print("Це новий рекорд!")
                else:
                    print(f"\nВітаємо! Ви погодились купити слона після {response_count} відмов.")
                    print("Якщо хочете, можете спробувати побити свій рекорд знову.")

        elif choice == "2":
            if best_record is None:
                print("\nЩе немає встановленого рекорду.")
            else:
                print(f"\nВаш рекорд за сесію: {best_record} відмов.")

        elif choice == "3":
            print("\nДякуємо за гру! До побачення!")
            break

        else:
            print("\nНевірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
