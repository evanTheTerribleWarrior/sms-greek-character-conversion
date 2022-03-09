# If you are sending out many SMSes, you should not need to do this conversion for each SMS. 
#You could do it once, store this message in your database and then send it out to many destinations in this new format


import binascii
gsm = ("@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ\x1bÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?"
       "¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà")
ext = ("````````````````````^```````````````````{}`````\\````````````[~]`"
       "|````````````````````````````````````€``````````````````````````")

#These two lists hold static codes for the same letters on the same positions so it's easy to replace

# A, B, E, Z, H, I, K, M, N, O, P, T, Y, X
greek_code = [913,914,917,918,919,921,922,924,925,927,929,932,933,935]
english_code = [65,66,69,90,72,73,75,77,78,79,80,84,89,88]

final_array = []
def gsm_encode(message):
	for c in message:
		idx = gsm.find(c);
		if idx == -1:
			code_index = greek_code.index(ord(c))
			final_array.append(chr(english_code[code_index]))
		else:
			final_array.append(c)
            
            
text = "ΑΥΤΟ ΤΟ ΜΗΝΥΜΑ ΠΡΕΠΕΙ ΝΑ ΣΤΑΛΕΙ ΣΕ GSM ΚΑΙ ΟΧΙ ΣΕ ΚΑΤΙ ΑΛΛΟ. ΓΡΑΦΩ ΚΙ ΑΛΛΟΥΣ ΧΑΡΑΚΤΗΡΕΣ ΓΙΑ ΝΑ ΞΕΠΕΡΑΣΩ ΤΟ ΟΡΙΟ ΤΟΥ UCS2."

gsm_encode(text)
#print(final_array)
gsm_message = ''.join(final_array)
print(gsm_message)
