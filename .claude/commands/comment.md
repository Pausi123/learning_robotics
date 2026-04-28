---
description: Kommentiere die aktuell geöffnete Datei als Lernhilfe
---

Kommentiere den folgenden Code als Lernhilfe für mich.

Argumente: $ARGUMENTS

## Sprache
- Standard: Deutsch
- Falls "en" oder "english" in den Argumenten: Englisch
- Falls "de" oder "deutsch" in den Argumenten: Deutsch

## Tiefe
- Falls "kurz" oder "short" in den Argumenten: Nur das Wichtigste kommentieren — Blöcke und nicht-offensichtliche Zeilen
- Falls "ausführlich" oder "detailed" in den Argumenten: Jede relevante Zeile kommentieren
- Standard (kein Argument): ausführlich

## Stil
- Lernhilfe: Erkläre nicht nur WAS der Code tut, sondern auch WARUM — warum diese Methode, warum dieser Parameter, was passiert wenn man es anders macht
- Kommentare direkt oberhalb oder hinter der jeweiligen Zeile, nicht als Block am Anfang
- Keine Zusammenfassung am Ende, keine Einleitung — nur den kommentierten Code ausgeben
- Vorhandene Kommentare beibehalten und ggf. verbessern

## Sprachspezifische Hinweise

### Python
- Ich bin Beginner bis Intermediate — erkläre alles was für einen Einsteiger nicht selbsterklärend ist
- Besonders wichtig: Konzepte die sich von anderen Sprachen unterscheiden (z.B. Unpacking, Context Manager, List Comprehensions, Decorators)

### C
- Ich bin Neuling — erkläre alle nicht-offensichtlichen Konzepte ausführlich
- Besonders wichtig: Alles rund um Speicher und Pointer, da das in Python nicht existiert
- Auf typische Fallstricke hinweisen wenn sie im Code auftauchen könnten

### C++
- Ich bin Neuling mit Python-Hintergrund — erkläre alle Konzepte
- Zum Beispiel die , die in Python kein Äquivalent haben
- Besonders wichtig: Objektorientierung in C++, Speicherverwaltung, Standardbibliothek
- ROS2/rclcpp-spezifische Muster erklären falls vorhanden

## Kontext
Behandle mich nicht als Senior Dev. Kurz aber präzise, kein Filler.
