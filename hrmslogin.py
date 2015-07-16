# Python 模拟登录,然后记录cookie,之后完成登录
import urllib.request
import http.cookiejar

users={"TIANLEI":"123","XUJINJIA":"123"}
for user,pwd in users:
  
  # 登录并获取最新的hrms页面
  params = {"userid":user, "pwd":pwd}
  webCookie = http.cookiejar.CookieJar()
  openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(webCookie))
  webRequest = openner.open("http://hrms.crc.com.cn/psp/HRPRD/?cmd=login", urllib.parse.urlencode(params).encode())
#webRequest = openner.open("http://hrms.crc.com.cn/psp/HRPRD/EMPLOYEE/HRMS/h/?tab=DEFAULT")
#http://hrms.crc.com.cn/psp/HRPRD/EMPLOYEE/HRMS/c/CRC_ESS_MENU.CRC_ESS_PERSONAL.GBL?PORTALPARAM_PTCNAV=CRC_ESS_PERSONAL_GBL&EOPP.SCNode=HRMS&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=CRC_FLD_SELF_SERVE&EOPP.SCLabel=%E5%91%98%E5%B7%A5%E8%87%AA%E5%8A%A9&EOPP.SCPTfname=CRC_FLD_SELF_SERVE&FolderPath=PORTAL_ROOT_OBJECT.CRC_FLD_SELF_SERVE.CRC_ESS_PERSONAL_GBL
#webRequest = openner.open("http://hrms.crc.com.cn/psp/HRPRD/EMPLOYEE/HRMS/c/CRC_ESS_MENU.CRC_ESS_PERSONAL.GBL?PORTALPARAM_PTCNAV=CRC_ESS_PERSONAL_GBL&EOPP.SCNode=HRMS&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=CRC_FLD_SELF_SERVE&EOPP.SCLabel=%E5%91%98%E5%B7%A5%E8%87%AA%E5%8A%A9&EOPP.SCPTfname=CRC_FLD_SELF_SERVE&FolderPath=PORTAL_ROOT_OBJECT.CRC_FLD_SELF_SERVE.CRC_ESS_PERSONAL_GBL&IsFolder=false")
  htmlData = webRequest.read() 

  print(htmlData.decode('UTF-8')) #重新解码为UTF-8
  print("\nDone")
#dataFile = open(filePath + ".html", "w")
#dataFile.write(str(htmlData))
exit()
