import subprocess
result = subprocess.check_output('curl -F "sobaodanh=02000145" diemthi.hcm.edu.vn/Home/Show')
print(result)

f = open("sobaodanh.txt","r+")
f.truncate(0)
f.close()

for i in range(2000001,2074719):
    with open("sobaodanh.txt","a") as f:
        subprocess.run('curl -F "sobaodanh=0'+str(i)+'" diemthi.hcm.edu.vn/Home/Show,stdout=f)
        f.close()
        print(i-2000000)

