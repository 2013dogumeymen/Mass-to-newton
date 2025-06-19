import scipy
import scipy.constants

#startup msg
startup_msg_tr = "Tahmini (sapma vb. hesaplanmamıştır) çekim kuvveti hesaplama"

lang = input("Please select language (tr/en): ").lower()

if lang == "tr" :
    m_gr = float(input("kütle giriniz(gram) :"))

    m_kg = m_gr / 1000

    F = m_kg * scipy.constants.g 

    print(f"{F:,.4f} Newton'luk bir çekim gücü bulunmakta, bu da {m_kg} kilogramlık bir kütleye karşılık gelmektedir.")

elif lang == "en" :
    m_gr = float(input("enter the mass(grams) :"))

    m_kg = m_gr / 1000

    F = m_kg * scipy.constants.g
    
    print(f"{F:,.4f} Newton = {m_kg} kilograms.")

else :
    print("wrong language please tr or english")
    exit()

input("\nÇıkmak için Enter'a basın... / Press Enter to exit...")


