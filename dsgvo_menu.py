#!/usr/bin/env python3
import os
import sys

def zeige_menu():
    print("\n" + "=" * 60)
    print("GEMUESEHANDEL DSGVO-ADMIN (BT-WEB01)")
    print("Sprint 3 - Art. 15 & 17 DSGVO")
    print("=" * 60)
    print("1) Auskunft Kunde (Art. 15)")
    print("2) Kunde loeschen (Art. 17)")
    print("0) Beenden")
    print("=" * 60)

while True:
    zeige_menu()
    choice = input("Auswahl: ").strip()
    
    if choice == "1":
        kid = input("Kunde ID: ").strip()
        if kid.isdigit():
            os.system(f"python3 dsgvo_auskunft.py {kid}")
        else:
            print("Nur Zahlen erlaubt!")
    
    elif choice == "2":
        kid = input("Kunde ID: ").strip()
        if kid.isdigit():
            os.system(f"python3 dsgvo_loeschen.py {kid}")
        else:
            print("Nur Zahlen erlaubt!")
    
    elif choice == "0":
        print("DSGVO-Admin beendet.")
        break
    
    else:
        print("Ungueltige Auswahl (1, 2 oder 0)!")
    
    input("\nEnter druecken fuer Menue...")
