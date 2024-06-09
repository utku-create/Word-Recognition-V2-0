import speech_recognition as sr

def sesi_kaydet():
    r = sr.Recognizer()

    with sr.Microphone() as kaynak:
        print("Dinliyorum...")
        ses = r.listen(kaynak)

        söylenen_cümle = ""
        dil = "tr"  # Varsayılan dil Türkçe

        try:
            # Türkçe olarak tanımaya çalış
            söylenen_cümle = r.recognize_google(ses, language="tr-TR")
            print("Söylenen cümle (Türkçe):", söylenen_cümle)
            dil = "tr"
        except sr.UnknownValueError:
            pass  # Türkçe olarak anlayamadık
        except sr.RequestError:
            print("Üzgünüm, servisle ilgili bir problem var (Türkçe).")

        if not söylenen_cümle:
            try:
                # İngilizce olarak tanımaya çalış
                söylenen_cümle = r.recognize_google(ses, language="en-US")
                print("Söylenen cümle (İngilizce):", söylenen_cümle)
                dil = "en"
            except sr.UnknownValueError:
                pass  # İngilizce olarak anlayamadık
            except sr.RequestError:
                print("Üzgünüm, servisle ilgili bir problem var (İngilizce).")
            except Exception as e:
                print("Bir hata oluştu: " + str(e))

        if not söylenen_cümle:
            try:
                # Fransızca olarak tanımaya çalış
                söylenen_cümle = r.recognize_google(ses, language="fr-FR")
                print("Söylenen cümle (Fransızca):", söylenen_cümle)
                dil = "fr"
            except sr.UnknownValueError:
                pass  # Fransızca olarak anlayamadık
            except sr.RequestError:
                print("Üzgünüm, servisle ilgili bir problem var (Fransızca).")
            except Exception as e:
                print("Bir hata oluştu: " + str(e))

        if not söylenen_cümle:
            try:
                # İspanyolca olarak tanımaya çalış
                söylenen_cümle = r.recognize_google(ses, language="es-ES")
                print("Söylenen cümle (İspanyolca):", söylenen_cümle)
                dil = "es"
            except sr.UnknownValueError:
                pass  # İspanyolca olarak anlayamadık
            except sr.RequestError:
                print("Üzgünüm, servisle ilgili bir problem var (İspanyolca).")
            except Exception as e:
                print("Bir hata oluştu: " + str(e))

    return söylenen_cümle, dil

# Kontrol edilecek kelimelerin listesi
kelime_listesi = ["yardım", "destek", "imdat",
                  "acil", "kurtarın", "beni duyan var mı", "sesimi duyan var mı",
                  "yardıma ihtiyacım var", "hey", "help", "trapped", "emergency",
                  "rescue", "injured", "stuck", "save", "need", "aid", "urgent","Aide", "Urgent",
                  "Sauvez-moi", "Danger", "Pompier",
                  "Ambulance", "Aidez-moi", "S'il vous plaît", "Blessé", "Perdu","ayuda", "agua", "comida",
                  "medicina", "rescate", "refugio", "familia", "emergencia", "salud", "comunicación"]

while True:
    yazı, dil = sesi_kaydet()

    for kelime in kelime_listesi:
        if kelime.lower() in yazı.lower():
            print(f"'{kelime}' kelimesi tanındı!")

    if "çıkış" in yazı.lower() or "exit" in yazı.lower():
        if dil == "tr":
            print("Program Türkçe olarak sonlandırılıyor.")
        elif dil == "en":
            print("Program İngilizce olarak sonlandırılıyor.")
        elif dil == "fr":
            print("Program Fransızca olarak sonlandırılıyor.")
        else:
            print("Program İspanyolca olarak sonlandırılıyor.")
        break
