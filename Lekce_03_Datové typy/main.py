# ÚLOHA 1: Sčítací past (Cíl: 5 + 3 = 8)
# ---------------------------------------------------------
x = int(input("Zadej první čislo: "))
y = int(input("Zadej druhé číslo: "))

print (f"Výsledek je: {x+y}")
# ÚLOHA 2: Opakovač jména (Cíl: "Honza" a 3 -> "HonzaHonzaHonza")
# ---------------------------------------------------------
jmeno = input("Zadej jméno: ")
x = int(input("Kolikrát chceš jméno zopakovat: "))

print(jmeno * x)

# ÚLOHA 3: Rok narození (Cíl: 2026 - věk)
# ---------------------------------------------------------
vek = int(input("Zadej svůj věk: "))

print(f"Narodil ses přibližně v roce {2026-vek}")

# ÚLOHA 4: Výplata (Cíl: mzda * hodiny)
# ---------------------------------------------------------
mzda = int(input("Jaká je Vaše hodinová mzda? "))
hodiny = int(input("Kolik máte odpracovaných hodin? "))

print(f"Vaše celková odměna je {mzda * hodiny} Kč")

# ÚLOHA 5: Magická matematika (Cíl: (x + 10) * 2)
# ---------------------------------------------------------
cislo = int(input("Zadej své číslo: "))

print(f"Výsledek je: {(cislo + 10)*2}")
