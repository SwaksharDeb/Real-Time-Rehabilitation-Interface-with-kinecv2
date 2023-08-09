# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:15:47 2023

@author: hp
"""
import os
def get_gender():
    while True:
        gender = input("Please enter subject's gender (male/female): ").lower()
        if gender == "male" or gender == "female" or gender == "m" or gender == "f":
            return gender
        else:
            print("Invalid input. Please enter 'male' or 'female'.")

def get_patient_type():
    while True:
        patient_type = input("Please enter subject's patient type (stroke/parkinson/neckpain/healthy): ").lower()
        if patient_type in ["stroke", "parkinson", "neckpain", "backpain", "healthy", "s", "p", "np", "bp", "h"]:
            return patient_type
        else:
            print("Invalid input. Please enter 'stroke', 'parkinson', 'pain', or 'healthy'.")

def save_info(directory, name, age, gender, id, patient_type):
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist
    filename = os.path.join(directory, f"{id}_info.txt")
    
    with open(filename, 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"ID: {id}\n")
        file.write(f"Patient Type: {patient_type}\n")

    print(f"Information saved to {filename}")
def main():
    NAME = input("Please enter subject's name: ")
    AGE = input("Please enter subject's age: ")
    gender = get_gender()
    ID = str(input("Please enter subject's ID: "))
    Patient_type = get_patient_type()

    print("Subject's Information:")
    print("Name:", NAME)
    print("Age:", AGE)
    print("Gender:", gender)
    print("ID:", ID)
    print("Patient Type:", Patient_type)

    save_directory = ID
    save_info(save_directory, NAME, AGE, gender, ID, Patient_type)
    return ID

if __name__ == "__main__":
    main()
    