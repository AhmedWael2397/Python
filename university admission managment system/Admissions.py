
def Menu():
    print("\t\t=== Admissions ===")
    print("1. Add Applicant")
    print("2. Applicant Analyzer")
    print("3. Admissions Report")
    print("4. Exit\n")
    print("================================")

def AddApplicant(A):
    ApplicantID=len(A)+1                                        #0
    name = input("Enter applicant's name: ")                    #1
    gpa = float(input("Enter applicant's GPA: "))               #2
    sat_score = int(input("Enter applicant's SAT score: "))     #3
    Activities=get_Activities_list()                            #4
    Score=0                                                     #5
    state=''                                                    #6
    A.append([ApplicantID,name,gpa,sat_score,Activities,Score,state])

def get_Activities_list():
    try:
        user_input = input("Enter elements of the list separated by spaces: ")
        user_list = user_input.split()
        return user_list
    except ValueError:
        print("Please enter valid strings separated by spaces.")
        return get_Activities_list()
    

ThresholdGPA=2  
ThresholdSAT=5 
thresholdAcceptance=6 
ThresholdRejection=3   
StudentsActivities=['campaigners','tunerz','gamerz']
## POINTS SYSTEM: ( 6 points to get accepted )
#=================================================
#PASSING GPA GIVES 3 POINTS
#PASSING SAT GIVES 3 POINTS
#ACTIVITY ENROLLMENT GIVES 1 POINT 

def ApplicantAnalyzer(A):
    for Applicant in A:
        Applicant[5]=0
        SuccessCounter=0
        WaitingCounter=0
        RejectionCounter=0
        if Applicant[2]>=ThresholdGPA:
            Applicant[5]+=3
        if Applicant[3]>=ThresholdSAT:
            Applicant[5]+=3
        for Activity in Applicant[4]:
            #print(Activity)
            if Activity in StudentsActivities:
                #print("d5lt a +1")
                Applicant[5]+=1
        print("Score= ", Applicant[5])
        if Applicant[5]>=ThresholdRejection and Applicant[5] <thresholdAcceptance:
            Applicant[6]='Waiting list'
            WaitingCounter+=1
        elif Applicant[5]<ThresholdRejection:
            Applicant[6]='Rejected'
            RejectionCounter+=1
        elif Applicant[5] >=thresholdAcceptance:
            Applicant[6]='Accepted'
            SuccessCounter+=1

    
        
def Reporter(A):
    for Applicant in A:
        print("Mr ",Applicant[1]," has scored ",Applicant[5],"POINTS and is ",Applicant[6])


#QualifiedApplicants=[]
