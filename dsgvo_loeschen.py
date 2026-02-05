#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error
import sys
from config import DB_CONFIG

def main(kunde_id):
    print(f"\n{'='*60}")
    print(f"DSGVO LÖSCHUNG - Art. 17 (Kunde ID: {kunde_id})")
    print(f"{'='*60}")
    
    confirm = input("\n⚠️  Kunde + ALLE Aufträge LÖSCHEN? (JA/nein): ").upper()
    if confirm != "JA":
        print("❌ Abgebrochen.")
        return
    
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.callproc('dsgvo_loeschen', (kunde_id,))
        
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                print(row[0])
                
    except Error as e:
        print(f"❌ DB‑Fehler: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python3 dsgvo_loeschen.py <kunde_id>")
        exit(1)
    main(int(sys.argv[1]))
