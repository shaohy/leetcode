class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        unique_morse_representations = set()
        for word in words:
            unique_morse_representations.add(self.to_morse(word))
        return len(unique_morse_representations)

    def to_morse(self, word):
        morse_dict = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        output = ""
        for i in word:
            output += morse_dict[ord(i) - 97]
        return output
