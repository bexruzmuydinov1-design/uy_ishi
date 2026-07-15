"""
АВТОСАЛОН — консольное приложение на Python
--------------------------------------------
- 10 моделей автомобилей
- по 3 комплектации (версии) в каждой модели
- цены ориентированы на реальный рынок РФ 2026 года (округлены, актуальны примерно)
- расчёт покупки в рассрочку: срок в месяцах и сумма ежемесячного платежа
"""

CATALOG = {
    "LADA Granta": [
        ("Standard",  788_000),
        ("Classic",   1_088_000),
        ("Luxe",      1_320_000),
    ],
    "LADA Vesta": [
        ("Classic",   1_550_000),
        ("Comfort",   1_780_000),
        ("Enjoy",     1_990_000),
    ],
    "Kia Rio (Solaris KRS)": [
        ("Classic",   2_210_000),
        ("Comfort",   2_540_000),
        ("Premium",   2_870_000),
    ],
    "Hyundai Solaris": [
        ("Active",    2_150_000),
        ("Comfort",   2_450_000),
        ("Style",     2_750_000),
    ],
    "Toyota Camry": [
        ("Comfort",   4_630_000),
        ("Elegance",  4_950_000),
        ("Prestige",  5_200_000),
    ],
    "Haval Jolion": [
        ("Comfort",   2_050_000),
        ("Elite",     2_320_000),
        ("Flagship",  2_590_000),
    ],
    "Chery Tiggo 7 Pro": [
        ("Life",      2_450_000),
        ("Active",    2_700_000),
        ("Luxury",    2_950_000),
    ],
    "Geely Coolray": [
        ("Comfort",   2_150_000),
        ("Flagship",  2_400_000),
        ("Flagship+", 2_650_000),
    ],
    "Changan CS35 Plus": [
        ("Comfort",   1_850_000),
        ("Lux",       2_050_000),
        ("Top",       2_250_000),
    ],
    "Omoda C5": [
        ("Play",      1_950_000),
        ("Joy",       2_150_000),
        ("Style",     2_400_000),
    ],
}

INSTALLMENT_TERMS = [6, 12, 24, 36]


def show_models():
    """Вывести список моделей."""
    print("\n=== Список моделей автосалона ===")
    for i, model in enumerate(CATALOG.keys(), start=1):
        print(f"{i}. {model}")


def show_trims(model):
    """Вывести комплектации выбранной модели."""
    trims = CATALOG[model]
    print(f"\n=== Комплектации: {model} ===")
    for i, (trim, price) in enumerate(trims, start=1):
        print(f"{i}. {trim} — {price:,.0f} руб.".replace(",", " "))


def choose_from_list(prompt, count):
    """Запросить у пользователя номер из списка (1..count)."""
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and 1 <= int(raw) <= count:
            return int(raw) - 1
        print(f"Введите число от 1 до {count}.")


def calculate_installment(price, down_payment, months, annual_rate=0.0):
    """
    Расчёт рассрочки.
    price          — цена автомобиля
    down_payment   — первоначальный взнос (руб.)
    months         — срок рассрочки в месяцах
    annual_rate    — годовая ставка (0.0 = беспроцентная рассрочка)
    Возвращает (ежемесячный платёж, общая сумма выплат, переплата)
    """
    amount_to_pay = price - down_payment

    if annual_rate == 0:
        monthly_payment = amount_to_pay / months
        total_paid = amount_to_pay
    else:
        # аннуитетная формула
        monthly_rate = annual_rate / 12
        monthly_payment = amount_to_pay * (
            monthly_rate * (1 + monthly_rate) ** months
        ) / ((1 + monthly_rate) ** months - 1)
        total_paid = monthly_payment * months

    overpayment = total_paid - amount_to_pay
    return monthly_payment, total_paid, overpayment


def get_down_payment(price):
    """Запросить первоначальный взнос (в рублях или в процентах)."""
    while True:
        raw = input(
            "Введите первоначальный взнос в рублях (или в % от цены, например '20%'): "
        ).strip()
        try:
            if raw.endswith("%"):
                percent = float(raw[:-1])
                if not (0 <= percent < 100):
                    print("Процент должен быть от 0 до 99.")
                    continue
                return price * percent / 100
            value = float(raw.replace(" ", ""))
            if 0 <= value < price:
                return value
            print("Взнос не может быть больше цены авто и должен быть >= 0.")
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")


def choose_term():
    """Выбор срока рассрочки."""
    print("\nДоступные сроки рассрочки (мес.):")
    for i, term in enumerate(INSTALLMENT_TERMS, start=1):
        print(f"{i}. {term} месяцев")
    idx = choose_from_list("Выберите срок: ", len(INSTALLMENT_TERMS))
    return INSTALLMENT_TERMS[idx]


def format_money(value):
    return f"{value:,.2f} руб.".replace(",", " ")


def process_purchase(model, trim, price):
    print(f"\nВы выбрали: {model} ({trim}) — {format_money(price)}")

    print("\nСпособ оплаты:")
    print("1. Полная оплата")
    print("2. Рассрочка")
    choice = choose_from_list("Выберите вариант: ", 2)

    if choice == 0:
        print(f"\nК оплате: {format_money(price)}. Спасибо за покупку!")
        return

    # --- Рассрочка ---
    down_payment = get_down_payment(price)
    months = choose_term()

    # Условно: беспроцентная рассрочка от автосалона (annual_rate = 0.0)
    monthly_payment, total_paid, overpayment = calculate_installment(
        price, down_payment, months, annual_rate=0.0
    )

    print("\n=== Условия рассрочки ===")
    print(f"Цена автомобиля:          {format_money(price)}")
    print(f"Первоначальный взнос:     {format_money(down_payment)}")
    print(f"Срок рассрочки:           {months} месяцев")
    print(f"Ежемесячный платёж:       {format_money(monthly_payment)}")
    print(f"Итого к выплате (без взноса): {format_money(total_paid)}")
    print(f"Переплата:                {format_money(overpayment)}  (рассрочка беспроцентная)")


def main():
    print("=" * 50)
    print("      Добро пожаловать в АВТОСАЛОН 'DriveHouse'")
    print("=" * 50)

    while True:
        models = list(CATALOG.keys())
        show_models()
        m_idx = choose_from_list("\nВыберите номер модели (0 — выход): ", len(models))
        model = models[m_idx]

        trims = CATALOG[model]
        show_trims(model)
        t_idx = choose_from_list("Выберите комплектацию: ", len(trims))
        trim, price = trims[t_idx]

        process_purchase(model, trim, price)

        again = input("\nХотите оформить ещё одну покупку? (да/нет): ").strip().lower()
        if again not in ("да", "yes", "y", "д"):
            print("\nСпасибо, что выбрали наш автосалон! До встречи!")
            break


if __name__ == "__main__":
    main()