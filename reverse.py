class string_reverse:
    def __init__(self, word):
     self._word = word
     def reverse(self):
        return self._word[::-1]
reversal_string = string_reverse("CODING")
print(reversal_string.reverse())