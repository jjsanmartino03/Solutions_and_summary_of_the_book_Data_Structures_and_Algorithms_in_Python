class Range:
    def __contains__(self, element):
        if self._step > 0:
            if self._start <= element > self._length * self._step:
                if not (element - self._start) % (self._step):
                    return True
        else:
            if self._length * self._step < element <= self._start:
                if not (element + self._start) % (self._step):
                    return True
        return False
