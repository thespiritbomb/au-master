from mycroft import MycroftSkill, intent_file_handler


class AuMaster(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('au.schools.intent')
    def handle_block_d_au(self, message):
        self.speak_dialog('There are several different schools under Ansal University . These are School of Engineering and Technology . Sushant School of Art and Architecture . School of Hospitality and Management . Sushant School of Business . School of Law . Sushant School of Design . Sushant School of Health Sciences . and Sushant School of Planning and Development . ')

    @intent_file_handler('dean.set.who.intent')
    def handle_block_d_au(self, message):
        self.speak('Doctor Anamika Paul is the Dean of School of Engineering and Technology . ')

    @intent_file_handler('dean.set.where.intent')
    def handle_block_d_au(self, message):
        self.speak('The Dean office for School of Engineering and Technology is situated in Room number D-302 on the 3rd floor of the D Block . ')
        self.speak_dialog('block.d.au.locate')
    
    @intent_file_handler('program.director.who.intent')
    def handle_block_d_au(self, message):
        self.speak('Doctor Latika Duhan is the Program Director of School of Engineering and Technology . ')
    
    @intent_file_handler('set.ug.courses.intent')
    def handle_block_d_au(self, message):
        self.speak('S.E.T. offers various undergraduate courses . These are B.Tech. in Computer Science and Engineering with specializations available in A.I. , M.L. , I.O.T , blockchain , and Cybersecurity . B.Tech. in Mechanical Engineering with a specialization in Autonomous Vehicles . B.Tech. in Electrical and Electronics Engineering with a specialization in Renewable Energy . and B.Tech. in Civil Engineering . ')
    
    @intent_file_handler('set.electronics.lab.intent')
    def handle_block_d_au(self, message):
        self.speak('The Electronics Lab is situated in Room number D-320 on the 3rd floor of the D Block . ')
        self.speak_dialog('block.d.au.locate')

    @intent_file_handler('set.i.t.lab.intent')
    def handle_block_d_au(self, message):
        self.speak('The I.T. Lab is situated in Room number D-312 on the 3rd floor of the D Block . ')
        self.speak_dialog('block.d.au.locate')

    @intent_file_handler('set.au.locate.intent')
    def handle_block_d_au(self, message):
        self.speak('The School of Engineering and Technology is situated on the 3rd floor of the D Block .')
        self.speak_dialog('block.d.au.locate')

    @intent_file_handler('block.d.au.locate.intent')
    def handle_block_d_au(self, message):
        self.speak_dialog('block.d.au.locate')


def create_skill():
    return AuMaster()