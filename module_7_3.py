class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = [*file_name]
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        words = []
        str_punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as opener:
                for line in opener:
                    line = line.lower()
                    for p in str_punctuation:
                        if p in line:
                            line = line.replace(p, ' ')
                    split_line = line.split(sep=' ')
                    words.append(split_line)
        sorted_list = [x for y in words for x in y]
        all_words[self.file_name] = sorted_list
        return all_words

    def find(self, word):
        dict_ = self.get_all_words()
        list_ = []
        for name, words in dict_.items():
            for w in words:
                if word.lower() in w:
                    index = words.index(w)
                    list_.append(self.file_name)
                    list_.append(index+1)
                    break
        return list_

    def count(self, word):
        dict_ = self.get_all_words()
        list_ = []
        count = 0
        for name, words in dict_.items():
            for w in words:
                if word.lower() in w:
                    count += 1
        list_.append(self.file_name)
        list_.append(count)
        return list_


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

