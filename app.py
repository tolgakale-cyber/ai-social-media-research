from engine.config import SEKTÖR, VERİ_KAYNAKLARI, YAPAY_ZEKÂ_MODELLERİ


def main():
    print("AI Social Media Research Automation")
    print(f"Sektör: {SEKTÖR}")

    print("\nVeri kaynakları:")
    for kaynak in VERİ_KAYNAKLARI:
        print(f"- {kaynak}")

    print("\nYapay zekâ modelleri:")
    for model in YAPAY_ZEKÂ_MODELLERİ:
        print(f"- {model}")

    print("\nSistem başlatıldı.")


if __name__ == "__main__":
    main()