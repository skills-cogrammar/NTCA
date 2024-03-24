class ReverseInt():

    def get_reversed_int(self, initial):
        initial = list(str(initial))

        left = 0
        right = len(initial) - 1

        while left < right:
            temp = initial[left]
            initial[left] = initial[right]
            initial[right] = temp

            left += 1
            right -= 1

        if (initial[-1] == '-'):
            return -int(''.join(initial[:-1]))

        return int(''.join(initial))
