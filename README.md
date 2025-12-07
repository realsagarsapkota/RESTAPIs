As a software developer, I will begin the project by planning out the API endpoints in detail. Then, i will start to build models in the models i will create user by extending the django built in user model where the user can be either job seeker or a recruiter . Similarly, I will create a model name job that has fields like title, description, location, salary, job_type. Then I will create an application model where it stores job_applicant, resume_link, cover letter and the application_status stores whether the applicant has applied , shortlisted or rejected. 

Furthermore, i will move to create serializers to convert the models into the json for the api. In serializer i will create userserializer, jobserializer to show their respective details and applicationserializer to handle job application. Then, i will move to create an endpoints.

For the authentication:
1. POST/register : to create an account
2. POST/login : to login

For Application:
1.POST/jobs/<int:pk>/apply : to apply job
2.GET/applications : to see the application by recruiters and job seekers

For Job:
1.GET/jobs/ : to list all jobs
2.GET/jobs/<int:pk>/ : to view single job
3.POST/jobs : for recruiter to post a new

Then, i will move forward to implement filter. In filter i will choose to filter jobs by location, job type and salary. I will utilize djangofilterbackend by installing django filters.

For authentication and permission i will utilize token based authentication.



