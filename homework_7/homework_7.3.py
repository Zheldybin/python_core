class Doctor:
    def treat(self):
        print("Врач проводит общий осмотр")


class Surgeon(Doctor):
    def treat(self):
        print("Хирург проводит операцию")


class Dentist(Doctor):
    def treat(self):
        print("Дантист лечит зубы")


class Therapist(Doctor):
    def treat(self):
        print("Терапевт проводит терапевтическое лечение")

    def assign_doctor(self, patient):
        if patient.treatment_plan == 1:
            patient.doctor = Surgeon()
        elif patient.treatment_plan == 2:
            patient.doctor = Dentist()
        else:
            patient.doctor = Therapist()

        patient.doctor.treat()


class Patient:
    def __init__(self, treatment_plan):
        self.treatment_plan = treatment_plan
        self.doctor = None


therapist = Therapist()

patient1 = Patient(1)
print("Пациент 1, план лечения:", patient1.treatment_plan)
therapist.assign_doctor(patient1)

patient2 = Patient(2)
print("Пациент 2, план лечения:", patient2.treatment_plan)
therapist.assign_doctor(patient2)


patient3 = Patient(5)
print("Пациент 3, план лечения:", patient3.treatment_plan)
therapist.assign_doctor(patient3)