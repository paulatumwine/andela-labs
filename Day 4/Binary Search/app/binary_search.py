class BinarySearch(list):

    def __init__(self, a, b):

        list.__init__(self)

        counter = 1
        while counter <= a:
            step = counter * b
            self.append(step)
            counter += 1

        self.length = a

    def search(self, arg_to_find):

        no_of_iterations = 0
        arg_index = -1
        first = 0
        last = self.length - 1

        if arg_to_find == self[first]:
            return {'count': no_of_iterations, 'index': first}
        elif arg_to_find == self[last]:
            return {'count': no_of_iterations, 'index': last}
        elif arg_to_find not in self:
            return {'count': no_of_iterations, 'index': arg_index}

        while first <= last and arg_index == -1:
            midpoint = (first + last) // 2
            if self[midpoint] == arg_to_find:
                arg_index = midpoint
            else:
                if arg_to_find < self[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
                no_of_iterations += 1

        return {'count': no_of_iterations, 'index': arg_index}
