from Bio.Seq import Seq

# DNA dizilimini oluştur
dna_sequence = Seq("ATGCTAGCGTACGATCGATCGTAGCTAGCTAGCTAGCTAG")

# Dizilimin uzunluğunu hesapla
sequence_length = len(dna_sequence)
print("Dizilim Uzunluğu:", sequence_length)

# Dizilimi transkribe et (DNA -> mRNA)
mRNA_sequence = dna_sequence.transcribe()
print("mRNA Dizilimi:", mRNA_sequence)

# Dizilimi tersine çevir
reverse_sequence = dna_sequence.reverse_complement()
print("Tersine Çevrilmiş Dizilim:", reverse_sequence)

# Belirli bir bölgeleri kes
cut_site = 10
cut_sequence = dna_sequence[:cut_site]
print(f"Kesilmiş Dizilim (0-{cut_site}): {cut_sequence}")

# Belirli bir motifin sayısını say
motif = "CTAG"
motif_count = dna_sequence.count(motif)
print(f"'{motif}' Motifi Sayısı:", motif_count)
