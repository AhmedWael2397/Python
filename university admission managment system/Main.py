import Admissions
Applicants=[]

while True:
     Admissions.Menu()
     userInput=input("==> ")
     if userInput =='1':
          Admissions.AddApplicant(Applicants)
          print("Applicant added to Admissions system successfuly\n")
          print(Applicants)
     elif userInput =='2':
          Admissions.ApplicantAnalyzer(Applicants)
          print("Applicants Analysis Finished")
          print("===============================")
     elif userInput=='3':
          Admissions.Reporter(Applicants)
