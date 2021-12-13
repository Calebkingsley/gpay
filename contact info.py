import cont

kingsley=cont.cont("kingsley","induvidual","8754554295","lastcontacted")
kingsley.contact_open()
kingsley.name_verificaton()
kingsley.identity_verification()
kingsley.mobile_verification()
kingsley.lastcontected_verification()

class personal_info(cont.cont):
    def __init__(self,name,induvidual,phonenumber,lc):
        super().__init__(name,induvidual,phonenumber,lc)


    def open_personalnfo(self):
        print("personal info")

kingsley=personal_info("kingsley","personal","8754554295","lastcontected")
kingsley.open_personalnfo()
kingsley.name_verificaton()
kingsley.mobile_verification()
kingsley.lastcontected_verification()
                         

contacts=[{"name":"abishek","identity":"friend","mobilenumber":9936304497,"lastcontacted":"more than a week"},
          {"name":"abinaya mam","identity":"professor","mobilenumber":9245555365,"lastcontacted":"2 days ago"},
          {"name":"abinesh","identity":"friend","mobilenumber":6379621613,"lastcontacted":"4 hours ago"},
          {"name":"Abishek football","identity":"friend","mobilenumber":9840237572,"lastcontacted":"more than a month"},
          {"name":"aditiya","identity":"friend","mobilenumber":9962929509,"lastcontacted":"more than a week"},
          {"name":"agent akash","identity":"friend","mobilenumber":9884180922,"lastcontacted":"more than a week"},
          {"name":"agent akash","identity":"friend","mobilenumber":9884180922,"lastcontacted":"not yet called"},
          {"name":"appa","identity":"family","mobilenumber":9444704367,"lastcontacted":"more than a week"},
          {"name":"aswin rijo","identity":"friend","mobilenumber":9487449443,"lastcontacted":"before 6 hours"},
          {"name":"bala","identity":"friend","mobilenumber":7448729735,"lastcontacted":"more than a week"},
          {"name":"bercial","identity":"family","mobilenumber":7358142225,"lastcontacted":"more than a month"},
          {"name":"barath","identity":"friend","mobilenumber":7092028571,"lastcontacted":"more than a month"},
          {"name":"bhuvanesh","identity":"friend","mobilenumber":94865531514,"lastcontacted":"2 weeks ago"},
          {"name":"bharath disys","identity":"family","mobilenumber":984412975,"lastcontacted":"a day ago"},
          {"name":"bryan","identity":"friend","mobilenumber":97104667134,"lastcontacted":"more than a year"},
          {"name":"chitti","identity":"family","mobilenumber":9003295352,"lastcontacted":"more than a month"},
          {"name":"damodharan","identity":"riend","mobilenumber":9486889280,"lastcontacted":"more than 2 months"},
          {"name":"deepak disys","identity":"friend","mobilenumber":9843130762,"lastcontacted":"2 days ago"},
          {"name":"derick","identity":"friend","mobilenumber":6383173625,"lastcontacted":"more than a month"},
          {"name":"dhanuskodi","identity":"friend","mobilenumber":9884836245,"lastcontacted":"2 days ago"},
          {"name":"dinesh","identity":"friend","mobilenumber":9384211231,"lastcontacted":"more than a year"},
          {"name":"dinesh","identity":"friend","mobilenumber":9962734252,"lastcontacted":"1 hour ago"},
          {"name":"emimal","identity":"friend","mobilenumber":9940564975,"lastcontacted":"more than a month"},
          {"name":"evangelin","identity":"friend","mobilenumber":9677267626,"lastcontacted":"more than a year"},
          {"name":"ezra","identity":"friend","mobilenumber":7358605268,"lastcontacted":"more than a month"},
          {"name":"ganesh","identity":"friend","mobilenumber":8939450651,"lastcontacted":"more than 2 month"},
          {"name":"gamnesh clg","identity":"friend","mobilenumber":8124872730,"lastcontacted":"more than a month"},
          {"name":"gokul","identity":"friend","mobilenumber":9444234317,"lastcontacted":"more than a month"},
          {"name":"gurudoss","identity":"famil friend","mobilenumber":93807447737,"lastcontacted":"more than a month"},
          {"name":"haanah","identity":"friend","mobilenumber":960758882,"lastcontacted":"a month ago"},
          {"name":"hari haran","identity":"friend","mobilenumber":9790464335,"lastcontacted":"more than a month"},
          {"name":"harrikrishanan","identity":"friend","mobilenumber":8610408567,"lastcontacted":"more than a week"},
          {"name":"hod cse","identity":"professor","mobilenumber":9894204992,"lastcontacted":"2 days ago"},
          {"name":"immaculate","identity":"friend","mobilenumber":9500700199,"lastcontacted":"more than a year"},
          {"name":"immanuael","identity":"schoolfriend","mobilenumber":6379165794,"lastcontacted":"5 minutes ago"},
          {"name":"jagan","identity":"friend","mobilenumber":6385733012,"lastcontacted":"more than a week"},
          {"name":"jaswanth","identity":"friend","mobilenumber":89394992,"lastcontacted":"more than a week"},
          {"name":"jeffery officail","identity":"friend","mobilenumber":9941013193,"lastcontacted":"1 hour ago"},
          {"name":"jeffrey bro","identity":"friend brother","mobilenumber":9941072962,"lastcontacted":"more than a week"},
          {"name":"jegan bro","identity":" family friend","mobilenumber":93611151281,"lastcontacted":"more than a week"},
          {"name":"jeni ece","identity":"friend","mobilenumber":7305506899,"last contacted":"2 hours ago"},
          {"name":"jeremy","identity":"friend","mobilenumber":7871436021,"last contacted":"more than a month"},
          {"name":"jerry chitti","identity":"family","mobilenumber":96001062065,"last contacted":"more than a week"},
          {"name":"jeruson alpha","identity":"friend","mobilenumber":7338958234,"last contacted":"more than 2 week"},
          {"name":" jo winston","identity":"friend","mobilenumber":7904707618,"last contacted":"more than a week"},
          {"name":"joel","identity":"friend","mobilenumber":7092485812,"last contacted":"more than a month"},
          {"name":"jonathan","identity":"friend","mobilenumber":8072615542,"last contacted":"more than 2 weeks"},
          {"name":"jones","identity":"friend","mobilenumber":8072615954,"last contacted":"more than a week"},
          {"name":"jonna","identity":"family friend","mobilenumber":8754531304,"last contacted":"more than 3 week"},
          {"name":"jaswanth","identity":"friend","mobilenumber":89394992,"last contacted":"more than a week"},
          {"name":"josh","identity":"family","mobilenumber":805625165,"last contacted":"more than 3 week"},
          {"name":"josh kumar","identity":"friend","mobilenumber":97898669415,"last contacted":"more than a week"},
          {"name":"joshua samuel","identity":"friend","mobilenumber":6379696243,"last contacted":"more than a month"},
          {"name":"jp","identity":"friend","mobilenumber":9952070148,"last contacted":"2 weeks"},
          {"name":"karthi","identity":"friend","mobilenumber":6382569638,"last contacted":"more than a week"},
          {"name":"karthi clg","identity":"friend","mobilenumber":6379845953,"last contacted":"more than 2 month"},
          {"name":"karthikeyan disys","identity":"friend","mobilenumber":8778799456,"last contacted":"more than a week"},
          {"name":"kavinilavan","identity":"friend","mobilenumber":6383252563,"last contacted":"more than 2 week"},
          {"name":"kevin class","identity":"friend","mobilenumber":9840862616,"last contacted":"more than a month"},
          {"name":"khalid","identity":"friend","mobilenumber":98412045515,"last contacted":"more than a month"},
          {"name":"kiran","identity":"friend","mobilenumber":9940327375,"last contacted":"more than a week"},
          {"name":"kishore","identity":"friend","mobilenumber":6381397241,"last contacted":"more than a week"},
          {"name":"kutti","identity":"friend","mobilenumber":9884932375,"last contacted":"more than a week"},
          {"name":"kumaraa","identity":"church friend","mobilenumber":7339092746,"last contacted":"more than a week"},
          {"name":"lokash","identity":"friend","mobilenumber":9566265635,"last contacted":"more than a week"},
          {"name":"madhan","identity":"friend","mobilenumber":938420404504,"last contacted":"more than a month"},
          {"name":"madhumita","identity":"friend","mobilenumber":6369747170,"last contacted":"more than a week"},
          {"name":"magesh","identity":"friend","mobilenumber":9840219225,"last contacted":"more than a month"},
          {"name":"magimaimay","identity":"family","mobilenumber":7395995610,"last contacted":"more than a year"},
          {"name":"mahalaxmi disys","identity":"friend","mobilenumber":9092042867,"last contacted":"more than a week"},
          {"name":"manager","identity":"friend","mobilenumber":9176672932,"last contacted":"more than 2 week"},
          {"name":"mark","identity":"friend","mobilenumber":7338820316,"last contacted":"more than 1 week"},
          {"name":"mervin","identity":"friend","mobilenumber":7338892332,"last contacted":"more than a month"},
          {"name":"mukilan","identity":"friend","mobilenumber":9543637589,"last contacted":"1 hour ago"},
          {"name":"mirthul","identity":"friend","mobilenumber":7338948324,"last contacted":"more than a week"},
          {"name":"mohit","identity":"friend","mobilenumber":9677116132,"last contacted":"more than 2 month"},
          {"name":"mowri","identity":"friend","mobilenumber":8610044972,"last contacted":"more than a month"},
          {"name":"muthu","identity":"friend","mobilenumber":8754420124,"last contacted":"more than a month"},
          {"name":"nalini aunty","identity":"family friend","mobilenumber":9790586799,"last contacted":"more than a week"},
          {"name":"naren clg","identity":"friend","mobilenumber":7010123291,"last contacted":"more than a month"},
          {"name":"naresh","identity":"friend","mobilenumber":9445809767,"last contacted":"more than 2 week"},
          {"name":"naveen","identity":"friend","mobilenumber":8838329320,"last contacted":"more than a week"},
          {"name":"naveen A","identity":"friend","mobilenumber":7358662015,"last contacted":"more than a month"},
          {"name":"nivetha clg","identity":"friend","mobilenumber":9047083789,"last contacted":"more than a month"},
          {"name":"paramasivam","identity":"friend","mobilenumber":9003027068,"last contacted":"more than a month"},
          {"name":"jaswanth","identity":"friend","mobilenumber":89394992,"last contacted":"more than a week"},
          {"name":"pataatsu","identity":"friend","mobilenumber":6374218156,"last contacted":"more than a month"},
          {"name":"paul joshua","identity":"friend","mobilenumber":8667361540,"last contacted":"more than a year"},
          {"name":"philip","identity":"friend","mobilenumber":9841141106,"last contacted":"more than a week"},
          {"name":"paul raj paul","identity":"friend","mobilenumber":9047359318,"last contacted":"more than a month"},
          {"name":"prakash","identity":"friend","mobilenumber":83000059773,"last contacted":"more than a month"},
          {"name":"praveen disys","identity":"friend","mobilenumber":9944039137,"last contacted":"more than a week"},
          {"name":"pravin","identity":"friend","mobilenumber":8682985598,"last contacted":"more than a week"},
          {"name":"priya","identity":"friend","mobilenumber":7397421851,"last contacted":"more than a week"},
          {"name":"rahul","identity":"friend","mobilenumber":89394992,"last contacted":"more than a week"},
          {"name":"rahul friend","identity":"friend","mobilenumber":7010974681,"last contacted":"more than a month"},
          {"name":"raja surender","identity":"friend","mobilenumber":9566602815,"last contacted":"more than 2 weeks"},
          {"name":"ravi","identity":"friend","mobilenumber":6379494371,"last contacted":"more than a month"},
          {"name":"rayan","identity":"friend","mobilenumber":7550139326,"last contacted":"more than a month"},
          {"name":"revthi","identity":"friend","mobilenumber":99449678976,"last contacted":"more than a month"},
          {"name":"rishinth","identity":"friend","mobilenumber":87544485415,"last contacted":"more than a month"},
          {"name":"ritesh disys","identity":"friend","mobilenumber":8190092281,"last contacted":"more than a month"},
          {"name":"ronald","identity":"friend","mobilenumber":763292020,"last contacted":"more than 2 years"},
          {"name":"roy","identity":"friend","mobilenumber":90039585514,"last contacted":"more than a month"},
          {"name":"ruby","identity":"friend","mobilenumber":9176027339,"last contacted":"more than a month"},
          {"name":"ryan","identity":"friend","mobilenumber":89394992,"last contacted":"more than a month"},
          {"name":"S K","identity":"friend","mobilenumber":9150729213,"last contacted":"more than a month"},
          {"name":"sam","identity":"friend","mobilenumber":6379912550,"last contacted":"more than 3 week"},
          {"name":"sanjay","identity":"friend","mobilenumber":6380917560,"last contacted":"more than a month"},
          {"name":"saravana anna","identity":"family friend","mobilenumber":80157244633,"last contacted":"more than a month"},
          {"name":"satish kumar","identity":"profeesor","mobilenumber":8760430744,"last contacted":"4 days ago"},
          {"name":"selvi aunty","identity":"family friend","mobilenumber":8825761271,"last contacted":"more than a month"},
          {"name":"sheeba","identity":"friend","mobilenumber":9789875820,"last contacted":"more than a month"},
          {"name":"shelcia","identity":"friend","mobilenumber":7397308623,"last contacted":"more than a month"},
          {"name":"sheryl","identity":"friend","mobilenumber":7904125152,"last contacted":"more than a month"},
          {"name":"shri hari","identity":"friend","mobilenumber":9790940523,"last contacted":"more than a month"},
          {"name":"simon","identity":"friend","mobilenumber":9840153328,"last contacted":"more than a month"},
          {"name":"siva","identity":"friend","mobilenumber":9840609549,"last contacted":"more than a week"},
          {"name":"sreeman","identity":"friend","mobilenumber":9884410380,"last contacted":"more than a month"},
          {"name":"subash","identity":"friend","mobilenumber":9655953984,"last contacted":"more than a week"},
          {"name":"sudhharar","identity":"professor","mobilenumber":9445188130,"last contacted":"more than a month"},
          {"name":"suriya","identity":"friend","mobilenumber":8056065964,"last contacted":"more than a year"},
          {"name":"tripati","identity":"friend","mobilenumber":8015200513,"last contacted":"more than a month"},
          {"name":"vasanth","identity":"friend","mobilenumber":9126210184,"last contacted":"more than a month"},
          {"name":"vicky","identity":"friend","mobilenumber":9791469723,"last contacted":"more than a week"},
          {"name":"viyash","identity":"friend","mobilenumber":8072935308,"last contacted":"more than a month"},
          {"name":"yowan","identity":"friend","mobilenumber":9940016192,"last contacted":"more than a month"},
          {"name":"zack ark","identity":"family friend","mobilenumber":95001533475,"last contacted":"more than a week"}]


for i in contacts:
    for j,k in i.items():
        print(f"{j}:{k}")
            
        




          
          
          
          
          



