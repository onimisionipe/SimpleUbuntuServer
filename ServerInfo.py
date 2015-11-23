class Info:

    def __init__(self, get):
        self.get = get

    def get_info(self):
        if self.get.lower() == 'uid':
            return '0x00000000'
        if self.get.lower() == 'heap':
            return '0x8000-0x1000000'
        if self.get.lower() == 'name':
            return 'Simple Server'
        if self.get.lower() == 'about':
            return 'Linux Version'
        if self.get.lower() == 'ver':
            return '1.19.05'
        if self.get.lower() == 'date':
            return '19/10/2015'
        if self.get.lower() == 'by':
            return 'Xrobot'
        if self.get.lower() == 'mail':
            return 'javaxrobot@gmail.com'
