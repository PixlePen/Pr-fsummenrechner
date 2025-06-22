import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import hashlib
import os # Für Dateigröße

# --- Funktionen ---
def select_file():
    """Öffnet einen Dateidialog und aktualisiert das Pfad-Label."""
    filepath = filedialog.askopenfilename()
    if filepath:
        file_path_var.set(filepath)
        # Zeige Dateigröße an (optional, aber nützlich)
        try:
            size_bytes = os.path.getsize(filepath)
            if size_bytes < 1024:
                size_str = f"{size_bytes} Bytes"
            elif size_bytes < 1024**2:
                size_str = f"{size_bytes/1024:.2f} KB"
            elif size_bytes < 1024**3:
                size_str = f"{size_bytes/1024**2:.2f} MB"
            else:
                size_str = f"{size_bytes/1024**3:.2f} GB"
            status_var.set(f"Größe: {size_str}")
        except OSError:
             status_var.set("Größe konnte nicht ermittelt werden.")
        result_var.set("") # Altes Ergebnis löschen
    else:
        file_path_var.set("Keine Datei ausgewählt")
        status_var.set("")
        result_var.set("")

def calculate_hash():
    """Berechnet die Prüfsumme der ausgewählten Datei."""
    filepath = file_path_var.get()
    algo = algo_var.get()

    if not filepath or filepath == "Keine Datei ausgewählt":
        messagebox.showerror("Fehler", "Bitte zuerst eine Datei auswählen.")
        return

    if not algo:
        messagebox.showerror("Fehler", "Bitte einen Algorithmus auswählen.")
        return

    try:
        status_var.set("Berechne...")
        root.update_idletasks() # UI aktualisieren, damit "Berechne..." sichtbar wird

        hasher = hashlib.new(algo)
        chunk_size = 65536 # 64KB Chunks - gut für Speicher

        with open(filepath, 'rb') as file:
            while chunk := file.read(chunk_size):
                hasher.update(chunk)

        hex_digest = hasher.hexdigest()
        result_var.set(hex_digest)
        status_var.set("Berechnung abgeschlossen.")

    except FileNotFoundError:
        messagebox.showerror("Fehler", f"Datei nicht gefunden:\n{filepath}")
        status_var.set("Fehler: Datei nicht gefunden.")
        result_var.set("")
    except Exception as e:
        messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten:\n{e}")
        status_var.set(f"Fehler: {e}")
        result_var.set("")

# --- GUI Aufbau ---
root = tk.Tk()
root.title("Datei Prüfsummen Rechner")

# Variablen
file_path_var = tk.StringVar(value="Keine Datei ausgewählt")
algo_var = tk.StringVar(value="sha256") # Standard: SHA256
result_var = tk.StringVar()
status_var = tk.StringVar()

# Frame für Dateiauswahl
file_frame = ttk.LabelFrame(root, text="Datei")
file_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

ttk.Button(file_frame, text="Datei wählen...", command=select_file).pack(side=tk.LEFT, padx=5, pady=5)
ttk.Label(file_frame, textvariable=file_path_var, relief="sunken", width=40).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

# Frame für Algorithmus
algo_frame = ttk.LabelFrame(root, text="Algorithmus")
algo_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

ttk.Radiobutton(algo_frame, text="SHA256", variable=algo_var, value="sha256").pack(side=tk.LEFT, padx=5)
ttk.Radiobutton(algo_frame, text="MD5", variable=algo_var, value="md5").pack(side=tk.LEFT, padx=5)
# Weitere hinzufügen bei Bedarf (z.B. sha1, sha512)

# Berechnen Button
ttk.Button(root, text="Prüfsumme berechnen", command=calculate_hash).grid(row=2, column=0, padx=10, pady=10)

# Frame für Ergebnis
result_frame = ttk.LabelFrame(root, text="Prüfsumme")
result_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

result_entry = ttk.Entry(result_frame, textvariable=result_var, state="readonly", width=60)
result_entry.pack(padx=5, pady=5, fill=tk.X)

# Statusleiste
status_label = ttk.Label(root, textvariable=status_var, relief="sunken")
status_label.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

root.columnconfigure(0, weight=1) # Erlaubt horizontalen Größenänderung
root.mainloop()