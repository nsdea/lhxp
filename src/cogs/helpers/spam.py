def is_spam(text):
    sample_count = 10
    sample = text[:sample_count]

    return text.count(sample) >= 3

if __name__ == '__main__':
    print(is_spam("""Dieser PC erfüllt derzeit nicht alle Systemanforderungen für Windows 11.
Wie du trotzdem Windows 11 installieren kannst und wenn nötig wie man die TPM Sperre umgehen kann oder auch wie du die CPU Sperre umgehst. Das zeige ich Dir in diesem Video.

Bei vielen erscheint häufig die Meldung, dass der PC oder das Notebook
nicht die Anforderung erfüllt. Microsoft sagt, wenn man die Installation trotzdem durchführt, dann wird nicht garantiert, dass Du Updates für Windows 11 erhältst. Ich habe das getestet, mehr dazu im Video. 

!!!!!!!! BITTE BEACHTEN
- genau gucken: nicht die appraiser.dll löschen... sondern die appraiserres.dll
- Bei der Installation den Haken bei "an den Verbesserungen teilnehmen." rausnehmen... 
- oder kurz LAN bzw. WLAN deaktivieren
!!!!!!!! Es geht sonst nicht
Dieser PC erfüllt derzeit nicht alle Systemanforderungen für Windows 11.
Wie du trotzdem Windows 11 installieren kannst und wenn nötig wie man die TPM Sperre umgehen kann oder auch wie du die CPU Sperre umgehst. Das zeige ich Dir in diesem Video.

Bei vielen erscheint häufig die Meldung, dass der PC oder das Notebook
nicht die Anforderung erfüllt. Microsoft sagt, wenn man die Installation trotzdem durchführt, dann wird nicht garantiert, dass Du Updates für Windows 11 erhältst. Ich habe das getestet, mehr dazu im Video. 

!!!!!!!! BITTE BEACHTEN
- genau gucken: nicht die appraiser.dll löschen... sondern die appraiserres.dll
- Bei der Installation den Haken bei "an den Verbesserungen teilnehmen." rausnehmen... 
- oder kurz LAN bzw. WLAN deaktivieren
!!!!!!!! Es geht sonst nicht
Dieser PC erfüllt derzeit nicht alle Systemanforderungen für Windows 11.
Wie du trotzdem Windows 11 installieren kannst und wenn nötig wie man die TPM Sperre umgehen kann oder auch wie du die CPU Sperre umgehst. Das zeige ich Dir in diesem Video.

Bei vielen erscheint häufig die Meldung, dass der PC oder das Notebook
nicht die Anforderung erfüllt. Microsoft sagt, wenn man die Installation trotzdem durchführt, dann wird nicht garantiert, dass Du Updates für Windows 11 erhältst. Ich habe das getestet, mehr dazu im Video. 

!!!!!!!! BITTE BEACHTEN
- genau gucken: nicht die appraiser.dll löschen... sondern die appraiserres.dll
- Bei der Installation den Haken bei "an den Verbesserungen teilnehmen." rausnehmen... 
- oder kurz LAN bzw. WLAN deaktivieren
!!!!!!!! Es geht sonst nicht
"""))