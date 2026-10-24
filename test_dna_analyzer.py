import unittest
from dna_analyzer import (
    validate_dna,
    count_nucleotide,
    length_calculate,
    calculate_gc_content,
    transcribe_dna_to_rna,
    reverse_complement,
    find_motif,
    calculate_hamming_distance,
)

class TestValidateDNA(unittest.TestCase):
    def test_valid_dna(self):
        self.assertTrue(validate_dna("ATGC"))
    def test_invalid_dna(self):
        self.assertFalse(validate_dna("ATGX"))
    def test_empty_dna(self):
        self.assertFalse(validate_dna(""))
    def test_lowercase_dna(self):
        self.assertTrue(validate_dna("atgc"))
    def test_dna_with_outer_spaces(self):
        self.assertTrue(validate_dna(" atgc "))            
    def test_dna_with_internal_spaces(self):
        self.assertFalse(validate_dna("AT GC"))


class TestCountNucleotide(unittest.TestCase):
    def test_count_nucleotides(self):
        self.assertEqual(count_nucleotide("AATGC"),{"A": 2, "T": 1, "G": 1, "C": 1})
    def test_count_lowercase_dna(self):
        self.assertEqual(count_nucleotide("aatgc"),{"A": 2, "T": 1, "G": 1, "C": 1})


class TestLengthCalculate(unittest.TestCase):
    def test_normal_length(self):
        self.assertEqual(length_calculate("ATGC"), 4)
    def test_empty_length(self):
        self.assertEqual(length_calculate(""), 0)


class TestGCContent(unittest.TestCase):
    def test_known_gc_percentage(self):
        self.assertAlmostEqual(calculate_gc_content("GGCCAT"), 66.6667, places=3)
    def test_lowercase_gc(self):
        self.assertAlmostEqual(calculate_gc_content("ggccat"), 66.6667, places=3)
    def test_empty_gc(self):
        self.assertEqual(calculate_gc_content(""), 0.0)


class TestTranscription(unittest.TestCase):
    def test_transcribe_dna(self):
        self.assertEqual(transcribe_dna_to_rna("ATGC"), "AUGC")
    def test_transcribe_lowercase_dna(self):
        self.assertEqual(transcribe_dna_to_rna("atgc"), "AUGC")


class TestReverseComplement(unittest.TestCase):
    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("ATGC"), "GCAT")
    def test_reverse_complement_lowercase(self):
        self.assertEqual(reverse_complement("atgc"), "GCAT")


class TestFindMotif(unittest.TestCase):
    def test_motif_positions(self):
        self.assertEqual(find_motif("ATATAT", "AT"), [1, 3, 5])
    def test_motif_not_found(self):
        self.assertEqual(find_motif("ATGC", "AAA"), [])
    def test_overlapping_motifs(self):
        self.assertEqual(find_motif("AAAAA", "AAA"), [1, 2, 3])


class TestHammingDistance(unittest.TestCase):
    def test_equal_length_sequences(self):
        self.assertEqual(calculate_hamming_distance("GAGCCT", "CATCGT"), 3)
    def test_unequal_length_sequences(self):
        self.assertIsNone(calculate_hamming_distance("ATGC", "ATG"))
    def test_hamming_lowercase(self):
        self.assertEqual(calculate_hamming_distance("atgc", "ATGT"), 1)    

if __name__ == "__main__":
    unittest.main()