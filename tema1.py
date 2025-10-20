#Rezolvare tema 1

articol = """La mai bine de 2.200 de ani de la moartea sa, unul dintre cei mai influenți și evazivi filosofi ai Antichității vorbește din nou.
Folosind o tehnică inovativă de imagistică, cercetătorii italieni au citit părți dintr-un sul de papirus carbonizat care deveniseră ilizibile
în urma celui mai notoriu dezastru natural care a lovit lumea clasică: erupția vulcanului Vezuviu în anul 79 d.Hr, potrivit The Times.
Rezultatele au dezvăluit noi detalii despre viața lui Zenon din Citium, fondatorul Stoicismului, ale cărui învățături despre rațiune și reziliență
au modelat gândirea occidentală. Zenon, care a trăit între anii 334 î.Hr. și 262 î.Hr., a propovăduit că viața bună se dobândește prin rațiune,
virtute și stăpânire de sine emoțională. El a ținut prelegeri de sub o colonadă pictată în Atena - stoa poikilē, de unde și-a luat numele școlii sale.
De aici a apărut o filosofie care a modelat gândirea unei mulțimi de romani eminenți, inclusiv Cicero, Seneca și Marcus Aurelius, și care răsună și astăzi.
Detalii noi despre viața și ideile sale au ieșit la iveală după ce oamenii de știință au folosit o nouă tehnică, o formă de imagistică termică,
pentru a citi un sul de papirus carbonizat. Pasajele recent lizibile provin din „Istoria Stoa” de Filodemos din Gadara, scrisă între aproximativ 75 și 50 î.Hr.
Acestea oferă imagini rare despre Zenon. Emigrat fenician la Atena, el este portretizat ca fiind fragil din cauza unei diete sărace, singuratic până la punctul
de misantropie și batjocorit pentru accentul său străin. Cel mai cunoscut tratat al său, Republica, cunoscut mult timp doar prin reputație,
este „îndoielnic din punct de vedere moral, pentru că recomandă practici sociale și sexuale considerate jenante”, a declarat Graziano Ranocchia
de la Universitatea din Pisa, care a condus proiectul. Ideile „jenante” includeau respingerea căsătoriei și a vieții de familie, împărțirea partenerilor,
egalitatea dintre bărbați și femei și toleranța relațiilor între persoane de același sex desfășurate în mod deschis. Utopia lui Zenon își imagina
o comunitate de înțelepți conduși doar de rațiune, fără bani, tribunale sau proprietăți. În Atena secolului al IV-lea î.Hr., astfel de noțiuni păreau indecente,
iar mai târziu stoicii le-au înăbușit în liniște. Totuși, în ciuda ridicolului, faima lui Zenon era de așa natură încât atenienii l-au onorat
cu o înmormântare publică, un tribut rar pentru un străin."""
#cerinta 1
print("Cerinta 1: \n\n\n")
print(articol)
middle=len(articol)//2
prima_jumatate=articol[:middle]
print(prima_jumatate)
adoua_jumatate=articol[middle:]
print(adoua_jumatate)

#cerinta 2
print("\n\n\n Cerinta 2: \n\n\n")
prima_jumatate=prima_jumatate.upper()
print(prima_jumatate)
prima_jumatate=prima_jumatate.strip()
print(prima_jumatate)

#cerinta 3
print("\n\n\n Cerinta 3 \n\n\n")
adoua_jumatate=adoua_jumatate[::-1]
print(adoua_jumatate)
adoua_jumatate=adoua_jumatate[0].upper() + adoua_jumatate[1:]
print(adoua_jumatate)
adoua_jumatate=adoua_jumatate.replace(".", "")
adoua_jumatate=adoua_jumatate.replace(",", "")
adoua_jumatate=adoua_jumatate.replace("!", "")
adoua_jumatate=adoua_jumatate.replace("?", "")
final=prima_jumatate + adoua_jumatate
print(final)