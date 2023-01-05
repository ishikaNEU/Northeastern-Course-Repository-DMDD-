# Northeastern-Course-Repository
NEU resource for courses offered. 

# Team Members: 

Ishika Misal (email: misal.i@northeastern.edu)
Utkarsha Shirke (email: shirke.u@northeastern.edu )
Supriya Tripathi (email: tripathi.su@northeastern.edu)

# Project Description: 

This project aims to create a database containing all relevant resources. The resources database will include: 

- Programs offered on the Boston campus of Northeastern University in the College of Engineering, and details about their duration, offerings, and specializations. 
- The relevant study material (paid and free resources) for all courses offered by COE. 
- Tools and software required by the courses.  
- Program contacts (Professors/Advisors/Current Teaching Assistants). 
- Future career outcomes post-degree completion. 

We aspire to help learners through our initiative by helping them collate the resources they need to navigate their course. 

## Scope: 
We have shortlisted 3 graduate degree programs offered by Northeastern University’s College Of Engineering.  Our database is built around these programs. 
Masters of Science in Information Systems
Masters of Science in Data Analytics Engineering
Masters of Science Software Engineering Systems

## Plan of Action:
We have used 3 sources to collect the data: 

### Website Scraping: 
As most of the details about the course offerings are available on the Northeastern university’s website, we have scraped multiple pages to gather information in one place. 

### API Scraping: 
We have scraped LinkedIn API to collect information about the jobs a student can secure after graduating from the courses within our scope. We have used Python and Scrapy to get job-related data. We used the ai-skunks GitHub as a starting point to get jobs-related data. 

### Google Forms: 
To get more on-ground data, we spoke to a few students and circulated google forms to collect data pertaining to resources that are relevant to the aforementioned programs. 

#### Google form Link to collect data:
https://docs.google.com/forms/d/e/1FAIpQLSfrdYENonfpEiqz62068CAPzFMHxywHvGfN4KWWV_0_zlkFOQ/formResponse
https://docs.google.com/forms/d/e/1FAIpQLSdQA2PA0DnS3jZjijo3N6l_oaYShjSEPOj0YfJWczVFrZ2KjQ/viewform

We have collated all the above data sources to create a database and established connections between program offerings, jobs related to these programs, events conducted to promote jobs and programs, and the resources learners need to excel in their coursework. 

# ER Diagram:

