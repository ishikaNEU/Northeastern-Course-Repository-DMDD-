# Northeastern-Course-Repository

One stop resource for all course related information at Northeastern University.  

## Team Members: 

- Ishika Misal (email: misal.i@northeastern.edu, NUID: 002787945)
- Utkarsha Shirke (email: shirke.u@northeastern.edu NUID: 002797914 )
- Supriya Tripathi (email: tripathi.su@northeastern.edu NUID: 002770986)

## Project Description: 

This project aims to create a database containing all relevant resources. The resources database will include: 

- Programs offered on the Boston campus of Northeastern University in the College of Engineering, and details about their duration, offerings, and specializations. 
- The relevant study material (paid and free resources) for all courses offered by COE. 
- Tools and software required by the courses.  
- Future career outcomes post-degree completion. 

We aspire to help learners through our initiative by helping them collate the resources they need to navigate their course. 

## Scope: 

We have shortlisted 3 graduate degree programs offered by Northeastern University’s College Of Engineering.  Our database is built around these programs. 
- Masters of Science in Information Systems (MSIS)
- Masters of Science in Data Analytics Engineering (MS DAE)
- Masters of Science Software Engineering Systems (MS CSYE)

## Implementation

### Phase 1: Twitter 

We started with thorough research and collection of existing data pertaining to this project. We sought various sources of data and verified the existing ones. To begin with, we laid out the use cases which we were seeking answers for. As the next steps, we spoke to a bunch of students at Northeastern University to gather information and factor in their points of view. 

Moving forward, we sought broader sources of information which led us to Twitter. Since Twitter as a platform voices many opinions, we thought it would give us a good sense of our project space. We scraped Twitter API, using tweepy for relevant programs, courses, and resources offered by Northeastern university, tweets, information about users, and their posts related to our database. This was a good starting point for our database and it helped us to move in the right direction. 

The performed the following steps for above analysis: 

- Fetched data from twitter 
- Inserted that data in our database using MYSQL
- Performed Queries to view data related to courses, programs, faculty details, events, and users. 
- Aligned and corraborated our usecases with the data collected using Twitter API 

#### Please visit the following link to get a detailed view of our Twitter data analysis
https://github.com/Tripathi-Supriya/Northeastern-Course-Repository/tree/main/Twitter%20Bot


### Phase 2: Gathering data from multiple resources

After collecting data from twitter, we condenseed our search to three main sources for data collection, described as follows: 

#### Website Scraping: 
As most of the details about the course offerings are available on the Northeastern university’s website, we have scraped multiple pages to gather information in one place. 

#### API Scraping: 
We have scraped LinkedIn API to collect information about the jobs a student can secure after graduating from the courses within our scope. We have used Python and Scrapy to get job-related data. We used the ai-skunks GitHub as a starting point to get jobs-related data. 

#### Google Forms: 
To get more on-ground data, we spoke to a few students and circulated google forms to collect data pertaining to resources that are relevant to the aforementioned programs. 

#### Google form Link to collect data:
https://docs.google.com/forms/d/e/1FAIpQLSfrdYENonfpEiqz62068CAPzFMHxywHvGfN4KWWV_0_zlkFOQ/formResponse
https://docs.google.com/forms/d/e/1FAIpQLSdQA2PA0DnS3jZjijo3N6l_oaYShjSEPOj0YfJWczVFrZ2KjQ/viewform

We have collated all the above data sources to create a database and established connections between program offerings, jobs related to these programs, events conducted to promote jobs and programs, and the resources learners need to excel in their coursework. To fetch the data we ran Python Script for scraping NEU Websites in Jupyter Notebook and Linkedin API Script for Scraping jobs on Linkedin. We also cleaned the data to fit our usecase using Python and MYSQL. 


#### Please visit the following link to get a detailed view of Phase 2
https://github.com/Tripathi-Supriya/Northeastern-Course-Repository/tree/main/Assignment_3_WebScrape

### Phase 3: Normalization

The data collected in Phase 2 was sufficient but it was not in standard format. Phase 3 of this project involved normalizing this data. We studied all the tables obtained in the second phase extensively and realised that some tables were violating the some normal forms viz. 1NF, 2NF, and 3NF. We have documeneted all these changes in a separate detailed folder. 

