"""
Принцип единой отвественности заключается в разделении по отдельным классам создание и хранение журнала
и записи журнала в файл
"""


class Journal:
    def __init__(self, entries, count):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, position):
        del self.entries[position]

    def __str__(self):
        return ''.join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()