![DMDD_Assignment3_ER_Diagram](https://user-images.githubusercontent.com/114371417/205808808-e3847d95-8b94-44b6-b2bb-e834471e4fe9.png)


## Data Cleaning:


1. NEU_Programs Table:

 - Removed all programs name which were not in Boston in the dataframe using drop duplicates command in python
 

2. Neu_Course_Catalog Table:

 - Unwanted text removed in python after scraping data and then inserted into table.


3. NEU_Course_Faculty Table:

 - Data inserted from csv file by collecting responses from Students


4. Resource_Material1 Table:

 - Data inserted from csv file as per responses given by students


5. NEU_Event Table:

 - This data is manually inserted in SQL by using insert query. Hence, the data is validated and then inserted into table

6. NEU_Specialization Table:

-  Data is validated beffore inserting into table. 


7. Course_Core_Requirement Table:

 -  Accurate data scraped from Northeastern University website. No cleaning required


8. Jobs_Info Table:

 - Duplicate jobs are removed from the scraped data in jupyter notebook

## Assignment Execution Steps:

Run the below Queries for the complete code Execution by following the given steps:


## 1. Create NEU_Program table

	CREATE TABLE NEU_Program (
	program_name varchar(100),
	duration varchar(100),
	program_url varchar(255),
	PRIMARY KEY (program_name)
	);


## 2. Create NEU_Course_Catalog

	CREATE TABLE NEU_Course_Catalog (
	program_name varchar(50),
	course_id varchar(50),
	course_name varchar(100),
	course_description longtext,
	PRIMARY KEY (course_id)
	);


## 3. Create Resources_Material1 table

	CREATE TABLE Resource_material1(
	resource_id integer auto_increment,
	course_id varchar(255),
	software_download_url longtext,
	professional_certificate longtext,
	online_platform longtext,
	course_rating integer,
	Primary Key (resource_id)
	);

#### Set auto increment value to 3100

	ALTER TABLE Resource_material1 AUTO_INCREMENT=3100;


## 4. Create NEU_Course_Faculty Table

	CREATE TABLE NEU_Course_Faculty (
	faculty_id integer auto_increment,
	program_name varchar(50),
	course_id varchar(100),
	faculty_name varchar(100),
	faculty_rating integer,
	Primary Key (faculty_id)
	);


#### Set auto increment value to 4100

	ALTER TABLE NEU_Course_Faculty AUTO_INCREMENT=4100;



## 5. Create Course_Core_Requirement table

	CREATE TABLE course_core_requirement (
	core_course_id integer auto_increment,
	program_name varchar(50),
	course_id varchar(50),
	course_name varchar(100),
	PRIMARY KEY (core_course_id)
	);

#### Set auto increment value to 1101

	ALTER TABLE course_core_requirement AUTO_INCREMENT=1101;


## 6.  Create Jobs_Info Table

	CREATE TABLE Jobs_Info (
	Job_No integer auto_increment,
	program_name varchar(255),
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

#### Set auto increment value to 900

	ALTER TABLE jobs_info AUTO_INCREMENT=900;


## 7. NEU_Event table:

	CREATE TABLE NEU_Event (
	event_id integer auto_increment,
	program_name varchar(50),
	event_name varchar(255),
	Primary Key (event_id)
	);

#### Set auto increment value to 101

	ALTER TABLE neu_event AUTO_INCREMENT=101;
	
	
## 8. NEU_Specialization Table

	CREATE TABLE NEU_Specialization (
	spec_course_id integer auto_increment,
	course_id varchar(50),
	credit_hours integer,
	specialization varchar(100),
	Primary Key (spec_course_id)
	);

## Set auto increment value to 1000

	ALTER TABLE NEU_Specialization AUTO_INCREMENT=1000;


#### Add Foreign Key constraints


	ALTER TABLE NEU_Course_Catalogs
	ADD CONSTRAINT NEU_Course_Catalog_fk1 FOREIGN KEY (program_name)	
	REFERENCES NEU_Programs(program_name);


	ALTER TABLE Resource_material1s
	ADD CONSTRAINT Resource_material1_fk FOREIGN KEY (course_id)
	REFERENCES NEU_Course_Catalogs(course_id);


	ALTER TABLE NEU_Course_Facultys
	ADD CONSTRAINT NEU_Course_Faculty_fk1 FOREIGN KEY (course_id)
	REFERENCES NEU_Course_Catalogs(course_id);
	

	ALTER TABLE Course_Core_Requirements
	ADD CONSTRAINT NEU_Course_Core_Requirement_fk1 FOREIGN KEY (program_name)
	REFERENCES NEU_Programs(program_name);
	

	ALTER TABLE NEU_Events
	ADD CONSTRAINT NEU_Event_fk1 FOREIGN KEY (program_name)
	REFERENCES NEU_Programs(program_name);
	
	
	ALTER TABLE Jobs_Infos
	ADD CONSTRAINT Jobs_Info_fk1 FOREIGN KEY (program_name)
	REFERENCES NEU_Programs(program_name);
	
	
	ALTER TABLE NEU_Specializations
	ADD CONSTRAINT NEU_Specialization_fk1 FOREIGN KEY (course_id)
	REFERENCES NEU_Course_Catalogs(course_id);

## 9. Run the Python Script for scraping NEU Websites in Jupyter Notebook

## 10. Run Linkedin API Script for Scraping jobs on Linkedin

#### SQL to insert data in NEU_Event Table

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



## SQL to insert data in NEU_Specialization Table


	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("CSYE 6225",4,"Big Data Systems and Analytics Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("DAMG 7245",4,"Big Data Systems and Analytics Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 7250",4,"Big Data Systems and Analytics Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 7390",4,"Big Data Systems and Analytics Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("CSYE 7280",4,"Intelligent Systems Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 7375",4,"Intelligent Systems Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 7390",4,"Intelligent Systems Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 7610",4,"Intelligent Systems Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 7500",4,"Smart Contracts Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 7510",4,"Smart Contracts Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 7520",4,"Smart Contracts Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 7525",2,"Smart Contracts Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 7535",2,"Smart Contracts Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("CSYE 7280",4,"User Experience Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 6150",4,"User Experience Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 6245",4,"User Experience Concentration");
	INSERT INTO NEU_Specialization (course_id,credit_hours,specialization) VALUES ("INFO 6350",4,"User Experience Concentration");


## 11. Delete data from table to run the python script again

	DELETE FROM jobs_info;
	DELETE FROM neu_specialization;
	DELETE FROM neu_course_faculty;
	DELETE FROM resource_material1;
	DELETE FROM neu_course_catalog;
	DELETE FROM neu_event;
	DELETE FROM course_core_requirement;
	DELETE FROM neu_program;

## Use Cases
          

### 1. How many total courses are available for Information Systems Program in Northeastern University?

SQL Statement: 

	SELECT a.program_name, 
	COUNT(a.course_name), b.program_url
	FROM neu_course_catalog a 
	LEFT OUTER JOIN
	NEU_Program b 
	ON a.program_name = b.program_name 
	WHERE b.program_name = 'Information Systems'
	GROUP BY a.program_name;
	

### 2.    Which courses do we need to take to do specialization in User Experience Concentration?

SQL Statement:

        Select * from neu_specialization where specialization = 'User Experience Concentration';

### 3.  List top rated professors at NEU whose rating is above 4. Also mention the courses and its description taught by the professor.

SQL Statement:
      
      SELECT a.program_name,b.faculty_name,b.faculty_rating, a.course_name, a.course_description 
      FROM  neu_Course_Catalog a
      RIGHT OUTER JOIN NEU_course_Faculty b 
      ON a.course_id = b.course_id 
      WHERE b.faculty_rating >= 4 
      Order by b.faculty_rating desc;

### 4. What are the core course requirements for Information Systems, Software Engineering Systems and Data Analytics?

SQL Statement:

	SELECT a.program_name, GROUP_CONCAT(a.course_id SEPARATOR  '|'),      
	COUNT(a.course_id), b.program_url
	FROM Course_Core_requirement a
	LEFT JOIN NEU_Program b
	ON a.program_name = b.program_name
	GROUP BY a.program_name;

### 5.  List courses available for Data Analytics Engineering along with its course_outcome.

SQL Statement:

	SELECT
	program_name, course_id,course_name, course_description
	FROM
	NEU_Course_Catalog 
	WHERE program_name = 'Data Analytics Engineering';


### 6.	What is the average overall rating given by students to a professor for a given course?

SQL Statement:

	SELECT faculty_name, round (AVG(faculty_rating),1) as Average_rating 
	FROM NEU_course_Faculty 
	GROUP BY faculty_name;

### 7.Which courses students need to take to do specialization in Big Data Systems concentration and which resources are available for them?

SQL Statement:

	SELECT c.program_name,a.specialization, a.course_id, c.course_name, b.course_rating,b.online_platform
	FROM NEU_Specialization a
	LEFT JOIN NEU_course_catalog c on c.course_id = a.course_id
	LEFT JOIN Resource_material1 b 
	ON a.course_id = b.course_id
	WHERE a.specialization like '%Big Data%';



### 8. List details about all the Masters programs available in Northeastern University

SQL Statement:

	SELECT * FROM NEU_program;


### 9.  Which job positions for students in Data Analytics Engineering and list the details related to those positions?

SQL Statement:

	SELECT program_name, title, company_name,description
	FROM Jobs_info
	WHERE program_name LIKE '%Data%';
 
### 10.  List the events hosted by Northeastern University for students by Data Analytics Engineering Department.
  
SQL Statement:
                      
	SELECT program_name, event_name 
	FROM Neu_Event 
	WHERE program_name = 'Data Analytics Engineering';


### 11. Which professors teach courses related to Big Data Systems and list the ratings given by students for the course?

SQL Statement:

	SELECT a.faculty_name, c.course_rating, b.course_name
	FROM NEU_Course_Faculty a 
	JOIN NEU_Course_Catalog b 
	ON a.course_id = b.course_id
	JOIN Resource_material1 c 
	ON c.course_id = b.course_id 
	WHERE b.course_name like '%Big-Data Systems%'
	ORDER BY c.course_rating;


### 12.   Find the average course rating for Information Systems Program

SQL Statement:

	SELECT b.program_name, AVG(a.course_rating) 
	FROM Resource_material1 a 
	RIGHT JOIN NEU_Course_Catalog  b
	ON a.course_id = b.course_id
	WHERE b.program_name  ='Information Systems';


### 13.   List courses with lowest rating.

SQL Statement:

	SELECT a.course_id,a.course_rating,b.course_name,b.course_description
	FROM Resource_material1 a
	LEFT JOIN NEU_Course_catalog b
	ON a.course_id = b.course_id
	WHERE course_rating = (select min(course_rating) from resource_material1);


### 14.  Find the  professors who taught DAMG 7350, INFO 5100, DAMG 6105, DAMG 7275 courses.

SQL Statement:


	SELECT * FROM NEU_course_Faculty 
	WHERE faculty_name  = ANY (SELECT faculty_name FROM NEU_course_Faculty WHERE course_id  IN ('DAMG 7350', 'INFO 5100', 'DAMG 6105', 'DAMG 7275'));


### 15.  Which resources are available for students who have chosen Information Systems program?

SQL Statement:

	SELECT b.program_name, b.course_id, c.software_download_url, c.professional_certificate, c.online_platform
	FROM NEU_Course_Catalog b
	JOIN Resource_material1 c ON c.course_id = b.course_id 
	WHERE b.program_name = 'Information Systems';

## Sample data from all tables

### Neu_Program  table:

![image](https://user-images.githubusercontent.com/106060204/205521942-81860914-5251-45f3-9e29-bfb565989cb1.png)


### NEU_Course_Catalog Table:
![image](https://user-images.githubusercontent.com/106060204/205522001-3b82ae3e-fc03-491a-acf4-8eaecea794d8.png)


### Jobs_Info Table:
![image](https://user-images.githubusercontent.com/106060204/205522007-cfef9d3c-8452-4806-9d23-4d7ae9525f64.png)


### Course_Core_Requirement Table:
![image](https://user-images.githubusercontent.com/106060204/205522017-87cab419-4b75-4a08-b60d-43c786b5d7b7.png)


### NEU_Event Table: 
![image](https://user-images.githubusercontent.com/106060204/205522022-593119f2-4c0c-4222-a2c7-a204dfb8e0da.png)



### NEU_Course_Faculty Table:
![image](https://user-images.githubusercontent.com/106060204/205522031-84670a48-fb9d-4733-abfe-8f83407c9740.png)


### NEU_Specialization Table:
![image](https://user-images.githubusercontent.com/106060204/205522037-dc3913ec-b3c7-47b9-bd1c-a56bbc6e1ec4.png)


### Resource_Material1 Table:
![image](https://user-images.githubusercontent.com/106060204/205522046-02708eab-7d61-42bd-a92f-c3ae3f07229c.png)