#### Please visit the following link to get a detailed view Normalization conducted in Phase 3
https://github.com/Tripathi-Supriya/Northeastern-Course-Repository/tree/main/Assignment_4

### Phase 4: Final Project

Here's a brief overview of the dataset obtained after the final phase i.e after normlization of all the required tables:

## ER Diagram:

![ER_Diagram](https://user-images.githubusercontent.com/114371417/207747151-73db7804-e7c5-4d5c-86e5-e2c1d4202379.png)


### Final Project Execution Steps:

Run the below Queries for the complete code Execution by following the given steps:

####CREATE TABLE STATEMENTS


## 1.Neu_Program:

       CREATE TABLE NEU_Program (
       program_name varchar(100),
       duration varchar(100),
       program_url varchar(255),
       PRIMARY KEY (program_name)
       );

## 2. NEU_Course_Catalog:

        CREATE TABLE NEU_Course_Catalog (
        program_name varchar(50),
        course_id varchar(50),
        course_name varchar(100),
        course_description longtext,
        PRIMARY KEY (course_id)
        );

## 3. NEU_Event Table:

        CREATE TABLE NEU_Event (
        event_id integer auto_increment,
        program_name varchar(50),
        event_name varchar(255),
        Primary Key (event_id)
        );

#### Set auto increment value to 974

        ALTER TABLE NEU_Event AUTO_INCREMENT=974;

## 4.Course_Core_Requirement Table:

        CREATE TABLE course_core_requirement (
        core_course_id integer auto_increment,
        program_name varchar(50),
        course_id varchar(50),
        course_name varchar(100),
        PRIMARY KEY (core_course_id)
        );

#### Set auto increment value to 1400

      ALTER TABLE Course_Core_Requirement AUTO_INCREMENT=1400;


## 5. NEU_Faculty Table:

        CREATE TABLE neu_faculty (
        faculty_name varchar(255),
        faculty_rating integer,
        PRIMARY KEY (faculty_name)
        );

#### Set auto increment value to 1200

       ALTER TABLE Course_Core_Requirement AUTO_INCREMENT=1200;


## 6. NEU_Course_Faculty Table:

       CREATE TABLE NEU_Course_Faculty (
       fac_course_id  integer auto_increment,
       faculty_name varchar(255),
       course_id integer,
       PRIMARY KEY (fac_course_id)
       );

#### Set auto increment value to 4280

        ALTER TABLE NEU_Course_Faculty AUTO_INCREMENT=4280;


## 7. NEU_Course_Specialization Table: 

        CREATE TABLE NEU_Course_Specialization (
        spec_course_id  integer auto_increment,
        specialization_id integer,
        course_id integer,
        credit_hours integer,
        PRIMARY KEY (spec_course_id  )
        );

#### Set auto increment value to 6700

        ALTER TABLE NEU_Course_Specialization AUTO_INCREMENT=6700;


## 8. NEU_Specialization Table:

        CREATE TABLE NEU _Specialization (
        specialization_id integer,
        specialization_name,
        PRIMARY KEY (specialization_id  )
        );


## 9.NEU_Resource_Materials table:

        CREATE TABLE NEU_Resource_Materials(
        software_name varchar(255),
        software_download_url longtext,
        professional_certification longtext,
        online_platform longtext,
        PRIMARY KEY (software_name)
        );


## 10.NEU_Course_Resource table: 

        CREATE TABLE NEU_Course_Resource (
        course_resource_id integer auto_increment,
        course_id varchar(255),
        software_name varchar(255),
        course_rating integer,
        PRIMARY KEY (course_resource_id)
        );

#### Set auto increment value to 5233
 
        ALTER TABLE NEU_Course_Resource AUTO_INCREMENT=5233;


## 11.Job_Info table:

      CREATE TABLE Job_Info (
      Job_no integer auto_increment,
      title varchar(255),
      job_id varchar(255),
      company_name varchar(255),
      location varchar(255),
      date_posted date ,
      link longtext,
      description longtext,
      seniority_level varchar(255) ,
      employement_type varchar(255),
      job_function varchar(255),
      industry varchar(255),
      primary key (job_No)
      );

#### Set auto increment value to 601

      ALTER TABLE Job_info AUTO_INCREMENT=601;


## 12.Program_jobs Table:

      CREATE TABLE Program_jobs (
      program_job_no integer auto_increment,
      job_id varchar (255),
      program_name varchar(255),
      PRIMARY KEY (program_job_no)
      );

#### Set auto increment value to 10178

      ALTER TABLE Job_info AUTO_INCREMENT=10178;


#### Adding Foreign Constraints:

       ALTER TABLE NEU_Course_Catalogs
       ADD CONSTRAINT NEU_Course_Catalog_fk1 FOREIGN KEY (program_name)	
       REFERENCES NEU_Programs(program_name);

       ALTER TABLE Course_Core_Requirements
       ADD CONSTRAINT NEU_Course_Core_Requirement_fk1 FOREIGN KEY (program_name)
       REFERENCES NEU_Programs(program_name);

        ALTER TABLE Course_Core_Requirements
        ADD CONSTRAINT NEU_Course_Core_Requirement_fk1 FOREIGN KEY (program_name)
        REFERENCES NEU_Programs(program_name);

        ALTER TABLE NEU_Events
        ADD CONSTRAINT NEU_Event_fk1 FOREIGN KEY (program_name)
        REFERENCES NEU_Programs(program_name);


        ALTER TABLE NEU_Course_Facultys
        ADD CONSTRAINT NEU_Course_Facultys_fk1 FOREIGN KEY (course_id)
        REFERENCES NEU_Course_Catalogs(course_id);

        ALTER TABLE NEU_Course_Facultys
        ADD CONSTRAINT NEU_Course_Facultys_fk2 FOREIGN KEY (faculty_name)
        REFERENCES Neu_facultys(faculty_name);

        ALTER TABLE NEU_Course_Specializations
        ADD CONSTRAINT NEU_Course_Specializations_fk1 FOREIGN KEY (course_id)
        REFERENCES NEU_Course_Catalogs(course_id);

        ALTER TABLE NEU_Course_Specializations
        ADD CONSTRAINT NEU_Course_Specializations_fk2 FOREIGN KEY (specialization_id)
        REFERENCES NEU_Specializations(specialization_id);


        ALTER TABLE NEU_Course_resources
        ADD CONSTRAINT NEU_Course_resources_fk1 FOREIGN KEY (course_id)
        REFERENCES NEU_Course_Catalogs(course_id);


        ALTER TABLE NEU_Course_resources
        ADD CONSTRAINT NEU_Course_resources_fk2 FOREIGN KEY (software_name)
        REFERENCES NEU_Resource_material(software_name);


        ALTER TABLE Programs_jobs
        ADD CONSTRAINT Programs_jobs_fk1 FOREIGN KEY (program_name)
        REFERENCES NEU_Programs(program_name);


        ALTER TABLE Programs_jobs
        ADD CONSTRAINT Programs_jobs_fk1 FOREIGN KEY (job_id)
        REFERENCES Jobs_Info(job_id);


## 9. Run the Python Script for scraping NEU Websites in Jupyter Notebook

#### 10. SQL to insert data in Tables:

## NEU_Event Table:

      INSERT INTO neu_event (program_name,event_name) VALUES ("Information Systems","Ethics Institute Speaker, Michael Hannon ( Friday, November 18, 2022 12pm to 1:30pm )");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Information Systems","Ethics Institute Speaker, Don Fallis ( Friday, December 2, 2022 12pm to 1:30pm)");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Information Systems","Using a Systems-based Culturally Responsive Evaluation (SysCRE) Framework (Wednesday, November 16, 2022 10am to 11:30am)");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Information Systems","Designing an Engaging Academic Presentation (Friday, November 11, 2022)");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Information Systems","Listener Research Study (Friday, November 11, 2022)");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Data Analytics Engineering","Problem Play (Friday, November 11, 2022 8pm to 10pm)");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Data Analytics Engineering","Graduate programs open house ");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Data Analytics Engineering","Women in STEM: An Evening with Distinguished Alumni (6th March 2023)");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Data Analytics Engineering","Fall Graduate Programs Open House ");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Data Analytics Engineering","Northeastern University Mumbai Education Exhibition");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Software Engineering Systems","Graduate Studies Information Session");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Software Engineering Systems","Next Steps for Critical Infrastructure & Cyber Security: CISA Dir. Wales (Tue, Nov 15, 11:00 PM)");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Software Engineering Systems","International Education Week Kick-Off Event (Mon, Nov 14, 2:00 PM)");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Software Engineering Systems","Greatest MINDS Generations - A Gathering of Black Bostonians (All Ages)2023 (Thu, Jan 19, 9:00 AM)");
      INSERT INTO neu_event (program_name,event_name) VALUES ("Software Engineering Systems","Can AI Help Create a More Sustainable World? (Tue, Nov 15, 5:00 PM)");
      
 
 ## NEU_Specialization Table:

      INSERT INTO NEU_Specialization (specialization_id,specialization_name) VALUES (9100, "Big Data Systems and Analytics Concentration");
      INSERT INTO NEU_Specialization (specialization_id,specialization_name) VALUES (9101, "Intelligent Systems Concentration");
      INSERT INTO NEU_Specialization (specialization_id,specialization_name) VALUES (9102, "Smart Contracts Concentration");
      INSERT INTO NEU_Specialization (specialization_id,specialization_name) VALUES (9103, "User Experience Concentration");

