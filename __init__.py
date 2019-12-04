from mycroft import MycroftSkill, intent_file_handler


class AuMaster(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('au.schools.intent')
    def handle_au_schools(self, message):
        self.speak('There are several different schools under Ansal University . These are School of Engineering and Technology . Sushant School of Art and Architecture . School of Hospitality and Management . Sushant School of Business . School of Law . Sushant School of Design . Sushant School of Health Sciences . and Sushant School of Planning and Development . ')

    @intent_file_handler('dean.set.who.intent')
    def handle_dean_set_who(self, message):
        self.speak('Doctor Anamika Paul is the Dean of School of Engineering and Technology . ')

    @intent_file_handler('dean.set.where.intent')
    def handle_dean_set_where(self, message):
        self.speak('The Dean office for School of Engineering and Technology is situated in Room number D-302 on the 3rd floor of the D Block . ')
        self.speak_dialog('block.d.au.locate')
    
    @intent_file_handler('program.director.who.intent')
    def handle_program_director_who(self, message):
        self.speak('Doctor Latika Duhan is the Program Director of School of Engineering and Technology . ')
    
    @intent_file_handler('set.ug.courses.intent')
    def handle_set_ug_courses(self, message):
        self.speak('S.E.T. offers various undergraduate courses . These are B.Tech. in Computer Science and Engineering with specializations available in A.I. , M.L. , I.O.T , blockchain , and Cybersecurity . B.Tech. in Mechanical Engineering with a specialization in Autonomous Vehicles . B.Tech. in Electrical and Electronics Engineering with a specialization in Renewable Energy . and B.Tech. in Civil Engineering . ')
    
    @intent_file_handler('set.electronics.lab.intent')
    def handle_set_electronics_lab(self, message):
        self.speak('The Electronics Lab is situated in Room number D-320 on the 3rd floor of the D Block . ')
        self.speak_dialog('block.d.au.locate')

    @intent_file_handler('set.i.t.lab.intent')
    def handle_set_i_t_lab(self, message):
        self.speak('The I.T. Lab is situated in Room number D-312 on the 3rd floor of the D Block . ')
        self.speak_dialog('block.d.au.locate')

    @intent_file_handler('set.chem.lab.intent')
    def handle_set_chem_lab(self, message):
        self.speak('The Chemistry Lab is situated in Room number D-212 on the 2nd floor of the D Block . ')
        self.speak_dialog('block.d.au.locate')

    @intent_file_handler('set.clubs.intent')
    def handle_set_clubs(self, message):
        self.speak('The school of engineering and technology has various clubs . These are Cultural Club . Sports Club . Social Welfare club . and Computer Society of India . ')

    @intent_file_handler('set.au.locate.intent')
    def handle_set_au_locate(self, message):
        self.speak('The School of Engineering and Technology is situated on the 3rd floor of the D Block .')
        self.speak_dialog('block.d.au.locate')

    @intent_file_handler('block.d.au.locate.intent')
    def handle_block_d_au_locate(self, message):
        self.speak_dialog('block.d.au.locate')
        self.gui.show_image('https://i.imgur.com/ywF4omt.png')

    @intent_file_handler('canteen.au.locate.intent')
    def handle_canteen_au_locate(self, message):
        self.speak('Exit the reception and take a right . walk straight for 5 meters and take a right. walk straight for 17 meters . The canteen will be right ahead of you . ')

    @intent_file_handler('volleyball.au.locate.intent')
    def handle_volleyball_au_locate(self, message):
        self.speak('Exit the reception and take a right . walk straight for 25 meters until you reach the food stalls . Take a right . The volleyball court will be right ahead of you . ')

    @intent_file_handler('law.au.locate.intent')
    def handle_law_au_locate(self, message):
        self.speak('Exit the reception and take a right . walk straight for 20 meters and take a right . walk straight for 450 meters . The law block will be right ahead of you . ')

    @intent_file_handler('hostels.au.locate.intent')
    def handle_hostels_au_locate(self, message):
        self.speak('Exit the reception and take a right . walk straight for 20 meters and take a right . walk straight for 450 meters . The hostels will be to your right . ')


def create_skill():
    return AuMaster()
