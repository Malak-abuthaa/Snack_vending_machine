class Execptions(Exception):
    @staticmethod
    def note_exception():
        Exception ('unable to collect money, machine accept only 20$ 50$ in Note Slot')

    @staticmethod
    def slot_exception():
        Exception('unable to collect money, machine accept only 1$ in coin slot')

    @staticmethod
    def currency_exception():
        Exception('unable to collect money, machine accept only USD Currency')

    @staticmethod
    def slot_c_exception():
        Exception('unable to collect money, machine accept only 10c 20c 50c')