## NEU_Course_specialization table:

      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9100,"CSYE 6225",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES(9100,"DAMG 7245",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9100,"INFO 7250",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9100,"INFO 7390",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9101,"CSYE 7280",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9101,"INFO 7375",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9101,"INFO 7390",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9101,"INFO 7610",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9102,"INFO 7500",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9102,"INFO 7510",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9102,"INFO 7520",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9102,"INFO 7525",2);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9102,"INFO 7535",2);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9103,"CSYE 7280",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9103,"INFO 6150",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9103,"INFO 6245",4);
      INSERT INTO NEU_Course_Specialization (Specialization_id,course_id,credit_hours) VALUES (9103,"INFO 6350",4);
     
     
## 11. Delete data from table to run the python script again

      DELETE FROM job_info;
      DELETE FROM program_jobs;
      DELETE FROM neu_course_specialization;
      DELETE FROM neu_specialization;
      DELETE FROM neu_facultys;
      DELETE FROM neu_resource_materials;
      DELETE FROM neu_course_resource;
      DELETE FROM neu_course_faculty;
      DELETE FROM neu_course_catalog;
      DELETE FROM neu_event;
      DELETE FROM course_core_requirement;
      DELETE FROM neu_program;
      
      
## Database Tables Output:

### 1.NEU_Program:

 ![image](https://user-images.githubusercontent.com/114371417/207749425-9341a99c-9e41-4a62-b950-919256e19fb3.png)


### 2.NEU_Course_Catalog Table:

![image](https://user-images.githubusercontent.com/114371417/207749469-c262ad89-c84e-4bda-bbfb-3278ba9131ad.png)

                
### 3.NEU_Event Table:

 ![image](https://user-images.githubusercontent.com/114371417/207749511-c0f00ef3-8200-49e5-894e-087060543d6c.png)


### 4.Course_Core_Requirement Table:

 ![image](https://user-images.githubusercontent.com/114371417/207749554-bbb1883e-b687-475d-a601-68246ff38134.png)


### 5.NEU_Course_Resource Table:
      
  ![image](https://user-images.githubusercontent.com/114371417/207749606-90683dc5-93ff-4ee4-ab7f-5136a802ba8d.png)


### 6.NEU_Resource_Materials Table:

 ![image](https://user-images.githubusercontent.com/114371417/207749652-9d778947-ced2-4fd5-ad62-bf0b872a0af8.png)


### 7.Job_Info Table:

![image](https://user-images.githubusercontent.com/114371417/207749699-960cad9f-28e6-4844-8866-f4d7f6b730d7.png)


### 8.Program_Jobs Table:

 ![image](https://user-images.githubusercontent.com/114371417/207749725-7c0ed0be-467b-45c8-834d-c0593aafeee1.png)


### 9.NEU_Facultys Table:

 ![image](https://user-images.githubusercontent.com/114371417/207749763-de1bdf05-b1db-44ad-b518-4998d5cc86ef.png)


### 10.	NEU_Course_faculty Table: 

![image](https://user-images.githubusercontent.com/114371417/207749794-4bb5f452-75e3-4edb-9402-8b386d660b8a.png)


### 11.NEU_Specialization Table:

![image](https://user-images.githubusercontent.com/114371417/207749847-88d9e74c-c8bf-4a60-94db-e7c76fa255a8.png)

 
### 12.NEU_Course_Specialization Table:

 ![image](https://user-images.githubusercontent.com/114371417/207749881-59b5cbf9-c9c4-44ff-8fd9-eafc79fea6dd.png)


## Use Cases:


### 1. How many total courses are available for Information Systems Program in Northeastern  University?

      SELECT a.program_name, 
      COUNT(a.course_name), b.program_url
      FROM neu_course_catalog a 
      LEFT OUTER JOIN
      NEU_Program b 
      ON a.program_name = b.program_name 
      WHERE b.program_name = 'Information Systems'
      GROUP BY a.program_name;

 ![image](https://user-images.githubusercontent.com/114371417/207750026-56bc013b-8e09-490b-99b9-98caf4c86a28.png)



### 2. Which courses do we need to take to do specialization in User Experience Concentration?

        SELECT a.specialization_name,b.course_id,c.course_name 
        FROM
        neu_specialization a 
        LEFT JOIN neu_course_specialization b
        ON  a.specialization_id = b.specialization_id 
        RIGHT JOIN  neu_course_catalog c 
        ON b.course_id = c.course_id
        WHERE a.specialization_name = 'User Experience Concentration';

![image](https://user-images.githubusercontent.com/114371417/207750205-f2bba063-f4f3-4a39-b304-60e46a3fa6e0.png)


### 3.List top rated professors at NEU whose rating is above 4. Also mention the courses and its description taught by the professor.

        SELECT a.faculty_name,a.faculty_rating,b.course_id,c.course_description 
        FROM neu_facultys a 
        JOIN neu_course_faculty b 
        ON a.faculty_name = b.faculty_name
        JOIN neu_course_catalog c 
        ON b.course_id = c.course_id
        WHERE a.faculty_rating >= 4;
        
![image](https://user-images.githubusercontent.com/114371417/207750289-0e219e1f-8f00-40c1-9d62-b342367f5687.png)

 

### 4. What are the core course requirements for Information Systems, Software Engineering Systems and Data Analytics?

        SELECT a.program_name, GROUP_CONCAT(a.course_id SEPARATOR  '|'),      
        COUNT(a.course_id), b.program_url
        FROM Course_Core_requirement a
        LEFT JOIN NEU_Program b
        ON a.program_name = b.program_name
        GROUP BY a.program_name;
        
![image](https://user-images.githubusercontent.com/114371417/207750348-3ff3e91f-674d-42e4-b8d5-aca2226eddd5.png)


 
### 5. List courses available for Data Analytics Engineering along with its course_outcome.

        SELECT
        program_name, course_id,course_name, course_description
        FROM
        NEU_Course_Catalog 
        WHERE program_name = 'Data Analytics Engineering';

![image](https://user-images.githubusercontent.com/114371417/207750408-a88f0c7d-7791-4878-84f2-f56b0715a9c3.png)


### 6. What is the average overall rating given by students to a professor for a given course?

        SELECT faculty_name, round (AVG(faculty_rating),1) as Average_rating 
        FROM neu_Facultys
        GROUP BY faculty_name;

![image](https://user-images.githubusercontent.com/114371417/207750450-c51803ab-ad85-450a-9d26-b29883b22321.png)


### 7. Which courses students need to take to do specialization in Big Data Systems concentration and which resources are available for them?

        SELECT a.specialization_name, b.course_id,c.course_name,d.software_name,e.online_platform
        FROM neu_specialization a 
        LEFT JOIN neu_course_specialization b
        ON a.specialization_id = b.specialization_id
        LEFT JOIN neu_course_catalog c 
        ON b.course_id = c.course_id
        LEFT JOIN neu_course_resource d 
        ON c.course_id = d.course_id
        LEFT JOIN neu_resource_materials e
        ON d.software_name = e.software_name
        WHERE a.specialization_name like '%Big Data%';
        
![image](https://user-images.githubusercontent.com/114371417/207750504-227fd2e0-18e0-4991-8c59-c4489ae60044.png)

 
### 8. List details about all the Masters programs available in Northeastern University

        SELECT * FROM NEU_program;

![image](https://user-images.githubusercontent.com/114371417/207750541-f835e862-ec58-4c3b-aba8-2794d9b2c881.png)


### 9. Which job positions for students in Data Analytics Engineering and list the details related to those positions?

        SELECT b.program_name, a.job_id,a.title,a.company_name,a.description,a.location
        FROM program_jobs b 
        LEFT JOIN job_info a 
        ON a.job_id = b.job_id 
        WHERE b.program_name LIKE '%Data%';

![image](https://user-images.githubusercontent.com/114371417/207750579-f3e3945b-bfe5-405b-b2d5-ce6e1e2f2259.png)

### 10. List the events hosted by Northeastern University for students by Data Analytics Engineering Department.

         SELECT program_name, event_name 
         FROM Neu_Event 
         WHERE program_name = 'Data Analytics Engineering';
         
![image](https://user-images.githubusercontent.com/114371417/207750672-7989581b-6b8c-45be-969a-67731a828d5f.png)

 
### 11.Which professors teach courses related to User Experience and list the ratings given by students for the course?

          SELECT a.specialization_name, b.course_id,c.program_name, d.faculty_name,e.faculty_rating
          FROM neu_specialization a
          LEFT JOIN neu_course_specialization b
          ON a.specialization_id = b.specialization_id
          LEFT JOIN neu_course_catalog c
          ON b.course_id = c.course_id
          LEFT JOIN neu_course_faculty d 
          ON d.course_id = c.course_id
          LEFT JOIN neu_facultys e
          ON e.faculty_name = d.faculty_name
          WHERE a.specialization_name like '%User%';
     
![image](https://user-images.githubusercontent.com/114371417/207750736-4211434a-9718-4416-a2ba-5d733a149e08.png)

 
### 12. Find the average course rating for Information Systems Program

          SELECT a.program_name, AVG(b.course_rating)
          FROM neu_course_catalog a 
          RIGHT JOIN neu_course_resource b
          ON a.course_id = b.course_id
          WHERE a.program_name  ='Information Systems';

![image](https://user-images.githubusercontent.com/114371417/207750804-c29da372-b82f-416b-8f99-f48a249e7cbe.png)

 
### 13. List courses with lowest rating.

          SELECT a.course_id, a.course_name,a.course_description,b.course_rating
          FROM neu_course_catalog a 
          LEFT JOIN neu_course_resource b
          ON a.course_id = b.course_id
          WHERE b.course_rating = (select min(course_rating) from neu_course_resource);

![image](https://user-images.githubusercontent.com/114371417/207750845-f093d23c-f092-449e-a875-dc9862cc09d9.png)

### 14. Find the professors who taught DAMG 7350, INFO 5100, DAMG 6105, DAMG 7275 courses.

          select a.faculty_name, b.course_id 
          from neu_facultys a 
          JOIN NEU_Course_faculty b
          ON a.faculty_name = b.faculty_name
          where b.course_id IN ('DAMG 7350', 'INFO 5100','DAMG 6105' ,'DAMG 7275');

![image](https://user-images.githubusercontent.com/114371417/207750902-1b79fe17-cf71-477c-b96d-f7ff9adac0b9.png)


### 15. Which resources are available for students who have chosen Information Systems program?

          SELECT a.program_name, a.course_id,b.software_name,c.software_download_url,c.online_platform
          FROM neu_course_catalog a 
          JOIN neu_course_resource b
          ON a.course_id = b.course_id
          JOIN neu_resource_materials c
          ON b.software_name = c.software_name
          WHERE a.program_name = 'Information Systems';
         
![image](https://user-images.githubusercontent.com/114371417/207750954-2924530f-233e-43fe-b44b-42b3d027878a.png)
          
          
## View Creation for Use Cases:

### 1.	How many total courses are available for Information Systems Program in Northeastern University?

          CREATE VIEW InformationSystems_Total_Courses AS
          SELECT a.program_name, 
          COUNT(a.course_name), b.program_url
          FROM neu_course_catalog a 
          LEFT OUTER JOIN
          NEU_Program b 
          ON a.program_name = b.program_name 
          WHERE b.program_name = 'Information Systems'
          GROUP BY a.program_name;
          
![image](https://user-images.githubusercontent.com/114371417/207751188-6a9ee0d4-fbaa-4399-bdeb-3f599d2c3121.png)


### 2.	Which courses do we need to take to do specialization in User Experience Concentration?

           CREATE VIEW User_Experience_Specialization_Courses AS
           SELECT a.specialization_name,b.course_id,c.course_name 
           FROM
           neu_specialization a 
           LEFT JOIN neu_course_specialization b
           ON  a.specialization_id = b.specialization_id 
           RIGHT JOIN  neu_course_catalog c 
           ON b.course_id = c.course_id
           WHERE a.specialization_name = 'User Experience Concentration';

![image](https://user-images.githubusercontent.com/114371417/207751354-bcc6cb7c-c015-486c-8d09-44bbbef2c6c5.png)


### 3.	List top rated professors at NEU whose rating is above 4. Also mention the courses and its description taught by the professor.

          CREATE VIEW NEU_Top_Rated_Professors AS
          SELECT a.faculty_name,a.faculty_rating,b.course_id,c.course_description 
          FROM neu_facultys a 
          JOIN neu_course_faculty b 
          ON a.faculty_name = b.faculty_name
          JOIN neu_course_catalog c 
          ON b.course_id = c.course_id
          WHERE a.faculty_rating >= 4;

![image](https://user-images.githubusercontent.com/114371417/207751414-17bc0e46-65e6-4841-be32-90c834268bc3.png)



### 4.	What are the core course requirements for Information Systems, Software Engineering Systems and Data Analytics?

          CREATE VIEW Programs_Core_Course_requirement AS 
          SELECT a.program_name, GROUP_CONCAT(a.course_id SEPARATOR  '|'),      
          COUNT(a.course_id), b.program_url
          FROM Course_Core_requirement a
          LEFT JOIN NEU_Program b
          ON a.program_name = b.program_name
          GROUP BY a.program_name;

![image](https://user-images.githubusercontent.com/114371417/207751456-fb21bec0-f57b-44f5-af79-28e44a9db990.png)


### 5.	List courses available for Data Analytics Engineering along with its course_outcome.

            CREATE VIEW Data_Analytics_course_outcome AS 
            SELECT
            program_name, course_id,course_name, course_description
            FROM
            NEU_Course_Catalog 
            WHERE program_name = 'Data Analytics Engineering';

![image](https://user-images.githubusercontent.com/114371417/207751516-e317ceba-839e-4906-8930-7c4975d8e923.png)


### 6.	What is the average overall rating given by students to a professor for a given course?

          Create VIEW Professor_Avg_rating AS
          SELECT faculty_name, round (AVG(faculty_rating),1) as Average_rating 
          FROM neu_Facultys
          GROUP BY faculty_name;

![image](https://user-images.githubusercontent.com/114371417/207751560-74f41d6b-91ac-4276-95ea-a3bb3cb8b4e6.png)


### 7.	Which courses students need to take to do specialization in Big Data Systems concentration and which resources are available for them?

            CREATE VIEW Big_data_Course_Resource AS
            SELECT a.specialization_name, b.course_id,c.course_name,d.software_name,e.online_platform
            FROM neu_specialization a 
            LEFT JOIN neu_course_specialization b
            ON a.specialization_id = b.specialization_id
            LEFT JOIN neu_course_catalog c 
            ON b.course_id = c.course_id
            LEFT JOIN neu_course_resource d 
            ON c.course_id = d.course_id
            LEFT JOIN neu_resource_materials e
            ON d.software_name = e.software_name
            WHERE a.specialization_name like '%Big Data%';

![image](https://user-images.githubusercontent.com/114371417/207751637-e32ba94c-f9fe-4cb6-a7c5-dbc53eda8f74.png)


### 8.	Which job positions are available for students in Data Analytics Engineering and list the details related to those positions?  

          CREATE VIEW Data_Analytics_Job_Positions AS 
          SELECT b.program_name, a.job_id,a.title,a.company_name,a.description,a.location
          FROM program_jobs b 
          LEFT JOIN job_info a 
          ON a.job_id = b.job_id 
          WHERE b.program_name LIKE '%Data%';

![image](https://user-images.githubusercontent.com/114371417/207751684-9f6798d2-5e45-486d-b14d-26486b8066fd.png)


### 9.	Which professors teach courses related to User Experience and list the ratings given by students for the course?
 
            CREATE VIEW User_Experience_Professors AS
            SELECT a.specialization_name, b.course_id,c.program_name, d.faculty_name,e.faculty_rating
            FROM neu_specialization a
            LEFT JOIN neu_course_specialization b
            ON a.specialization_id = b.specialization_id
            LEFT JOIN neu_course_catalog c
            ON b.course_id = c.course_id
            LEFT JOIN neu_course_faculty d 
            ON d.course_id = c.course_id
            LEFT JOIN neu_facultys e
            ON e.faculty_name = d.faculty_name
            WHERE a.specialization_name like '%User%';

![image](https://user-images.githubusercontent.com/114371417/207751739-0e3545b1-394c-40b3-bf9e-6c85adab9858.png)



### 10. Find the average course rating for Information Systems Program

            CREATE VIEW Information_System_Avg_Course_rating AS
            SELECT a.program_name, AVG(b.course_rating)
            FROM neu_course_catalog a 
            RIGHT JOIN neu_course_resource b
         	  ON a.course_id = b.course_id
         	  WHERE a.program_name  ='Information Systems';

![image](https://user-images.githubusercontent.com/114371417/207751806-fd73d768-00c4-4ebf-a557-d8d8830667af.png)


### 11. List courses with lowest rating.
      
      	  CREATE VIEW Lowest_Rating_Courses As
        	SELECT a.course_id, a.course_name,a.course_description,b.course_rating
        	FROM neu_course_catalog a 
        	LEFT JOIN neu_course_resource b
        	ON a.course_id = b.course_id
        	WHERE b.course_rating = (select min(course_rating) from neu_course_resource);

![image](https://user-images.githubusercontent.com/114371417/207751872-f0854c8f-186a-4cc9-a4a0-3abb4c570762.png)
                     
         

### 12. Find the professors who taught DAMG 7350, INFO 5100, DAMG 6105, DAMG 7275   courses.

           CREATE VIEW Professor_DAMG7350_INFO5100_DAMG6105_DAMG7275 AS
           select a.faculty_name, b.course_id 
           from neu_facultys a 
           JOIN NEU_Course_faculty b
           ON a.faculty_name = b.faculty_name
           where b.course_id IN ('DAMG 7350', 'INFO 5100','DAMG 6105' ,'DAMG 7275');

           ![image](https://user-images.githubusercontent.com/114371417/207751939-e72429a4-cb28-448d-a243-396703641a4e.png)



### 13. Which resources are available for students who have chosen Information Systems program?

          CREATE VIEW Information_Systems_Resource_Details AS
          SELECT a.program_name,a.course_id,b.software_name,
          c.software_download_url,c.online_platform
          FROM neu_course_catalog a 
          JOIN neu_course_resource b
          ON a.course_id = b.course_id
          JOIN neu_resource_materials c
          ON b.software_name = c.software_name
          WHERE a.program_name = 'Information Systems';
          
![image](https://user-images.githubusercontent.com/114371417/207751986-e137d5f8-28b7-4517-889a-cb0473a4d586.png)


## Conclusion

Our database now contains, easy to use tables, which have details relevnat to MSIS, SES, and CSYE programs offered at Northeasetrn University. Students can use this database to make informed decisions about their coursework, facult, events, and career related outcomes. 


