
# Twitter bot for Northeastern-Course-Repository

The overall goal of this project is to create a database containing all relevant resources. The first step towards this is by using data extracted via Twitter pertinent to programs, courses, and resources offered by Northeastern university. We have written a twitter bot that gets tweets, user details, tweet tags, and tweet mentions relevant to our project- Northeastern-Course-Repository. 

## UML diagram for the Northeastern-Course-Repository Twitter domain


![image](https://user-images.githubusercontent.com/106060204/201500622-d9a42637-5337-4367-bbee-67b766eb9cc3.png)



# USE-CASES, SQL STATEMENTS, AND RELATIONAL ALGEBRA

**1.** **Use Case:** Which tags are mostly used while posting tweets for the NEU course repo page? 

Description: The user tweets a comment/question for the NEU course repo. 

Actor: User

Precondition: When a user wants to ask a question regarding anything related to NEU, they tweet using the screen name of the NEU course repo. 

Actor action: The user request a response

System Responses: The requested Twitter handle replies back. 

Post Condition: Customer query successfully answered

Alternate Path: The user question is not relevant or they don’t receive a response. 

**SQL Statement:**

 SELECT 
    t1.tags, t2.tweet
FROM
    Tweet_Tag t1
        RIGHT JOIN
    Tweet_Details t2 ON t1.tweet_id = t2.tweet_id
WHERE
    t1.tags IS NOT NULL;

**Relational Algebra:**

π t1 . tags, t2 . tweet
 σ NOT (t1 . tags = NULL)
  (ρ t1 tweet_tag ⋈ t1 . tweet_id = t2 . tweet_id
   ρ t2 tweet_details)

**2. Use Case:** Which users are requesting information on Twitter related to career Events offered by Northeastern University and how many followers do they have? 

Description: The user tweets a comment/question using relevant keywords: jobs, neujobs, jobsearch.

Actor: User

Precondition: The user wants to ask a question regarding jobs related to programs offered at NEU. 

Actor action: The user request a response

System Responses: Users are directed to relevant job postings and informational websites. 
Alternate Path: The user question is not relevant or they don’t receive a response. 

**SQL Statement:**

SELECT 
    t1.name, t1.twitter_handle, t3.followers_count, t2.tags, t1.tweet
FROM
    Tweet_Details t1
        JOIN
    Tweet_Tag t2 ON t1.tweet_id = t2.tweet_id
       JOIN
	User t3 ON t1.twitter_handle = t3.twitter_handle
WHERE
    tags LIKE '%careers%';

**Relational Algebra:**

π t1 . name, t1 . twitter_handle, t3 . followers_count, t2 . tags, t1 . tweet
 σ tags LIKE "%careers%"
  (ρ t1 tweet_details ⋈ t1 . tweet_id = t2 . tweet_id
   ρ t2 tweet_tag ⋈ t1 . twitter_handle = t3 . twitter_handle
    ρ t3 user)


**3. Use Case:** Which events are hosted by specific departments at NEU for students in their particular programs? 

Description: The event hosting NEU organization tweets about upcoming events on Twitter and on their website. 

Actor: Program Department

Precondition: The event is planned as per student needs and program requirements. 

Actor action: The organizing committee hosts an offline/online event as planned for the students/staff/alumni. 

System Responses: The event is promoted on Twitter and other media to increase sign-ups!  

Post Condition: Students are able to connect with potential employers/seniors/mentors

**SQL Statement:** 

SELECT 
    program_name, events
FROM
    neu_events
WHERE
    program_name = 'Data Analytics Engineering'

**Relational Algebra:**

π program_name, events
 σ program_name = "Data Analytics Engineering" neu_events


**4. Use Case:** What are the specializations offered in the MSIS program by Northeastern university? 

Description: The user searches for concentrations offered by the MSIS program on the program department website. 

Actor: User and Program department 

Precondition: The user looks up the course catalog page for information. 
The program department updates the information on the webpage from time to time (preferably every semester)

Actor action: The user gets a detailed idea about the specializations offered in a course. 

System Responses: The program page takes the user to the correct informational page in the correct sequence. 

Post Condition: Customer can answer questions related to program concentrations and make course-related decisions based on it

Alternate Path: The user seeks concentration-related information on social media and gets the same answers from the program department's social handle, eg Twitter. 

**SQL Statement:**

 SELECT 
    *
FROM
    course_detail
WHERE
    program_name = 'Masters of Science in Information Systems'

**Relational Algebra:**
σ program_name = "Masters of Science in Information Systems" course_detail


**5. Use Case:** List all online platforms available for course INFO 5100 

Description:  The official webpage tweets information about useful platforms for specific courses for the students on Twitter. 

Actor: Program Department twitter handler 

Actor Action: Relevant platform URLs, names, and web pages are shared in the tweet. 

System Responses: The system notifies all followers about the new tweet. 

Post Condition: The students are able to access the posted resources and benefit from them. 

Alternate Path: The resources are published on the program’s website only or offline on an internal repository (like canvas). 

**SQL Statement:**

SELECT 
    d.program_name,
    d.course_name,
    d.course_id,
    r.online_platform
FROM
    course_detail d
        RIGHT JOIN
    resource_materials r ON d.program_name = r.program_name
WHERE
    d.course_id = 'INFO 5100'
    
  **Relational Algebra:**
  
  π d . program_name, d . course_name, d . course_id, r . online_platform
 σ d . course_id = "INFO 5100"
  (ρ d course_detail ⋈ d . program_name = r . program_name
   ρ r resource_materials)

**6. Use Case:** What are the core course requirements of a particular program? 

Description: The program_details table has information about the programs and the core_course_requiremnets have information about the core requirements. Using these we can find the core requirements of a particular program offered by NEU. 

Actor: Students

Precondition: The core requirements are defined by the program department. All programs must have at least 1 core course requirement in COE. 

Actor action: The student can collect information about core course offerings using this detail. 

System Responses: None

**SQL Statement:**

SELECT 
    *
FROM
    course_core_requirement
WHERE
    program_name = 'Masters of Science in Information Systems'


**Relational Algebra:**

σ program_name = "Masters of Science in Information Systems" course_core_requirement


**7. Use Case:**  What are the online resources available for a particular course? 

Description: This gives students a bunch of available online resources they can use to prepare for their course. 

Actor: Students

Precondition: The students must be aware of the content/syllabus offered in the course based on which the online resources are curated. 

Actor action: The students are directed to relevant websites for resources they access. 

System Responses: The system can further ask for ratings. Not yet designed. 

**SQL Statement:**

SELECT 
    program_name, online_platform
FROM
    resource_material
WHERE
    program_name = 'Data Analytics Engineering'

**Relational Algebra:**

π program_name, online_platform
 σ program_name = "Data Analytics Engineering" resource_material
  

**8. Use Case:** What are the professional certifications I can acquire for my program? 

Description: Information about professional certificates available in addition to courses taken by a student (PMP, CAPM, Oracle Developer, Azure, AWS, SQL developer, etc.)

Actor: Student

Precondition: Can check if NEU provides the required certifications at a subsidized cost if not available freely. 

Actor action: Students can find relevant certifications and information about their usability. 


**SQL Statement:**

SELECT 
    program_name, professional_certificate
FROM
    resource_material
WHERE
    program_name = 'Software Engineering Systems''

**Relational Algebra:** 

π program_name, professional_certificate
 σ program_name = "Software Engineering Systems" resource_material  

**9. Use Case:** What are internships/co-op/full-time opportunities available during the course/post-completion of my program? 

Description: The students can look for job opportunities relevant to them. A student looking for co-op roles only can filter results according to them, a full-time opportunity-seeking student can filter according to their search criteria. 

Actor: Students and job catalog maintenance team. 

Precondition: Eligibility criteria for open roles. 

Actor action: Students can apply using the linked application URL, and recruiters will receive interested candidates' profiles on their portal.  

System Responses: Students get application notifications after applying. 

**SQL Statement:**

SELECT 
    *
FROM
    jobs
WHERE
    program_name = 'Data Analytics Engineering';

**Relational Algebra:**

σ program_name = "Data Analytics Engineering" jobs

**10. Use Case:** How many courses have rating more than 5 for a particular program?

Description: The course details retrieved from the Course_Details are joined with the Resource_material table to help students look up software and tools needed during their course. 

Actor:  Students

Actor action:  Students can download the needed software using the link. 

**SQL Statement:**

SELECT 
    program_name, COUNT(course_id) AS TotalCourses, rating
FROM
    course_detail
WHERE
    rating >= 4
GROUP BY program_name
ORDER BY rating DESC;

**Relational Algebra:**

τ rating ↓
 π program_name, COUNT (course_id) → totalcourses, rating
  γ program_name, COUNT (course_id)
   σ rating >= 4 course_detail


**11. Use Case:** Which tweets give information related to events hosted by NEU for students?

Description: The event hosting NEU organization tweets about upcoming events on Twitter and on their website. 

Actor: Program Department

Precondition: The event is planned as per student needs and program requirements. 

Actor action: The organizing committee hosts an offline/online event as planned for the students/staff/alumni. 

System Responses: The event is promoted on Twitter and other media to increase sign-ups!  

Post Condition: Students are able to connect with potential employers/seniors/mentors

**SQL Statement:**

SELECT 
    m.tweet_id, m.twitter_handler, m.source_user, t.tweet
FROM
    tweet_mention m
        JOIN
    tweet_details t ON m.tweet_id = t.tweet_id
WHERE
    m.target_user = 'NEU_CourseRepo'
  
  **Relational Algebra:**
  
  π m . tweet_id, m . twitter_handler, m . source_user, t . tweet
  σ m . target_user = "NEU_CourseRepo"
  (ρ m tweet_mention ⋈ m . tweet_id = t . tweet_id
   ρ t tweet_details)

**12. Use Case:** How many followers does  NEU course repo page has? 

Description: Tells about the follower count for the NEU course repo page. Increase in the number of followers 

Actor: Program Department twitter handle

Precondition: Population of the page with relevant information so as to increase traffic on the page. 

Actor action: This data can be used to gauge interactiveness and relevance of the tweets, posts by the owner. 

System Responses: Use methods to improve quality of content and present relevant content keeping follower increase, decrease, and interaction as a metric of popularity. 

**SQL Statement:**

select count(*) from user;

**Relational Statement:** 

π COUNT (*)
 γ COUNT (*) user


**13. Use Case:** What are the tweets posted by users where NEU_CourseRepo is the target user? 

Description: Helps page handler take a stock of questions/comments posted by any user trying to communicate with the program department. This could be used to improve content. 

Actor: User

Actor action: Tweet/comment using target users' Twitter handle to direct the question to them. 

System Responses: The user tagged in the question gets system generated response followed by specific response. 

**SQL Statement:**

SELECT 
    t.name, m.tweet
FROM
    tweet_details t
        JOIN
    tweet_mention m ON t.tweet_id = m.tweet_id
WHERE
    target_user = 'NEU_CourseRepo'

**Relational Algebra:** 

π t . name, m . tweet
 σ target_user = "NEU_CourseRepo"
  (ρ t tweet_details ⋈ t . tweet_id = m . tweet_id
   ρ m tweet_mention)


**14. Use Case:** What online platforms are available for practice for a particular course? 

Description: Holds information about additional practice platforms available for students.  Redirects the students to relevant platforms. 

Actor: Student and program department 

Actor action: Students are able to find relevant practice platform. Program department updates this information regularly to be current. 

System Responses: 

Post Condition: 

Alternate Path: Information about practice platform is amde available on different channels, and mandated in case where necessary.

**SQL Statement:**

SELECT 
    program_name, course_name, online_platform
FROM
    resource_materials
WHERE
    program_name = 'Master of Science In Computer Software Engineering'
ORDER BY course_name

**Relational Algebra:** 
τ course_name
 π program_name, course_name, online_platform
  σ program_name = "Master of Science In Computer Software Engineering" resource_materials



**15. Use Case:** How many core courses do we need to take for Data Analytics Engineering program? 

Description: Renders core course list and electives separately, for user to identify and understand their program requirements. 

Actor: Program Department

Precondition: Identify the core requirements based on course work. 

Actor action: Program department maintains list of core courses and electives and updates it every year based on program offering. 

**SQL Statement:**

SELECT 
    COUNT(course_id), program_name
FROM
    course_core_requirement
WHERE
    program_name = 'Masters of Science in Data Analytics Engineering'

**Relational Algebra:** 

π COUNT (course_id), program_name
 γ COUNT (course_id)
  σ program_name = "Masters of Science in Data Analytics Engineering" course_core_requirement


# Team Members: 

Utkarsha Shirke (email: shirke.u@northeastern.edu )
Supriya Tripathi (email: tripathi.su@northeastern.edu)
Ishika Misal (email: misal.i@northeastern.edu)


# Outcome:

A consolidated resource repository as a database that is publicly available on GitHub. This will include documentation on how to use the database and a detailed walkthrough by the end of the project. 


