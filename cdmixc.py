'''用于检查租户业绩上传情况以及是否格式正确。

成都万象城 2015年07月06日
'''
import os, sys, time, platform, urllib, urllib.request, urllib.parse, time


path = "/mnt/资料/mixc_Interface tenants_2016.06.20" #默认搜索路径
shopdb="shopno.txt" #店铺名称数据库
marketing_manager = "cd0189" #运营主管在成都OA帐号

filelist = [] #文件列表
emptypath=[] #空目录，视为未上传业绩租户
shoppos=dict()
filecount = 0 #文件总数量
sp="/"
SystemType = "UNKNOWEN"
SystemBit = "UNKNOWEN"
emptylist=""

def _ReadShopNo():
    with open(shopdb, mode='rt', encoding='UTF-8') as shopfile:
        for line in shopfile.readlines():
            line=line.strip('\n')
            a, b=line.split("\t")
            #for number, shop in line:
            shoppos[a]=b
            #print(shoppos)

def _getSystem():
    (SystemBit, SystemType)=platform.architecture()
    
    if SystemType=='ELF':
        os.system("clear")
        SystemType='Linux'
        sp='/'
        print ("系统类型：{0} {1} \n".format(SystemType, SystemBit))
    elif SystemType=='WindowsPE':
        os.system("cls")
        SystemType='Windows'
        sp='\\'
        print ("系统类型：{0} {1} \n".format(SystemType, SystemBit))
    else:
        SystemType="操作系统未知，检测失败，店铺分页可能出现显示异常，但不会引起运行错误。"
        sp='/'
        
def _getEmpty():
    #获取空目录
    for dirpaths,dirnames,filenames in os.walk(path):
        for file in filenames:
                filelist.append(os.path.join(dirpaths,file))
        if len(os.listdir(dirpaths))==0:
            emptypath.append(dirpaths)
            
def _ShowReport():
    print("\n\n===================未上传业绩租户==================")
    print("搜索路径为:{0}\n".format(path))
    i=0
    global emptylist
    emptylist="<table>"
    for empty in emptypath:
        i+=1
        posnumber=empty.split(sp)[-1] 
        
        try:
            posname=shoppos[posnumber.upper()] 
        except:
            posname='-'
      
        emptylist +=  posname+ '， '
        print( str(i) +'：'+posnumber+ ' [' + posname+ ']')

    print("\n共 "+ str(len(emptypath))+ " 家租户未上传业绩，已自动发送消息到运营主管。")

    if filecount:
        print ("\n总共有 {0} 个文件\n".format(filecount))  
   
def sendsms(msg):  
    if not msg=="" and not marketing_manager=="":
        #msg=msg.encode("gbk")
        arg={'USER_ID':"cdmixc", 'PASSWORD':"123", 'FROM_ID':"admin", 'TO_ID':marketing_manager, 'CONTENT':msg.encode("gbk")}
        msg=urllib.parse.urlencode(arg)
        url="http://crlandcd.com/interface/sms.php?"+msg
        #print(url)
        req=urllib.request.urlopen(url)
        returnstr=req.read()[-6:]
        #print(returnstr)
        if returnstr==b'100#|#':
            print("\n消息发送成功\n")
        else:
            print("\n消息发送失败\n")
    '''

    the_page=req.read()
    print(the_page)
    url_values=arg+msg
    full_url=url+url_values 
    print(full_url) 
    urllib.request.urlopen(full_url).read() 
    '''
        
def run():

    if not os.path.exists(path):
        print("\n目录不存在，请检查配置文件，程序退出\n")
        exit(1)
    _ReadShopNo()
    _getSystem()
    _getEmpty()

    print ('''用法：cdmixc [选项]... [-d] 目标目录
    或：cdmixc [选项]... [-x] 

    用于检查万象城日常业绩目录是否存在异常

    版权所有（C） 2015.7  <成都万象城>
    这一程序是自由软件，你可以遵照自由软件基金会出版的GNU通用公共许可证条款来修改和重新发布这一程序。或者用许可证的第二版，或者（根据你的选择）用任何更新的版本。
    发布这一程序的目的是希望它有用，但没有任何担保。甚至没有适合特定目的隐含的担保。更详细的情况请参阅GNU通用公共许可证。
    你应该已经和程序一起收到一份GNU通用公共许可证的副本。如果还没有，写信给：
    The Free Software Foundation, Inc., 675 Mass Ave, Cambridge,
    MA02139, USA
    ''')
    
    i=0

    filecount = len(filelist)

    for filename in filelist:
        with open(filename,  mode="r", encoding="ASCII") as filecontent:
            fileline = filecontent.read()
            i+=1
            j=""
            
            for count in range(int(float(i/filecount)*100/3)):
                j += '#'
            
            if int(i/filecount)*100 < 100:
                sys.stdout.write('处理中 '+str(round(float(i/filecount)*100, 1))+'%  || '+j+'->'+"\r")
            else:
                sys.stdout.write('已完成 '+str(round(float(i/filecount)*100, 1))+'%                                                         ')
            
            sys.stdout.flush()
            time.sleep(0.002)

if __name__=="__main__":
    run()
    _ShowReport()
    if input("\n是否通知运营主管未上传业绩租户？（ y/N ) ")=='y':
        sendsms("\n截至 "+ time.strftime('%F %H:%M:%S')+ " 共 "+ str(len(emptypath))+ " 家租户未上传业绩，明细如下："+emptylist[:-2])
        print("提醒信息已发送至运营主管："+marketing_manager)
        
    input("\n请按回车键退出")
