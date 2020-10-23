class TreatData():

    @staticmethod
    def handle_keys(data):
        item = data.split(':')

        key = item[0].replace(" ", "_").lower()

        if len(item) > 1:
            return {
                f'{key}': item[1]
            }

    @staticmethod
    def avoid_keys(data):
        res_list = [i for n, i in enumerate(data) if i not in data[n + 1:]]
        new_list = []

        avoid_words = ['historysearch_for',
                       'search_for', 'parent_companysearch_for']

        for i in range(len(res_list)):
            if res_list[i] is not None:
                if list(res_list[i].keys())[0] not in avoid_words:
                    new_list.append(res_list[i])

        return new_list
