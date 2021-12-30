class AddOps:

    def __init__(self, **kwargs) -> None:
        self.params = {}
        self.params.update(kwargs)


    @staticmethod
    def __run_impl(left, right):
        return left + right

    
    def run(self):
        left = self.params["left"]
        right = self.params['right']
        return AddOps.__run_impl(left, right)


class SefDefOps:

    def __init__(self, **kwargs) -> None:
        self.params = {}
        self.params.update(kwargs)


    @staticmethod
    def __run_impl(num_1, num_2, num_3):
        return num_1 + num_2 + num_3

    
    def run(self):
        num_1 = self.params['num_1']
        num_2 = self.params['num_2']
        num_3 = self.params['num_3']
        return AddOps.__run_impl(num_1, num_2, num_3)

