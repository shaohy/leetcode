class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        trans_set = set()
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        for word in words:
            morse_letter = ""
            for letter in word:
                index_of_letter = ord(letter) - 97
                morse_letter += morse_code[index_of_letter]
            trans_set.add(morse_letter)
        return len(trans_set)
