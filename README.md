# diemthi-analysis
Analysis of Vietnamese College Entrance Test Results 2020  

In Vietnam, high school graduates need to take a standardized college entrance exam to get considered for higher education. They need to take five subject tests: Maths, Literature, English, Social Sciences and Natural Sciences. Parents and students prepare three years of high school for this one exam, which in many people’s opinions determine your future. Before 2015, students has to take two exams: one deciding whether they graduate high school, and the other is the college entrance exam. These two exams now became one, therefore it is extremely stressful for students in their last year of high school.  

I was interested to see the results of the students. In this project, I scraped 74,000 exam takers scores in 2020 from the official Government website of Ho Chi Minh city, analyzed it then visualized in with Tableau to give the audience insights on this exam.  

# Data Collection  
The data collection method for this project will be web scraping.  
The website to scrape from is called http://diemthi.hcm.edu.vn/Home. This website is inactive now, but it looks like this.   

![image](https://user-images.githubusercontent.com/72576730/124315197-98550d00-db41-11eb-90cb-c2b13fd80d8d.png)

The form on the landing page allows user to put in the ID number of the candidate, which after hitting Enter will return their exam results  

![image](https://user-images.githubusercontent.com/72576730/124315283-bcb0e980-db41-11eb-8891-1eb59c6fdc54.png)

The exam results are stored as a table in html form. After researching, I found that the ID numbers range from 02000001 to 02074719.
I created a little code snippet that iterate through the number above, go to this website, input that number in, then copy the html of the results pages, and store it into the sobaodanh.txt file. The code is in **crawlsbd.py**.    

```
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
```
It took me around 3 hours to scrape this data, and I believe there is a more time-efficient way to do this. The text file is approximately 170 MB in size.

  
# Data Cleaning and Processing  
After scrapping process, we need to clean the file so that it allows us to see the students’ name, DOB, and their scores in table format. I use another Python file to do it, however it was quite manual to look for what to delete and what to keep. The cleaning python script is **csv_sbd.py** .

![image](https://user-images.githubusercontent.com/72576730/124316580-cdfaf580-db43-11eb-9e4c-39d9d1f68e32.png)

# Data Visualization
https://public.tableau.com/views/VietnamCollegeEntranceExamScore2020/Dashboard1
